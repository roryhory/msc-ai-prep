# MSc Artificial Intelligence Preparation Glossary

**Purpose:** A growing reference for definitions, formulas, Python syntax, functions, and tooling encountered during the MSc preparation plan.

**Status key**

- **Secure** — can explain and use without notes
- **Review** — understood, but retrieval or precision needs practice
- **New** — recently introduced and not yet tested independently

---

# 1. Python language and project structure

## Core syntax and concepts

| Term | Definition | Example / note | Status |
|---|---|---|---|
| Variable | A name that refers to a value or object. | `count = 5` | Secure |
| Function | A reusable block of code defined with `def`. It may accept arguments and return a value. | `def mean(values): ...` | Secure |
| Parameter | A name listed in a function definition. | `value` in `def validate(value):` | Secure |
| Argument | The actual value supplied when calling a function. | `"S001"` in `validate_id("S001")` | Secure |
| Return value | The value sent back by a function using `return`. A function without an explicit `return` returns `None`. | `return measurement_number` | Review |
| Scope | The region of code in which a name is available. Variables created inside a function are normally local to it. | A local variable cannot normally be used outside its function. | Review |
| Boolean | A value that is either `True` or `False`. | `valid = True` | Secure |
| List | An ordered, mutable collection that can contain duplicate values. | `conditions = ["Control", "Treatment_A"]` | Secure |
| Tuple | An ordered, immutable collection. | `(2, 3)` | Review |
| Dictionary | A mutable collection of key–value pairs. | `{"condition": "Control", "count": 18}` | Secure |
| Set | An unordered collection of unique values. Useful for membership checks and duplicate detection. | `used_ids = {"S001"}` | Secure |
| Mutable | An object that can be changed after creation. | Lists, dictionaries, and sets are mutable. | Review |
| Immutable | An object that cannot be changed after creation. | Strings, integers, floats, and tuples are immutable. | Review |
| Module | A Python file containing code that can be imported. | `main.py` is imported with `import main`. | Review |
| Package | A collection of Python modules, usually organised in a directory. | `pytest` is an installed package. | New |
| Standard library | Modules supplied with Python itself. | `csv`, `sys`, and `datetime` | Secure |
| Third-party package | Software installed separately from Python. | `pytest`, NumPy, pandas | Secure |

## Control flow and errors

| Syntax / term | Definition | Example / note | Status |
|---|---|---|---|
| `if` / `elif` / `else` | Runs code conditionally. | `if value < 0: ...` | Secure |
| `for` loop | Repeats code for each item in an iterable. | `for row in reader:` | Secure |
| `try` / `except` | Attempts code and handles specified exceptions if they occur. | Used when converting strings to `int` or `float`. | Secure |
| `raise` | Explicitly creates an exception. | `raise ValueError("Invalid value")` | Secure |
| Exception | An object representing an error or unusual condition during execution. | `ValueError`, `KeyError` | Review |
| `ValueError` | Raised when a value has the correct general type but an invalid value or format. | `int("abc")` raises `ValueError`. | Secure |
| `KeyError` | Raised when a dictionary key does not exist. | `row["sample_id"]` fails if the header is absent. | Review |
| `sys.exit(code)` | Stops the program. Conventionally, `0` means success and a non-zero code means failure. | Best called from top-level program flow, not low-level validators. | Review |
| Separation of responsibilities | Each function should have a clear job. Validation functions identify errors; `main()` decides whether to skip, continue, or exit. | Improves clarity and testability. | Review |
| Premature return | Returning from inside a loop before all intended iterations have completed. | A `return True` inside the first validation loop checked only one field. | Review |
| State mutation | Changing a mutable object, such as adding an ID to a set. | Add an ID only after the whole row is valid. | Review |

## Frequently used syntax

### Function definition

```python
def validate_condition(condition):
    if condition not in required_conditions:
        raise ValueError(f'Invalid condition: {condition}')
```

### Formatted string

```python
message = f'Invalid sample ID: {sample_id}'
```

An f-string evaluates expressions inside `{}`.

### Main guard

```python
if __name__ == "__main__":
    main()
```

This runs `main()` when the file is executed directly, but not when it is imported by a test file.

### Checking for `None`

```python
if minimum is None:
    minimum = value
```

Use `is None` rather than `== None`.

---

# 2. Python file and data handling

| Function / concept | Definition | Example / note | Status |
|---|---|---|---|
| `open()` | Opens a file and returns a file object. | `open("results.csv", "r", newline="")` | Secure |
| Context manager | The `with` statement ensures resources such as files are closed automatically. | `with open(...) as file:` | Secure |
| `csv.DictReader` | Reads each CSV row as a dictionary keyed by the column headers. | `row["measurement"]` | Secure |
| `csv.DictWriter` | Writes dictionaries to a CSV using a specified list of field names. | Requires `writeheader()` and `writerows()`. | Secure |
| CSV header | The first row containing column names. | `sample_id,condition,replicate,...` | Secure |
| Required header validation | Checks that the file contains all expected column names before row processing begins. | Different from checking for blank row values. | Secure |
| Required field validation | Checks that a required value in an individual row is not blank. | `row["condition"] != ""` | Secure |
| Schema | The expected structure and rules of a dataset. | Required headers and accepted value types form part of the schema. | Review |
| Data validation | Checking that data satisfies defined rules without changing it. | Reject a malformed date rather than guessing its meaning. | Secure |
| Data cleaning / normalisation | Deliberately repairing, transforming, or standardising data. | Converting known date formats can be a cleaning step. | Review |

## Numeric conversion

```python
try:
    replicate_number = int(value)
except ValueError:
    raise ValueError("Replicate must be an integer")

if not 1 <= replicate_number <= 6:
    raise ValueError("Replicate must be from 1 to 6")
```

Keep conversion errors and valid-number range errors separate.

## Date parsing

```python
from datetime import datetime

parsed_date = datetime.strptime(value, "%Y-%m-%d")
```

- `strptime()` parses a string into a date/time object.
- `strftime()` formats a date/time object back into a string.

Strict format check:

```python
if parsed_date.strftime("%Y-%m-%d") != value:
    raise ValueError("Date must use YYYY-MM-DD")
```

---

# 3. Python environments, packages, and testing

| Term / command | Definition | Example / note | Status |
|---|---|---|---|
| Python interpreter | The program that executes Python code. | Checked with `python --version`. | Review |
| `PATH` | A system list of directories searched for executable commands. | If `pytest.exe` is not on `PATH`, use `python -m pytest`. | Review |
| Virtual environment | An isolated Python environment for one project, with its own interpreter reference and installed packages. | Created in `.venv/`. | Review |
| Dependency | A package required by a project. | `pytest`, NumPy, pandas | Secure |
| Dependency pinning | Recording exact package versions for reproducibility. | `python -m pip freeze > requirements.txt` | New |
| `pip` | Python’s package installer. | `python -m pip install pytest` | Secure |
| `pytest` | A third-party testing framework for Python. | Discovers files such as `test_main.py`. | Review |
| Unit test | A small automated test of one function or behaviour. | Testing that `validate_replicate("-1")` raises an error. | Secure |
| Happy path | A valid input path that should complete without errors. | Valid headers should not raise an exception. | Secure |
| Edge case | An input near a boundary or unusual condition. | Replicate `0`, `7`, empty headers | Secure |
| Test discovery | The rules pytest uses to locate tests. | Files named `test_*.py`; functions named `test_*`. | Review |
| `pytest.raises` | Confirms that code raises an expected exception. | `with pytest.raises(ValueError): ...` | Secure |
| Import path | Locations Python searches when importing modules. | Running `python -m pytest` from the project root allowed `import main`. | Review |

## Virtual environment commands

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install pytest
python -m pytest
deactivate
```

## Basic pytest example

```python
import pytest
import main


def test_invalid_replicate():
    with pytest.raises(
        ValueError,
        match="value must be an integer from 1 to 6"
    ):
        main.validate_replicate("-1")
```

---

# 4. Mathematics

## Linear algebra

| Term | Definition | Formula / note | Status |
|---|---|---|---|
| Matrix | A rectangular array of numbers arranged in rows and columns. | A matrix with 2 rows and 3 columns has shape \(2 \times 3\). | Secure |
| Matrix dimensions | Written as rows × columns. | \(A_{2\times3}B_{3\times2}\) produces a \(2\times2\) matrix. | Secure |
| Matrix multiplication | Each output entry is the dot product of one row of the first matrix and one column of the second. | Inner dimensions must match. | Review |
| Linear system | A set of linear equations solved simultaneously. | Can use substitution or elimination. | Secure |

## Calculus

| Term | Definition | Formula / note | Status |
|---|---|---|---|
| Derivative | Measures the instantaneous rate of change of a function. | \(\frac{df}{dx}\) | Secure |
| Power rule | Differentiate \(x^n\) by multiplying by \(n\) and reducing the exponent by 1. | \(\frac{d}{dx}x^n=nx^{n-1}\) | Secure |
| Chain rule | Differentiates a composite function by multiplying the outer derivative by the inner derivative. | \(\frac{d}{dx}e^{2x}=2e^{2x}\) | Secure |
| Partial derivative | Differentiates a multivariable function with respect to one variable while treating all others as constants. | \(\frac{\partial h}{\partial x}\) | Review |
| Constant with respect to a variable | A term containing no instance of the differentiation variable has derivative zero. | For \(\partial/\partial x\), \(5y^2\) is constant. | Review |

## Probability and statistics

| Term | Definition | Formula / note | Status |
|---|---|---|---|
| Prior probability | Probability assigned before observing new evidence. | \(P(D)\) | Secure |
| Likelihood | Probability of observed evidence assuming a hypothesis is true. | \(P(+\mid D)\) | Secure |
| Posterior probability | Updated probability after incorporating evidence. | \(P(D\mid +)\) | Secure |
| Bayes’ theorem | Updates a prior using the likelihood of observed evidence. | \(P(D\mid +)=\frac{P(+\mid D)P(D)}{P(+)}\) | Secure |
| Sensitivity | Proportion of actual positive cases correctly identified. | Same as recall / true-positive rate. | Review |
| False-positive rate | Proportion of actual negative cases incorrectly predicted positive. | \(FP/(FP+TN)\) | Review |
| Mean | Arithmetic average. | Sum divided by count. | Secure |
| Variance | Average squared distance of values from their mean. | Units are squared. | Review |
| Standard deviation | Square root of variance, returning to the original units. | \(\sigma=\sqrt{\mathrm{Var}(X)}\) | Review |
| Covariance | Measures whether two variables tend to deviate from their means in the same or opposite directions. | Positive: move together; negative: move oppositely. | Review |
| Correlation | Standardised covariance, ranging from \(-1\) to \(1\). It is unitless. | \(\rho=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}\) | Review |

---

# 5. Machine-learning concepts

| Term | Definition | Important distinction / formula | Status |
|---|---|---|---|
| Feature | An input variable used by a model to make a prediction. | Sometimes written as \(X\). | New |
| Target | The value or class the model is trained to predict. | Sometimes written as \(y\). | New |
| Training data | Data used to fit model parameters and learn patterns. | Must not contain information from validation or test samples. | Review |
| Validation data | Data used during model selection and hyperparameter tuning. | Repeated tuning means it is not the final unbiased estimate. | Review |
| Test data | Untouched data used once after model selection to estimate final generalisation performance. | Also called a holdout set. | Review |
| Parameter | A value learned from training data. | Examples: regression weights, neural-network weights. | New |
| Hyperparameter | A setting chosen outside the low-level fitting process. | Examples: tree depth, regularisation strength, number of layers. | Review |
| Generalisation | Performance on new, unseen data drawn from the intended population. | Central aim of predictive modelling. | Review |
| Overfitting | Learning patterns or noise specific to training data that do not generalise. | Often high training performance and weaker validation performance. | Secure |
| Underfitting | A model is too simple or insufficiently trained to capture relevant patterns. | Poor performance on both training and validation data. | New |
| Regularisation | Methods that discourage excessive model complexity to improve generalisation. | Often adds a penalty to the loss function. | Review |
| Loss function | A numerical measure of prediction error optimised during training. | Lower is usually better. | New |
| Data leakage | Information unavailable at genuine prediction time, or information from validation/test samples, influences fitting or preprocessing. | Produces overly optimistic performance estimates. | Review |
| Classification | Predicts a discrete class or category. | Benign/malignant, yes/no | Secure |
| Regression | Predicts a continuous numerical value. | Price, temperature, quantity | Secure |
| True positive (TP) | Predicted positive and actually positive. | Correct positive prediction. | Review |
| False positive (FP) | Predicted positive but actually negative. | Type I error in some statistical contexts. | Review |
| True negative (TN) | Predicted negative and actually negative. | Correct negative prediction. | Review |
| False negative (FN) | Predicted negative but actually positive. | Missed positive case. | Review |
| Precision | Among predicted positives, the proportion actually positive. | \(TP/(TP+FP)\) | Review |
| Recall | Among actual positives, the proportion correctly identified. | \(TP/(TP+FN)\) | Review |
| Cross-validation | Repeatedly trains on some folds and evaluates on another fold to estimate performance and compare models. | Validation folds come from the training data; keep a final test set separate. | Review |
| Fold | One subset used in cross-validation. | In 5-fold CV, each fold is used once for validation. | New |
| Holdout set | A portion of data kept separate from fitting and model selection. | Usually refers to the final test set. | Review |

## Precision and recall memory anchors

- **Precision:** “When the model says positive, how often is it right?”
- **Recall:** “Of all real positives, how many did the model find?”

---

# 6. Review queue

These are the current highest-priority glossary items to retrieve without notes:

1. Precision versus recall.
2. Validation set versus final test set.
3. Cross-validation inside a train/test workflow.
4. Covariance versus correlation.
5. Exact role of a virtual environment versus `requirements.txt`.
6. Partial derivatives.
7. Matrix multiplication arithmetic checks.
8. Exception scope and return placement in Python.

---

# 7. Update format for future sessions

After each session, add entries using this template:

```markdown
## New terms — YYYY-MM-DD

### Definitions

| Term | Definition | Example / formula | Status |
|---|---|---|---|
| ... | ... | ... | New |

### Python functions and syntax

| Function / syntax | Purpose | Minimal example | Status |
|---|---|---|---|
| ... | ... | ... | New |

### Status changes

- `term`: New → Review
- `term`: Review → Secure
```
