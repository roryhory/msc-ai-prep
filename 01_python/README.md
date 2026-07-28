# Experimental Results CSV Processor

A Python command-line program that reads experimental data from a CSV file, validates its contents, groups valid records by experimental condition, and writes summary statistics to a new CSV file

Invalid rows are reported in the terminal and excluded from the summary

## Input and output

The program reads:

- `baseline_experimental_results.csv`

It creates:

- `processed_results.csv`

The output contains the count, mean, minimum, and maximum measurements for each experimental condition

## Data requirements

The input CSV must contain these columns:

- `sample_id`
- `condition`
- `replicate`
- `measurement`
- `run_date`

Each row must satisfy the following rules:

- `sample_id` must not be blank and must be unique
- `condition` must be 'Control', 'Treatment_A', 'Treatment_B', or 'Treatment_C'
- `replicate` must be an integer from 1 to 6
- `measurement` must be numeric and between 0 and 150
- `run_date` must be a valid date in 'YYYY-MM-DD' format

## Invalid data

If a required CSV header is missing, the program stops without producing a summary.

If an individual row is invalid, the program prints the reason in the terminal, skips the entire row, and continues processing the remaining data.

The original input file is never modified

## Requirements

- Python 3.14.6
- No third-party dependencies

## How to run

Place `baseline_experimental_results.csv` in the same directory as `main.py`.

Run:

```bash
python main.py
```

## Running the tests

Automated tests were written using `pytest` to verify the behaviour of the
validation functions.

To run all tests:

```bash
python -m pytest
```

The current test suite verifies:

- successful header validation
- detection of missing CSV headers
- detection of duplicate sample IDs
- validation of replicate values outside the accepted range

## Implementation

The program first validates that the required headers are present in input CSV file using `validate_headers()`. If they are missing, a ValueError is raised and the program is exited with a terminal message indicating which column is missing from the data.

Each row of the file is then validated using `validate_row()` by confirming each of the required columns contains a valid value according to the rules outlined in [Data Requirements](#data-requirements). Any row containing invalid data will not be included in the summarised data, and the reason will be printed in the terminal.

Once validated, each row is added to `grouped_results`, using its experimental condition as the dictionary key. The value associated with each key is a list containing all valid rows for that condition. The program then calculates the count, mean, minimum, and maximum measurement for each condition and writes the results to processed_results.csv.

## Design decisions

- Rows are validated before their sample IDs are added to the set of used IDs - this prevents an invalid row from breaking a later valid row with the same ID
- Invalid rows are skipped rather than partially repaired because automatically changing source data could introduce incorrect assumptions
- Invalid headers stop the entire program because the remaining rows cannot be interpreted reliably without the expected schema
- Column names must match the required names exactly; aliases such as 'id' instead of 'sample_id' are not supported

## What I learned

- How to use `csv.DictReader` and `csv.DictWriter`
- The difference between validating that required CSV headers exist and checking that fields within individual rows are not blank.
- How sets can be used to detect duplicate values efficiently
- How to raise and catch exceptions without terminating the program from inside validation functions
- Why functions are easier to test when they raise errors instead of printing or calling `sys.exit()` themselves
- Why numeric conversion errors and valid-number range errors need to be handled separateley
- How to use `pytest` to verify both successful execution and expected exceptions.