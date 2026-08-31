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


## Documentation and string conventions

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| String quote style | Single and double quotes are functionally equivalent in Python; consistency matters more than choosing one. | Prefer `'text'`, but `"Rory's result"` avoids escaping. | Secure |
| Docstring | A string placed first in a module, class or function to document its purpose and public behaviour. | Triple double quotes are conventional. | New |
| `__doc__` | Attribute containing an object's docstring. | `print(calculate_mean.__doc__)` | New |
| `help()` | Displays documentation, including available docstrings. | `help(calculate_mean)` | New |

### Docstring example

```python
def calculate_mean(values):
    """Return the arithmetic mean of a non-empty sequence."""
    return sum(values) / len(values)
```

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

## Notebooks and kernels

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| Jupyter notebook | An interactive document that stores code cells, Markdown cells, outputs and notebook metadata in an `.ipynb` file. | Useful for exploratory analysis and explanatory workflows. | Review |
| `.ipynb` | JSON-based file format used by Jupyter notebooks. | The notebook stores cell source, outputs and execution metadata. | Review |
| Code cell | A notebook cell containing executable code sent to the selected kernel. | A pandas import or calculation belongs in a code cell. | Secure |
| Markdown cell | A notebook cell containing formatted explanatory text rather than executable Python. | Use headings such as `## 3. Data-quality checks`. | Secure |
| Output cell state | Results stored beneath a code cell after execution. Stored output may be stale if the source code later changes. | A visible table does not prove the current code produced it in a clean run. | Review |
| Kernel | The running process that executes notebook code and keeps variables in memory. | Restarting the kernel clears in-memory objects. | Review |
| `ipykernel` | The Python package that allows a Python interpreter to act as a Jupyter kernel. | The environment used version 6 after version 7.3.0 caused VS Code execution hangs. | Review |
| Hidden notebook state | Variables or imports left in kernel memory from cells run earlier or out of order. | A notebook may work interactively but fail after restart if it relies on hidden state. | Review |
| Restart and run all | Clears the kernel, then executes every cell in order to test reproducibility. | Use before considering an analysis complete. | Review |
| `sys.executable` | Path to the Python interpreter executing the current process or notebook kernel. | `print(sys.executable)` confirmed the `.venv` interpreter. | Review |
| Current working directory | Directory used as the starting point for relative file paths. It is separate from the interpreter location. | A notebook opened from `tests` resolved paths from that folder. | Review |
| `Path.cwd()` | Returns the process's current working directory as a `Path` object. | `from pathlib import Path; print(Path.cwd())` | Review |
| Relative path | A path interpreted from the current working directory rather than from a fixed drive root. | `../data/results.csv` goes up one directory before entering `data`. | Review |
| Absolute path | A complete path beginning from a drive or filesystem root. | Useful for diagnosis but less portable between computers. | Review |
| Kernel compatibility | Whether the selected kernel package versions work correctly with the notebook client and extensions. | Pinning `ipykernel<7` resolved repeated `Run All` hangs in this environment. | Review |
| `%pip` | IPython/Jupyter magic that runs pip in the environment associated with the current notebook kernel. | `%pip install scikit-learn` helps avoid installing a package into a different interpreter. | Review |
| Package name versus import name | A package can have a different installation name and Python import name. | Install `scikit-learn`; import with `from sklearn.decomposition import PCA`. | Review |
| Kernel/interpreter mismatch | The terminal can use one virtual environment while a notebook kernel executes another interpreter. | Compare `sys.executable` in the notebook with `python -c "import sys; print(sys.executable)"` in the terminal. | Review |

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

# 4. NumPy and scientific Python

## Arrays and dimensions

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| NumPy | A third-party Python package for efficient numerical computing with multidimensional arrays. | Conventionally imported with `import numpy as np`. | Review |
| `np.array()` | Creates a NumPy array from a compatible Python sequence. | `results = np.array([[1, 2], [3, 4]])` | Review |
| Array | A multidimensional, usually homogeneous collection of values. | All values normally share one `dtype`. | Review |
| Dimension / axis | One direction along an array. A 2D array has row and column axes. | Rows are axis 0; columns are axis 1. | Review |
| `ndim` | Number of dimensions in an array. | A matrix-like array has `ndim == 2`. | Review |
| `shape` | Tuple containing the length of each axis. | `(4, 3)` means 4 rows and 3 columns. | Secure |
| `size` | Total number of elements in an array. | Shape `(4, 3)` has size `12`. | Secure |
| `dtype` | The data type stored in the array. | Examples: `int64`, `float64`, `bool`. | Review |
| Homogeneous data | Array elements normally use one common data type. | Assigning Boolean values into an integer array stores them as `1` and `0`. | Review |
| One-dimensional selection | Selecting one column with an integer index removes that axis and returns a 1D array. | `experiment[:, 0]` has shape `(6,)`. | Review |
| Dimension-preserving slice | Selecting a column with a slice preserves two dimensions. | `experiment[:, 0:1]` has shape `(6, 1)`. | Review |

## Indexing and slicing

| Syntax | Purpose | Example | Status |
|---|---|---|---|
| `array[i]` | Selects an item or row along the first axis. | `results[1]` returns the second row. | Secure |
| `array[:, j]` | Selects all rows from one column. | `results[:, 2]` returns the third column. | Review |
| `:` | Slice meaning all entries along an axis. | `results[:, 2]` | Review |
| `array[a:b]` | Selects values from index `a` up to, but not including, `b`. | `results[1:3]` | Review |
| `array[:, a:b]` | Selects a range of columns from all rows. | `results[:, 1:]` | Review |

## Aggregation and axes

| Function / syntax | Definition | Example / note | Status |
|---|---|---|---|
| `array.sum()` | Adds all array elements unless an axis is supplied. | `results.sum()` | Review |
| `array.mean()` | Calculates the arithmetic mean of all elements unless an axis is supplied. | `results.mean()` | Review |
| `array.min()` | Returns the minimum value, optionally along an axis. | `results.min(axis=0)` | Review |
| `array.max()` | Returns the maximum value, optionally along an axis. | `results.max(axis=1)` | Review |
| `array.std()` | Calculates the standard deviation, optionally along an axis. | `replicates.std()` | Review |
| `np.argmax()` | Returns the index of the first maximum value along the requested axis or flattened input. | `sample_ids[np.argmax(sample_means)]` | Review |
| `axis=0` | Reduces down the rows and leaves one result per column. | `results.mean(axis=0)` gives column means. | Review |
| `axis=1` | Reduces across the columns and leaves one result per row. | `results.mean(axis=1)` gives row means. | Review |
| Reduction | An operation that combines multiple array values into fewer values. | Sum, mean, minimum and maximum are reductions. | Review |
| Boolean reduction | Boolean values behave like `1` and `0` in reductions, so `.sum()` counts `True` values. | `(replicates > 60).sum()` | Review |

### Axis memory aid

```python
results.mean(axis=0)  # removes the row axis -> one value per column
results.mean(axis=1)  # removes the column axis -> one value per row
```

## Vectorisation and Boolean selection

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| Vectorisation | Applying an operation to an entire array without explicit Python loops over each element. | `results > 16` | Secure |
| Element-wise operation | An operation performed independently on each array element. | `results * 2` doubles every element. | Review |
| Scalar comparison | A comparison between an array and one value is applied to every element. | `results > 16` | Review |
| Boolean mask | A Boolean array identifying elements that satisfy a condition. | `mask = results > 16` | Secure |
| Boolean indexing | Uses a Boolean mask to return matching values or rows. | `results[results > 16]` | Secure |

## Assignment, views and copies

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| Shared reference | Two names refer to the same array object, so mutation through either name affects the same data. | `second = results` | Review |
| `array.copy()` | Creates an independent copy of an array’s data. | `second = results.copy()` | Secure |
| View | A new array object that may share underlying data with another array. Some NumPy slices create views. | Changing a view may alter the source array. | New |
| Copy | An array with independent data. Changes do not affect the original. | Produced explicitly with `.copy()`. | Secure |

## Transposition, flattening and reshaping

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| Transpose | Swaps the axes of a 2D array. | `(6, 3)` becomes `(3, 6)`. | Review |
| `.T` | Shorthand attribute for transposing an array. | `transposed = replicates.T` | Review |
| `.flatten()` | Returns a flattened one-dimensional copy of an array. | `flat = transposed.flatten()` | Review |
| `.reshape()` | Returns an array with a new compatible shape without changing the number of elements. | `flat.reshape(3, 6)` | Review |
| Data order | Flattening reads values in the order of the current array; reshaping must respect that order to reconstruct the intended arrangement. | Flattening a transposed array differs from flattening the original. | Review |

## Broadcasting

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| Broadcasting | Applies operations to arrays of different but compatible shapes without manually copying values. | `(6, 3) + (3,)` | Review |
| Broadcasting compatibility | Dimensions are compared from right to left; each pair must be equal or one dimension must be `1`. | `(6, 3)` and `(6, 1)` are compatible. | Review |
| Column-wise broadcasting | A 1D array matching the final dimension is applied across every row. | `(6, 3) + (3,)` | Review |
| Row-wise broadcasting | A column-shaped array supplies one value per row and broadcasts across columns. | `(6, 3) + (6, 1)` | Review |
| Broadcasting error | Occurs when corresponding dimensions are neither equal nor `1`. | `(6, 3) + (2,)` fails because `3` and `2` conflict. | Review |


## Linear-algebra functions

| Function / syntax | Definition | Example / note | Status |
|---|---|---|---|
| `np.dot(a, b)` | Calculates a dot product for one-dimensional vectors by multiplying corresponding components and summing the products. | `np.dot(np.array([2, 1]), np.array([-1, 3]))` returns one scalar. | Secure |
| `a @ b` | Performs matrix multiplication using NumPy's shape rules. | `(m, n) @ (n, p)` produces shape `(m, p)`; `(m, n) @ (n,)` produces shape `(m,)`. | Secure |
| `np.linalg` | NumPy namespace containing common linear-algebra functions. | Includes `norm`, `solve`, `matrix_rank`, `det` and `inv`. | Review |
| `np.linalg.norm()` | Calculates a vector or matrix norm; for a one-dimensional vector, the default is its Euclidean magnitude. | `np.linalg.norm(np.array([3, 4]))` returns `5.0`. | Secure |
| `np.linalg.solve()` | Solves a square linear system `A @ x = b` directly when `A` is invertible and a unique solution exists. | `coefficients = np.linalg.solve(matrix, target)` | Secure |
| `np.linalg.matrix_rank()` | Returns the number of linearly independent rows or columns represented by a matrix. | Rank 1 spans one dimension; rank 2 can span a two-dimensional plane. | Secure |
| `np.linalg.det()` | Calculates the determinant of a square matrix. | Use `np.isclose(determinant, 0)` when testing numerical zero. | Secure |
| `np.linalg.inv()` | Calculates the inverse of an invertible square matrix. | Verify both `A @ A_inverse` and `A_inverse @ A` against `np.eye(n)`. | Review |
| `np.linalg.LinAlgError` | Exception raised by NumPy linear-algebra operations when a requested result is not defined or cannot be computed. | Attempting to invert a singular matrix raises this error. | Review |
| `np.eye()` | Creates an identity matrix. | `np.eye(2)` creates a `2 × 2` identity matrix. | Secure |
| `np.outer(a, b)` | Calculates the outer product, producing a matrix from every pairwise product of vector components. | `np.outer(unit_b, unit_b)` constructs a one-dimensional projection matrix. | Review |
| `np.isclose()` | Tests whether two scalar numeric values are equal within floating-point tolerances. | `np.isclose(residual @ direction, 0)` | Secure |
| `np.allclose()` | Tests whether numeric arrays are equal within floating-point tolerances. | `np.allclose(P @ P, P)` | Secure |
| `np.linalg.eig()` | Computes eigenvalues and right eigenvectors of a general square matrix. | Eigenvector `i` is stored in column `eigenvectors[:, i]` and corresponds to `eigenvalues[i]`. | Review |
| `np.linalg.eigh()` | Computes eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix. | Preferred for covariance matrices; eigenvalues are returned in ascending order. | Review |
| `np.cov(..., rowvar=False)` | Calculates a covariance matrix when rows are observations and columns are variables. | `np.cov(X, rowvar=False)` gives one covariance-matrix row/column per feature. | Review |
| `np.sqrt()` | Applies the square-root operation element-wise to an array. | `np.sqrt(eigenvalues)` converts variance magnitudes into standard-deviation scales. | Review |


## Combining, sorting and exporting arrays

| Function / syntax | Definition | Example / note | Status |
|---|---|---|---|
| `np.column_stack()` | Stacks one-dimensional arrays as columns in a new 2D array. | `np.column_stack((u, v))` forms a matrix whose columns are the vectors. | Review |
| `np.argsort()` / `.argsort()` | Returns indices that would sort an array; the same indices can reorder related rows or columns while preserving correspondence. | `idx = np.argsort(eigenvalues)[::-1]`; then `eigenvalues[idx]` and `eigenvectors[:, idx]`. | Review |
| `np.savetxt()` | Saves a NumPy array to a text file. | `np.savetxt('summary.csv', data, delimiter=',')` | Review |
| `fmt` | Controls number formatting in `np.savetxt()` and may specify one format per column. | `fmt=['%.0f', '%.2f']` | Review |
| `header` | Adds a header line when using `np.savetxt()`. | `header='sample_id,mean'` | Review |
| `comments` | Controls the prefix NumPy adds to the header. | `comments=''` removes the default `# `. | New |
| Scientific notation | A compact numeric format such as `1.01e+02`; it changes presentation, not numeric meaning. | The default `np.savetxt()` format commonly uses it. | Review |

## Current NumPy example

```python
import numpy as np

results = np.array([
    [12, 15, 18],
    [10, 14, 20],
    [13, 17, 19],
    [11, 16, 21]
])

mean_all = results.mean()
mean_rows = results.mean(axis=1)
mean_columns = results.mean(axis=0)
mask = results > 16
matching_values = results[mask]
```

---

# 5. pandas and tabular data

## Core structures and labels

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| pandas | A third-party Python package for working with labelled tabular data. | Conventionally imported with `import pandas as pd`. | Review |
| Series | A one-dimensional labelled pandas data structure. | `df['sample_id']` returns a Series with shape `(n,)`. | Secure |
| DataFrame | A two-dimensional labelled table with rows and columns. | `df[['sample_id']]` returns a DataFrame with shape `(n, 1)`. | Secure |
| Index | Labels attached to DataFrame or Series rows. They may be generated automatically or derived from data. | The default index is commonly `0, 1, 2, ...`. | Review |
| Column labels | Names attached to DataFrame columns. | `df['temperature']` selects a column by name. | Secure |
| `pd.DataFrame()` | Creates a DataFrame from arrays, dictionaries or other compatible data. | `pd.DataFrame(experiment, columns=columns)` | Review |
| Homogeneous NumPy input | A DataFrame created from one NumPy array initially inherits the array’s shared dtype. | Integer-looking IDs became `float64` because the source array contained decimals. | Review |

## Loading and inspecting data

| Function / syntax | Definition | Example / note | Status |
|---|---|---|---|
| `pd.read_csv()` | Loads a CSV file into a DataFrame and infers column data types. | `df = pd.read_csv('data/results.csv')` | Review |
| `df.head()` | Returns the first rows of a DataFrame. | `df.head(5)` | Review |
| `df.tail()` | Returns the final rows of a DataFrame. | `df.tail(3)` | New |
| `df.shape` | Tuple containing the number of rows and columns. | `(11, 5)` means 11 rows and 5 columns. | Secure |
| `df.columns` | Index-like collection containing the column labels. | `list(df.columns)` converts it to a list. | Review |
| `df.dtypes` | Series containing the dtype inferred for each column. | Numeric columns may be `int64` or `float64`. | Review |
| `df.info()` | Prints a concise summary of rows, columns, non-null counts, dtypes and memory use. | The method prints its report and returns `None`. | Review |
| `df.describe()` | Returns descriptive statistics for selected columns, including count, mean, standard deviation, quartiles, minimum and maximum. | `clean_df[['temperature', 'mean_result']].describe()` | Review |
| Dtype inference | pandas examines CSV values and chooses suitable data types for each column. | Blank cells in otherwise numeric columns become missing numeric values. | Review |
| `NaN` | A standard marker pandas uses for missing numeric data. | A blank numeric CSV field is commonly loaded as `NaN`. | Review |

## Selecting and filtering

| Syntax / concept | Definition | Example / note | Status |
|---|---|---|---|
| `df['column']` | Selects one column as a Series. | Shape `(n,)`. | Secure |
| `df[['column']]` | Selects a list containing one column and preserves a two-dimensional DataFrame. | Shape `(n, 1)`. | Secure |
| `df[['a', 'b']]` | Selects multiple columns as a DataFrame. | The result retains the requested column labels. | Secure |
| `.loc` | Selects rows and columns by labels or Boolean conditions. | `df.loc[df['temperature'] > 22.5, 'sample_id']` | Review |
| `.iloc` | Selects rows and columns by integer position. | `df.iloc[0:3, 1:4]` | Review |
| Boolean filtering | Uses a Boolean Series to retain rows where the condition is `True`. | `df[df['temperature'] > 22.5]` | Review |
| Selection output contract | A task should specify whether the output is a Series, DataFrame, mask, IDs, values or full rows. | Avoid ambiguous wording such as “return samples”. | Secure |

## Derived columns, sorting and copying

| Function / syntax | Definition | Example / note | Status |
|---|---|---|---|
| `df.assign()` | Returns a DataFrame with one or more added or replaced columns. | `df.assign(mean_result=values)` | Review |
| Direct column assignment | Adds or replaces a column using square brackets. | `df['temperature'] = filled_values` | Review |
| Row-wise pandas reduction | A reduction across selected columns uses `axis=1` to produce one value per row. | `df[['m1', 'm2']].mean(axis=1)` | Review |
| `df.sort_values()` | Returns rows sorted by one or more column values. | `df.sort_values('mean_result')` | Review |
| `df.copy()` | Creates a separate DataFrame object for cleaning or transformation. | `clean_df = raw_df.copy()` | Review |
| Raw versus cleaned data | Preserving the original DataFrame makes cleaning steps auditable and reversible. | Keep `raw_df` unchanged and modify `clean_df`. | Secure |

## Missing values and duplicates

| Function / concept | Definition | Example / note | Status |
|---|---|---|---|
| `df.isna()` | Returns a Boolean DataFrame marking missing values. | `df.isna().sum()` counts missing values per column. | Review |
| `df.dropna()` | Removes rows or columns containing missing values according to supplied rules. | `df.dropna(subset=['measurement_1', 'measurement_2'])` | Review |
| `df.fillna()` | Replaces missing values with a supplied value or rule. | `df['temperature'].fillna(median_temperature)` | Review |
| `df.duplicated()` | Returns a Boolean Series marking duplicated rows. | `df.duplicated().sum()` counts exact duplicates. | Review |
| `df.drop_duplicates()` | Removes repeated rows, keeping the first occurrence by default. | `clean_df = df.copy().drop_duplicates()` | Review |
| Exact duplicate row | A row whose compared column values match an earlier row. | Different from repeating only an identifier. | Secure |
| Duplicated identifier | Two or more rows share an identifier but may differ elsewhere. | A repeated `sample_id` is not automatically an exact duplicate. | Secure |
| Median imputation | Replaces a missing numeric value with the median of observed values. | Calculate the median after earlier cleaning steps specified by the workflow. | Review |
| Cleaning order | The order of cleaning operations can change calculated statistics and final outputs. | Removing a duplicate before calculating the median changed the imputed temperature. | Secure |

## Grouping and aggregation

| Function / concept | Definition | Example / note | Status |
|---|---|---|---|
| `df.groupby()` | Splits rows into groups sharing one or more key values so each group can be summarised or transformed. | `df.groupby('treatment')` | Review |
| Group key | Column or index level used to define groups. | `'treatment'` was the group key. | Review |
| `.agg()` | Applies one or more aggregation functions to grouped or ungrouped data. | Count, mean, minimum and maximum can be calculated together. | Review |
| Named aggregation | Creates explicitly named output columns using `output=('source_column', 'function')`. | `sample_count=('sample_id', 'count')` | Review |
| MultiIndex columns | Hierarchical column labels created when several aggregations are requested using dictionary/list syntax. | `mean_result` may have second-level labels `mean`, `min` and `max`. | Review |
| `as_index=False` | Keeps group keys as normal DataFrame columns instead of moving them into the index. | `df.groupby('treatment', as_index=False)` | Review |
| `reset_index()` | Moves index levels back into ordinary columns and creates a default integer index. | Useful after grouping with the default `as_index=True`. | Review |
| Aggregation output structure | Grouped calculations must control both the values and the resulting column/index layout. | Correct statistics can still be exported incorrectly if labels remain in the index. | Review |

### Named aggregation example

```python
group_summary = (
    clean_df
    .groupby('treatment', as_index=False)
    .agg(
        sample_count=('sample_id', 'count'),
        mean_result=('mean_result', 'mean'),
        minimum_result=('mean_result', 'min'),
        maximum_result=('mean_result', 'max'),
        mean_temperature=('temperature', 'mean')
    )
)
```

## Exporting pandas data

| Function / syntax | Definition | Example / note | Status |
|---|---|---|---|
| `df.to_csv()` | Writes a DataFrame to a CSV file. | `df.to_csv('results.csv', index=False)` | Review |
| `index=False` | Prevents the pandas index from being written as an extra CSV column. | Usually appropriate when the index is not meaningful source data. | Secure |
| Index loss during export | Data stored only in the index is omitted when exporting with `index=False`. | Convert meaningful index labels into columns first. | Review |

---

# 6. Exploratory data analysis and visualisation

## Analysis workflow and interpretation

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| Exploratory data analysis (EDA) | The process of inspecting, summarising and visualising data to understand its quality, distributions, relationships and limitations before formal modelling. | Combine data checks, descriptive statistics, plots and written interpretation. | Review |
| Analysis question | A specific question that determines which summaries and plots are relevant. | “What differences are observed in mean result across treatment groups?” | Secure |
| Descriptive statistics | Numerical summaries that describe observed data without making population-level causal claims. | Count, mean, standard deviation, quartiles, minimum and maximum. | Review |
| Distribution | The pattern of values in a variable, including centre, spread, shape and unusual observations. | A histogram provides a binned view of a numeric distribution. | Review |
| Observed range | Difference between the largest and smallest observed values. | `maximum - minimum` | Secure |
| Sample size | Number of observations included in an analysis or group. | Here, treatment groups contained only two or three observations. | Secure |
| Sampling variability | Natural variation in estimates caused by observing one sample rather than the entire population. | Larger samples generally reduce sampling variability but do not eliminate randomness. | Review |
| Association | Two variables show a pattern of changing together in the observed data. | Association alone does not prove that one causes the other. | Review |
| Causation | A change in one variable directly produces a change in another, under a justified causal design and analysis. | A grouped observational pattern is insufficient by itself. | Review |
| Confounding | A third variable is related to both the explanatory variable and the outcome, making their effects difficult to separate. | Treatment and temperature changed together in the exercise dataset. | Review |
| Limitation | A feature of the data or method that restricts the strength or scope of conclusions. | Tiny groups, missing-data choices and confounding were explicit limitations. | Secure |
| Missing-data trade-off | Both filling and deleting missing observations can affect estimates and introduce bias; the choice depends on context and assumptions. | Median imputation preserves a row but can reduce variation; deletion discards information. | Review |
| Reproducible analysis | An analysis that can be rerun from the same inputs and recorded dependencies in a clean, ordered execution state. | Restart the kernel and run every cell from top to bottom. | Review |

## Matplotlib and plots

| Term / syntax | Definition | Example / note | Status |
|---|---|---|---|
| Matplotlib | A Python plotting library used to create static, animated and interactive visualisations. | Commonly imported through `matplotlib.pyplot`. | Review |
| `matplotlib.pyplot` | A plotting interface that provides functions for creating figures and axes. | `import matplotlib.pyplot as plt` | Review |
| `plt.subplots()` | Creates a Figure and one or more Axes objects. | `fig, ax = plt.subplots()` | Review |
| Figure | The complete Matplotlib canvas that can contain one or more plots. | Stored as `fig` in `fig, ax = plt.subplots()`. | Review |
| Axes | The plotting area on which data, titles and axis labels are drawn. | Call methods such as `ax.hist()` and `ax.set_title()`. | Review |
| `ax.hist()` | Draws a histogram by grouping numeric observations into intervals. | `ax.hist(clean_df['mean_result'], bins=6)` | Review |
| Histogram | A plot showing how many numeric observations fall into adjacent intervals. | Useful for distribution shape, but unstable with very small samples. | Review |
| Bin | One numeric interval used by a histogram. | Too many bins for eight values can exaggerate fragmentation. | Review |
| `DataFrame.boxplot()` | Creates a box plot from DataFrame columns, optionally grouped by a categorical variable. | `clean_df.boxplot(column='mean_result', by='treatment', ax=ax)` | Review |
| Box plot | Summarises a distribution using the median, quartiles, whiskers and possible outliers. | With only two or three values per group, the summary is not stable. | Review |
| Observation-level data | Data containing one row per measured observation rather than one pre-aggregated row per group. | Required to show within-group variation in a box plot. | Review |
| Aggregated data | Data already reduced to summaries such as one mean per group. | A group-summary table cannot recover the original within-group distribution. | Review |
| `ax.set_title()` | Sets the title for one Axes object. | `ax.set_title('Mean result by treatment')` | Review |
| `ax.set_xlabel()` | Sets the x-axis label. | `ax.set_xlabel('Treatment')` | Review |
| `ax.set_ylabel()` | Sets the y-axis label. | `ax.set_ylabel('Mean result')` | Review |
| `fig.suptitle()` | Sets or clears the overall Figure title. | `fig.suptitle('')` removes pandas' automatic box-plot heading. | Review |
| `ax.scatter()` | Draws individual observations as points. | Use separate calls for original and projected points. | Review |
| `ax.plot()` | Draws connected line segments or continuous lines from supplied x- and y-coordinates. | Two endpoints can connect one original point to its projection. | Review |
| `zip()` for paired plotting | Iterates through corresponding rows from two arrays together. | `for original, projected in zip(points, projected_points): ...` | Review |
| `ax.quiver()` | Draws arrows that can represent vectors or directions. | Useful for displaying a projection direction from the origin. | New |
| Equal axis scaling | Uses the same visual scale on the x- and y-axes so angles and lengths are not distorted. | `ax.set_aspect('equal', adjustable='box')` | Review |
| `plt.show()` | Explicitly displays pending Matplotlib figures. | Notebooks may render the last figure automatically, but explicit display is clearer in scripts. | New |

---

# 7. Mathematics

## Linear algebra

| Term / syntax | Definition | Formula / note | Status |
|---|---|---|---|
| Scalar | A single numerical value used alone or to scale a vector. | In `3 * v`, `3` is the scalar. | Secure |
| Vector | A mathematical object with components that can represent magnitude and direction; a one-dimensional NumPy array can represent one computationally. | `np.array([2, 1])` has shape `(2,)`. | Secure |
| Vector component | One coordinate of a vector relative to a chosen basis. | For `(x, y)`, `x` and `y` are the components. | Secure |
| Vector norm | The magnitude or length of a vector. | Euclidean norm: \(\lVert v\rVert=\sqrt{\sum_i v_i^2}\). | Secure |
| Unit vector | A vector with norm 1. | Often written \(\hat{u}\). | Secure |
| Normalisation | Dividing a non-zero vector by its norm to produce a unit vector in the same direction. | \(\hat{u}=u/\lVert u\rVert\). | Secure |
| Euclidean distance | Straight-line distance between two vectors or points. | \(d(a,b)=\lVert a-b\rVert\). | Secure |
| Dot product | Multiplies matching vector components and sums the products, producing a scalar for two one-dimensional vectors. | \(a\cdot b=\sum_i a_i b_i\). | Secure |
| Orthogonal vectors | Non-zero vectors whose dot product is zero; geometrically, their directions are perpendicular. | \(a\cdot b=0\). | Secure |
| Matrix | A rectangular array of numbers arranged in rows and columns. | A matrix with 2 rows and 3 columns has shape \(2 \times 3\). | Secure |
| Matrix dimensions | Written as rows × columns. | \(A_{2\times3}B_{3\times2}\) produces a \(2\times2\) matrix. | Secure |
| Matrix multiplication | Each output entry is the dot product of one row of the first matrix and one column of the second. | Inner dimensions must match. | Secure |
| Matrix-vector multiplication | Applies a matrix to a vector and returns the transformed vector. | A `(2, 2)` matrix multiplied by shape `(2,)` returns shape `(2,)`. | Secure |
| Linear transformation | A mapping that preserves vector addition and scalar multiplication; matrices represent linear transformations once bases are chosen. | The matrix `[[2, 1], [0, 1]]` maps `(x, y)` to `(2x + y, y)`. | Secure |
| Linear combination | A sum of vectors multiplied by scalar coefficients. | \(c_1v_1+c_2v_2+\cdots+c_kv_k\). | Secure |
| Span | The set of every vector reachable through linear combinations of a given set of vectors. | Dependent vectors in \(\mathbb{R}^2\) may span only a line. | Secure |
| Subspace | A subset of a vector space that is itself closed under vector addition and scalar multiplication. | A line through the origin is a one-dimensional subspace of \(\mathbb{R}^2\). | Review |
| Linear dependence | A set is dependent when a linear combination equals the zero vector using coefficients that are not all zero. | Equivalently, at least one vector is redundant and can be expressed using the others. | Secure |
| Linear independence | A set is independent when the only linear combination equal to the zero vector uses all-zero coefficients. | Independent vectors each contribute a new direction to the span. | Secure |
| Basis | A linearly independent set of vectors that spans a vector space. | A basis contains no redundant vectors. | Secure |
| Basis equivalence in finite dimensions | For exactly `n` vectors in an `n`-dimensional space, independence, spanning the space, forming a basis and the column matrix having rank `n` are equivalent statements. | Rank `n` is a consequence or equivalent test, not an additional third requirement. | Secure |
| Rank | The number of linearly independent columns or rows of a matrix; equivalently, the dimension spanned by its columns. | A `2 × 2` matrix has rank 2 when its columns span the plane. | Secure |
| Full rank | A matrix has the largest rank possible for its dimensions. | A square `n × n` matrix is full rank when its rank is `n`. | Secure |
| Linear system | A set of linear equations solved simultaneously. | `A @ x = b`; a square full-rank `A` has a unique solution. | Secure |
| Determinant | A scalar associated with a square matrix that describes signed area, volume or higher-dimensional volume scaling. | For `[[a, b], [c, d]]`, \(\det(A)=ad-bc\). | Secure |
| Determinant magnitude | Absolute factor by which a transformation scales area in 2D, volume in 3D or `n`-dimensional volume generally. | \(|\det(A)|=2\) doubles area in two dimensions. | Secure |
| Determinant sign | Indicates whether the transformation preserves or reverses orientation. | A negative determinant reverses orientation. | Secure |
| Identity matrix | Square matrix that leaves vectors unchanged under multiplication. | \(AI=IA=A\). | Secure |
| Inverse matrix | Matrix that reverses an invertible square transformation. | \(A^{-1}A=AA^{-1}=I\). | Secure |
| Invertible matrix | Square matrix with an inverse; equivalently, it has non-zero determinant and full rank. | `A @ x = b` has one unique solution for every compatible `b`. | Secure |
| Singular matrix | Square matrix without an inverse. | Its determinant is zero and its rank is below full rank. | Secure |
| Unique solution | Exactly one coefficient vector satisfies a linear system. | For square `A`, this occurs when `A` is invertible. | Secure |
| Infinitely many solutions | Multiple coefficient vectors satisfy the same dependent system. | Occurs when the target lies in the column span but the columns are dependent. | Secure |
| No solution | No coefficient vector reaches the target. | Occurs when the target lies outside the column span. | Secure |
| Scalar projection | Signed scalar component of one vector along another direction. | \(\operatorname{comp}_v(u)=\frac{u\cdot v}{\lVert v\rVert}\). | Review |
| Vector projection | Vector component of `u` lying along the line spanned by non-zero `v`. | \(\operatorname{proj}_v(u)=\frac{u\cdot v}{v\cdot v}v\). | Secure |
| Residual | Component left after subtracting a projection from the original vector. | \(r=u-\operatorname{proj}_v(u)\). | Secure |
| Orthogonal decomposition | Writing a vector as a projection plus an orthogonal residual. | \(u=\operatorname{proj}_v(u)+r\), with \(r\cdot v=0\). | Secure |
| Projection matrix | Matrix mapping vectors onto a chosen subspace. | For unit `u`, \(P=uu^T\); for non-unit `v`, \(P=vv^T/(v^Tv)\). | Review |
| Symmetric matrix | Matrix equal to its transpose. | Orthogonal projection matrices satisfy \(P^T=P\). | Review |
| Idempotent matrix | Matrix unchanged by multiplication by itself. | Projection matrices satisfy \(P^2=P\). | Review |
| Column-vector convention | Vectors are multiplied on the right of a transformation matrix. | Use `P @ a`; then \(P(Pa)=(P^2)a\). | Review |
| Eigenvector | A non-zero vector whose direction is preserved by a linear transformation. | \(Av=\lambda v\). | Review |
| Eigenvalue | Scalar factor associated with an eigenvector; the transformation scales that eigenvector by this amount. | In \(Av=\lambda v\), \(\lambda\) is the eigenvalue. | Review |
| Eigenpair | A matching eigenvalue and eigenvector satisfying the eigenvector equation. | `eigenvalues[i]` corresponds to `eigenvectors[:, i]`. | Review |
| Eigenvector sign ambiguity | If \(v\) is an eigenvector, then \(-v\) represents the same eigenvector axis and is also an eigenvector for the same eigenvalue. | PCA implementations may return opposite signs without disagreeing. | Review |
| Diagonal matrix | A square matrix whose off-diagonal entries are zero. | \(\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\). | Review |
| Orthonormal vectors | Vectors that are mutually orthogonal and each have norm 1. | For an orthonormal component matrix \(W\), \(W^TW=I\). | Review |
| Change of basis | Expressing the same vectors using coordinates measured along a different set of basis directions. | PCA changes from original feature axes to covariance-eigenvector axes. | Review |
| Principal-component basis | The orthonormal basis formed by covariance-matrix eigenvectors, usually ordered from largest to smallest eigenvalue. | If \(Z=X_{\text{centered}}W\), columns of `Z` are coordinates in this basis. | Review |
| Diagonalisation of covariance in the PC basis | Expressing covariance in its orthonormal eigenvector basis removes cross-covariance terms. | \(W^T\Sigma W=\Lambda\), where \(\Lambda\) is diagonal. | Review |
| Positive semidefinite matrix | A symmetric matrix satisfying \(x^TAx\ge0\) for every vector \(x\). | Covariance matrices are positive semidefinite, so their eigenvalues are non-negative apart from tiny numerical error. | New |


## Calculus and optimisation

| Term | Definition | Formula / note | Status |
|---|---|---|---|
| Derivative | Instantaneous rate of change of a one-variable function with respect to its input; geometrically, the slope of the tangent to the curve at that point. | $\frac{df}{dx}$ | Secure |
| Power rule | Differentiate $x^n$ by multiplying by $n$ and reducing the exponent by 1. | $\frac{d}{dx}x^n=nx^{n-1}$ | Secure |
| Product rule | Differentiates the product of two functions. | $\frac{d}{dx}[u(x)v(x)]=u'v+uv'$ | Secure |
| Chain rule | Differentiates a composite function by multiplying the outer derivative by the derivative of the inner function. | $\frac{d}{dx}f(g(x))=f'(g(x))g'(x)$ | Secure |
| Stationary point | A point where the derivative or gradient is zero. It may be a local minimum, local maximum or another stationary point. | In one dimension, $f'(x)=0$. | Review |
| Partial derivative | Derivative of a multivariable function with respect to one variable while all other variables are held fixed. | $\frac{\partial f}{\partial x}$ | Secure |
| Constant with respect to a variable | A term containing no instance of the differentiation variable has derivative zero. | For $\partial/\partial x$, $5y^2$ is constant. | Secure |
| Gradient | Vector containing all partial derivatives of a scalar-valued multivariable function. It points in the direction of steepest local increase. | $\nabla f=[\partial f/\partial x_1,\ldots,\partial f/\partial x_n]^T$ | Secure |
| Negative gradient | Direction of steepest local decrease of a differentiable scalar-valued function. | Gradient descent moves in direction $-\nabla L$. | Secure |
| Objective function | Scalar function whose value an optimisation procedure seeks to minimise or maximise. | In the regression exercises, the objective was MSE loss. | Secure |
| Loss function | Objective function measuring model error for a given set of parameters. Lower values are normally preferred when minimising. | $L(w,b)=\frac{1}{n}\sum_i(\hat y_i-y_i)^2$ | Secure |
| Optimisation | Process of finding parameter values that minimise or maximise an objective function. | Gradient descent is one optimisation algorithm. | Secure |
| Model parameter | Value learned or adjusted during model fitting. | In $\hat y=wx+b$, $w$ and $b$ are parameters. | Secure |
| Gradient descent | Iterative optimisation method that updates parameters in the negative-gradient direction. | $\theta_{i+1}=\theta_i-\eta\nabla L(\theta_i)$ | Secure |
| Learning rate | Positive scalar that controls the size of each gradient-descent parameter update. | Usually written $\eta$. Too small can be slow; too large can overshoot or diverge. | Secure |
| Batch gradient descent | Gradient descent where each gradient calculation uses all observations in the dataset. | One update is based on the full-data gradient. | Secure |
| Local minimum | A point whose objective value is no greater than values in a nearby neighbourhood. | It need not be the lowest value over the whole domain. | Secure |
| Global minimum | A point whose objective value is no greater than the value at every other point in the domain. | A convex differentiable objective has no non-global local minima. | Secure |
| Convex function | Function whose line segment between any two points on its graph lies on or above the graph. For a differentiable convex function, every stationary point is a global minimum. | Convexity does not by itself guarantee a unique minimiser. | Review |
| Strictly convex function | Stronger form of convexity that prevents flat line segments between distinct points and gives at most one minimiser when one exists. | Useful distinction when discussing uniqueness. | Review |
| Linear-regression prediction | One-feature linear model mapping an input to a prediction. | $\hat y_i=wx_i+b$ | Secure |
| Mean squared error (MSE) | Mean of squared residuals between predictions and observed targets. | $L(w,b)=\frac{1}{n}\sum_{i=1}^{n}(\hat y_i-y_i)^2$ | Secure |
| Residual in regression | Difference between a prediction and observed target. The sign convention used in the gradient derivation was prediction minus target. | $r_i=\hat y_i-y_i$ | Secure |
| MSE gradient with respect to $w$ | Partial derivative describing how MSE changes locally when the slope/weight parameter changes while $b$ is held fixed. | $\frac{\partial L}{\partial w}=\frac{2}{n}\sum_i x_i(\hat y_i-y_i)$ | Secure |
| MSE gradient with respect to $b$ | Partial derivative describing how MSE changes locally when the intercept changes while $w$ is held fixed. | $\frac{\partial L}{\partial b}=\frac{2}{n}\sum_i(\hat y_i-y_i)$ | Secure |
| Analytical gradient | Gradient obtained by differentiating the objective function symbolically and then evaluating the resulting formula. | Used by the hand derivation and NumPy `gradients()` function. | Secure |
| Numerical gradient | Approximation to a derivative obtained from nearby function values rather than a symbolic derivative formula. | Useful mainly as a verification tool. | Review |
| Central finite difference | Numerical derivative approximation using function values on both sides of the evaluation point. | $f'(x)\approx\frac{f(x+\varepsilon)-f(x-\varepsilon)}{2\varepsilon}$ | Review |
| Gradient check | Comparison of an analytical gradient with an independently calculated numerical gradient to detect derivation or implementation errors. | Approximate agreement gives evidence that the analytical gradient is implemented correctly. | Review |
| Overshoot | A gradient-descent step crosses past a nearby minimum because the update is too large. | Repeated overshoot can produce oscillation or divergence. | Review |
| Divergence | Optimisation behaviour in which parameter values and/or loss move away from a stable minimum rather than converging. | Can occur when the learning rate is too large. | Secure |
| Feature scaling | Transforming feature magnitudes to more comparable numerical scales. It can change gradient magnitudes and optimisation stability. | If $x$ is rescaled, the $x_i$ factor in $\partial L/\partial w$ changes. | Review |
| Standardisation | Common feature-scaling transformation that centres a feature and divides by its standard deviation. | $z=(x-\mu)/\sigma$ | New |

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
| Covariance matrix | Square matrix containing feature variances on the diagonal and pairwise covariances off the diagonal. | For centred \(X\), sample covariance is \(\Sigma=X^TX/(n-1)\). | Review |
| Covariance-matrix symmetry | Pairwise covariance is unchanged by swapping the two variables, so the covariance matrix equals its transpose. | \(\operatorname{Cov}(x,y)=\operatorname{Cov}(y,x)\), hence \(\Sigma^T=\Sigma\). | Review |
| Correlation | Standardised covariance, ranging from \(-1\) to \(1\). It is unitless. | \(\rho=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}\) | Review |


---

# 8. Machine-learning concepts

| Term | Definition | Important distinction / formula | Status |
|---|---|---|---|
| Feature | An input variable used by a model to make a prediction. | Sometimes written as \(X\). | New |
| Target | The value or class the model is trained to predict. | Sometimes written as \(y\). | New |
| Training data | Data used to fit model parameters and learn patterns. | Must not contain information from validation or test samples. | Review |
| Validation data | Data used during model selection and hyperparameter tuning. | Repeated tuning means it is not the final unbiased estimate. | Review |
| Test data | Untouched data used once after model selection to estimate final generalisation performance. | Also called a holdout set. | Review |
| Parameter | A value learned or adjusted during model fitting. | Examples: regression weights and neural-network weights. | Secure |
| Hyperparameter | A setting chosen outside the low-level fitting process. | Examples: tree depth, regularisation strength, number of layers. | Review |
| Principal component analysis (PCA) | Linear dimensionality-reduction method that changes coordinates to orthogonal directions of decreasing variance. | Centre data, eigendecompose covariance, sort eigenpairs, project onto selected eigenvectors. | Review |
| Principal component direction | A covariance-matrix eigenvector used as a new axis through feature space. | PC1 is the eigenvector with the largest eigenvalue. | Review |
| PCA score / projected coordinate | An observation's coordinate along a principal-component direction. | `Z = X_centered @ W`; column `Z[:, i]` contains scores along PC `i`. | Review |
| Components matrix \(W\) | Matrix whose columns are selected orthonormal principal-component directions in the manual column-vector convention. | With 3 features and 2 retained PCs, `W.shape == (3, 2)`. | Review |
| Explained variance | Variance of the centred data along one principal-component direction. | For covariance PCA, explained variance of PC \(i\) is its eigenvalue \(\lambda_i\). | Review |
| Explained-variance ratio | Fraction of total variance captured by one principal component. | \(\lambda_i/\sum_j\lambda_j\). | Review |
| Cumulative explained variance | Total explained-variance ratio captured by the first \(k\) ordered components. | Used to choose the minimum number of PCs meeting a variance threshold. | Review |
| Dimensionality reduction | Representing observations with fewer coordinates than the original feature count. | PCA maps `(n, d)` data to `(n, k)` scores with \(k<d\). | Review |
| PCA reconstruction | Approximate mapping from retained PCA scores back into the original feature space. | \(X_{\text{reconstructed}}=ZW^T+\mu\). | Review |
| PCA reconstruction error | Difference between original observations and their reconstruction after discarded PC directions are removed. | Element-wise MSE: `np.mean((X - X_reconstructed) ** 2)`. | Review |
| PCA fit | Learns the training-data mean, principal directions and explained variances. | Do not refit merely to transform new observations into the existing PCA coordinate system. | Review |
| PCA transform | Centres observations using the learned mean and projects them onto learned principal directions. | \(Z=(X-\mu)W\). | Review |
| PCA inverse transform | Maps PCA scores back through retained component directions and restores the learned mean. | \(X_{\text{reconstructed}}=ZW^T+\mu\). | Review |
| PCA scale sensitivity | Covariance-based PCA is affected by feature units and numerical scales. | Standardisation may be appropriate when scale differences should not determine component importance. | Review |
| PCA linearity limitation | PCA learns linear combinations of original features and therefore may miss important nonlinear structure. | A curved low-dimensional manifold may not be represented efficiently by a few linear PCs. | New |
| Generalisation | Performance on new, unseen data drawn from the intended population. | Central aim of predictive modelling. | Review |
| Overfitting | Learning patterns or noise specific to training data that do not generalise. | Often high training performance and weaker validation performance. | Secure |
| Underfitting | A model is too simple or insufficiently trained to capture relevant patterns. | Poor performance on both training and validation data. | New |
| Regularisation | Methods that discourage excessive model complexity to improve generalisation. | Often adds a penalty to the loss function. | Review |
| Loss function | A numerical objective measuring prediction error for a set of model parameters. | Lower is usually better when the objective is minimised. | Secure |
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

# 9. Review queue

These are the current highest-priority glossary items to retrieve without notes:

1. Why covariance-matrix eigenvectors represent directions of variance.
2. Why the corresponding eigenvalues equal the variances of PCA score columns.
3. What “change of basis” means geometrically.
4. Why the covariance matrix of PCA scores is diagonal.
5. Deriving \(W^T\Sigma W=\Lambda\) from \(\Sigma W=W\Lambda\) and \(W^TW=I\).
6. Principal-component direction versus PCA score / projected coordinate.
7. Explained variance versus explained-variance ratio versus cumulative explained variance.
8. Why reduced reconstruction uses \(ZW^T+\mu\) and represents projection onto the retained subspace.
9. Eigenvector sign ambiguity when comparing PCA implementations.
10. Reordering related NumPy arrays with one `np.argsort()` index array.
11. `np.linalg.eig()` versus `np.linalg.eigh()`.
12. Covariance versus correlation.
13. Feature scaling and why covariance-based PCA is scale-sensitive.
14. Fit versus transform versus inverse transform.
15. Jupyter kernel interpreter versus terminal virtual environment.
16. `%pip` versus terminal `python -m pip`.
17. Restart-and-run-all reproducibility and hidden notebook state.
18. Precision versus recall.
19. Validation set versus final test set.
20. Cross-validation inside a train/test workflow.
21. Convexity versus strict convexity and what each guarantees about minima.
22. Central finite-difference gradient checking and why it is used for verification rather than training.
23. Feature scaling, gradient magnitude and learning-rate stability.
24. One-dimensional NumPy vectors `(n,)` versus explicit row `(1, n)` and column `(n, 1)` shapes.
25. Assignment versus NumPy views versus independent copies.
26. The right-to-left NumPy broadcasting rule.
27. Preserving intended element order through transpose, flatten and reshape.
28. Series versus one-column DataFrame selection.
29. `.loc` versus `.iloc`.
30. Cleaning-order consequences and missing-data trade-offs.
31. Named aggregation syntax.
32. pandas index versus normal data columns.
33. MultiIndex columns produced by multiple grouped aggregations.
34. `plt.subplots()` and the Figure/Axes distinction.
35. Matplotlib syntax for scatter points, direction lines, arrows and connecting segments.
36. Observation-level versus aggregated data for grouped plots.
37. Sampling variability versus “eliminating randomness.”
38. Association versus causation.
39. Confounding and its effect on interpretation.
40. `np.linalg.LinAlgError` handling for singular operations.
41. Classifying unique, infinite and absent solutions on a fresh singular system.
42. Scalar projection versus vector projection.
43. The unit-vector condition in \(P=uu^T\).
44. Deriving \(r\cdot v=0\) from the projection formula.
45. Why projection matrices are symmetric and idempotent.
46. Consistent row-vector versus column-vector notation.
47. Generalising a line projection to projection onto a higher-dimensional subspace.

---

# Appendix — Maintenance and machine-readable formatting rules

This file is a subject-organised reference, not a session history.

## Content maintenance

After each study session:

1. Insert new terms into the most relevant existing subject section.
2. Update existing definitions and confidence statuses in place.
3. Remove duplicates rather than recording the same concept twice.
4. Create a new top-level section only when the material introduces a genuinely new subject area.
5. Renumber and reorder sections so the document remains logically organised.
6. Keep the consolidated review queue near the end.
7. Record chronological progress, mistakes and AI interventions only in `ai_log.md`.

## Machine-readable table contract

The glossary can also act as the data source for a lookup program when these rules are followed:

1. Store every searchable term in a four-column Markdown table.
2. Use the column order: **Term / syntax**, **Definition**, **Example / note**, **Status**.
3. Keep one concept or callable per row.
4. Use top-level and second-level headings as subject and subtopic categories.
5. Put function, method and syntax names in backticks.
6. Use only the statuses **Secure**, **Review** and **New**.
7. Avoid unescaped vertical bars inside table cells; write `\|` when a literal bar is necessary.
8. Keep longer worked examples in code blocks directly below the relevant table rather than embedding multiline content in a row.
9. Do not create chronological “session update” sections in this file.
10. A lookup program should search the term, definition, example, subject and subtopic rather than relying on a manually maintained keyword list.
