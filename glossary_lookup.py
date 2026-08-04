#!/usr/bin/env python3
"""Search the structured Markdown glossary from the command line."""

from __future__ import annotations

import argparse
import difflib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


STATUSES = {'Secure', 'Review', 'New'}


@dataclass(frozen=True)
class Entry:
    term: str
    definition: str
    example: str
    status: str
    section: str
    subsection: str


def clean_markdown(value: str) -> str:
    """Remove simple inline Markdown from one table cell."""
    value = value.replace(r'\|', '|')
    value = re.sub(r'`([^`]*)`', r'\1', value)
    value = re.sub(r'\*\*([^*]+)\*\*', r'\1', value)
    return value.strip()


def split_row(line: str) -> list[str]:
    """Split a Markdown table row while preserving escaped vertical bars."""
    line = line.strip()
    if not line.startswith('|'):
        return []

    line = line[1:-1] if line.endswith('|') else line[1:]
    return [
        clean_markdown(cell)
        for cell in re.split(r'(?<!\\)\|', line)
    ]


def parse_glossary(path: Path) -> list[Entry]:
    """Read four-column glossary tables from a Markdown file."""
    if not path.exists():
        raise FileNotFoundError(f'Glossary not found: {path}')

    section = ''
    subsection = ''
    entries: list[Entry] = []

    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('# '):
            section = clean_markdown(line[2:])
            subsection = ''
            continue

        if line.startswith('## '):
            subsection = clean_markdown(line[3:])
            continue

        cells = split_row(line)
        if len(cells) != 4:
            continue

        if all(re.fullmatch(r':?-{3,}:?', cell.replace(' ', '')) for cell in cells):
            continue

        term, definition, example, status = cells
        if status not in STATUSES:
            continue

        entries.append(
            Entry(
                term=term,
                definition=definition,
                example=example,
                status=status,
                section=section,
                subsection=subsection,
            )
        )

    return entries


def normalise(value: str) -> str:
    """Normalise text for case-insensitive searching."""
    return re.sub(r'\s+', ' ', value.casefold()).strip()


def score(entry: Entry, query: str) -> float:
    """Score one glossary entry against a search query."""
    query_n = normalise(query)
    term_n = normalise(entry.term)
    full_text = normalise(
        ' '.join([
            entry.term,
            entry.definition,
            entry.example,
            entry.section,
            entry.subsection,
        ])
    )

    if query_n == term_n:
        return 100
    if term_n.startswith(query_n):
        return 90
    if query_n in term_n:
        return 80
    if query_n in full_text:
        return 65

    tokens = query_n.split()
    token_score = 50 * sum(token in full_text for token in tokens) / len(tokens)
    fuzzy_score = difflib.SequenceMatcher(None, query_n, term_n).ratio() * 60
    return max(token_score, fuzzy_score)


def search(
    entries: list[Entry],
    query: str,
    *,
    status: str | None,
    section: str | None,
    limit: int,
) -> list[Entry]:
    """Return the highest-scoring glossary matches."""
    section_n = normalise(section or '')
    matches: list[tuple[float, Entry]] = []

    for entry in entries:
        if status and entry.status != status:
            continue

        category = normalise(f'{entry.section} {entry.subsection}')
        if section_n and section_n not in category:
            continue

        entry_score = score(entry, query)
        if entry_score >= 25:
            matches.append((entry_score, entry))

    matches.sort(key=lambda item: (-item[0], item[1].term.casefold()))
    return [entry for _, entry in matches[:limit]]


def print_results(entries: list[Entry]) -> None:
    """Print results in a readable terminal format."""
    if not entries:
        print('No matching glossary entries found.')
        return

    for number, entry in enumerate(entries, start=1):
        category = entry.section
        if entry.subsection:
            category += f' > {entry.subsection}'

        print(f'\n{number}. {entry.term} [{entry.status}]')
        print(f'   Category: {category}')
        print(f'   Definition: {entry.definition}')
        if entry.example:
            print(f'   Example: {entry.example}')


def run_query(entries: list[Entry], query: str, args: argparse.Namespace) -> None:
    """Search and display one query."""
    results = search(
        entries,
        query,
        status=args.status,
        section=args.section,
        limit=max(1, args.limit),
    )

    if args.json:
        print(json.dumps(
            [asdict(entry) for entry in results],
            indent=2,
            ensure_ascii=False,
        ))
    else:
        print_results(results)


def main() -> None:
    """Run command-line or interactive glossary search."""
    parser = argparse.ArgumentParser(
        description='Search functions and concepts in the Markdown glossary.'
    )
    parser.add_argument(
        'query',
        nargs='*',
        help='Search words, such as groupby, missing values or broadcasting.',
    )
    parser.add_argument(
        '--file',
        default='glossary.md',
        help='Glossary path (default: glossary.md).',
    )
    parser.add_argument(
        '--status',
        choices=sorted(STATUSES),
        help='Restrict results to one confidence status.',
    )
    parser.add_argument(
        '--section',
        help='Restrict results to a subject or subtopic.',
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=8,
        help='Maximum number of results (default: 8).',
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Print results as JSON.',
    )
    args = parser.parse_args()

    try:
        entries = parse_glossary(Path(args.file))
    except (FileNotFoundError, OSError) as error:
        parser.error(str(error))

    query = ' '.join(args.query).strip()
    if query:
        run_query(entries, query, args)
        return

    print(f'Loaded {len(entries)} glossary entries.')
    print("Enter a search term, or type 'quit' to exit.")

    while True:
        try:
            query = input('\nSearch: ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return

        if query.casefold() in {'quit', 'exit', 'q'}:
            return
        if query:
            run_query(entries, query, args)


if __name__ == '__main__':
    main()
