# AI Assistance Log

This log records material AI assistance used during the MSc Artificial Intelligence preparation plan. Its purpose is to identify recurring weaknesses, distinguish independent work from assisted work, and confirm whether each solution can later be reproduced without AI.

---

## Entry 001 — Experimental Results CSV Processor

**Date:** 15–16 July 2026  
**Plan stage:** Python baseline diagnostic / Week 1  
**Status:** Python diagnostic completed; Week 1 minimum outcome achieved  
**Overall confidence:** Amber, progressing toward green

### Task

Build a Python command-line program that reads experimental results from a CSV file, validates the file and rows, skips invalid data, groups results by condition, calculates summary statistics, writes a new CSV, and includes automated tests.

### Independent work completed

- Wrote the first working procedural implementation without AI-generated code.
- Chose a set for duplicate IDs and a dictionary of lists for grouping conditions.
- Used `csv.DictReader` and `csv.DictWriter`.
- Calculated the required summaries correctly.
- Rewrote the program into functions after receiving review feedback.
- Added strict date validation and four `pytest` tests.
- Wrote and expanded the README.
- Implemented the revisions rather than replacing the program with a complete generated solution.

### Material AI interventions

| Area | Help received | Underlying issue | Current status |
|---|---|---|---|
| CSV schema | Clarified header validation versus blank-field validation | File-level and row-level requirements were not separated | Can now explain and implement both |
| Error handling | Explained why validators should raise errors and `main()` should decide whether to exit | Function responsibility and testability | Implemented |
| Boundaries | Identified that replicate `0` was incorrectly accepted | Edge cases were not listed before coding | Fixed |
| Duplicate IDs | Identified that IDs were recorded before full row validation | State was mutated too early | Fixed |
| Control flow | Identified a `return` inside a loop that stopped validation early | Return placement inside loops | Fixed |
| Exception scope | Explained why range errors were being caught as conversion errors | `try` blocks were too broad | Fixed |
| Error messages | Identified missing f-string prefixes | Python syntax rustiness | Fixed |
| Dates | Advised rejecting the whole row rather than guessing or repairing the date | Validation versus data repair | Implemented |
| Python style | Guidance on naming, built-ins, indentation, and `is None` | Python conventions were rusty | Mostly corrected |
| Tooling | Help with Python installation, virtual environments, `pytest`, PATH, and imports | Limited Python environment experience | Working, but needs repetition |
| Testing | Guidance on discovery, `pytest.raises`, message matching, and imports | Testing was new | Four passing tests |
| README | Guidance on documenting implementation, decisions, usage, and learning | README initially repeated the brief | Substantially improved |

### Strengths demonstrated

- The core algorithm and output were correct in the first version.
- JavaScript knowledge transferred well to Python control flow and data structures.
- Feedback was understood and applied rather than copied mechanically.
- The program improved significantly without being replaced by generated code.
- Questions focused on understanding design choices.
- Progressed from one procedural script to testable functions.
- Created a virtual environment and ran a test suite.

### Weak points and recurring issues

1. Requirements were not decomposed into file-level, row-level, and repair behaviour before coding.
2. Boundary cases were considered after the main path.
3. Return placement and exception scope need more deliberate checking.
4. Python-specific conventions and tooling are not yet automatic.
5. Testing is working but still new.
6. Documentation needs a final proofreading pass after technical work.

### Reproduction status

- **Core CSV processing:** Yes.
- **Header and row validators:** Likely yes; implemented after conceptual feedback.
- **Exception-handling structure:** Likely yes, but should be retrieved once from memory.
- **Basic `pytest` tests:** Yes.
- **Virtual-environment and import setup:** Partially; successful with guidance.
- **Complete rebuild from a blank file:** Not yet explicitly tested.

### Diagnostic outcome

**I can already:** translate a small specification into a working Python program using loops, functions, dictionaries, sets, file I/O, and basic exceptions.

**I need to refresh:** Python conventions, edge-case analysis, function boundaries, exception scope, automated testing, and environment setup.

**I cannot yet:** claim fluent use of type hints, comprehensions, classes, dataclasses, or Python package structure without reference material.

### Short no-AI retrieval check

1. Explain the difference between a missing CSV header and a blank field.
2. Write `validate_replicate()` from memory.
3. Explain why validators raise errors while `main()` decides whether to continue or exit.
4. Activate the virtual environment and run the tests without referring to the chat.
5. Explain why an invalid row should not add its ID to `used_ids`.

### Weekly reflection

**Most important thing learned:**  
Validation functions are easier to reuse and test when they raise clear exceptions, while the top-level program decides how those errors affect execution.

**Recurring error or misconception:**  
Beginning implementation before listing the exact contract and boundary cases led to missed distinctions and subtle control-flow bugs.

**First task next:**  
Complete the mathematics and machine-learning concept portions of the baseline diagnostic, then begin NumPy arrays, shapes, axes, indexing, and broadcasting.

---