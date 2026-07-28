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


## Entry 002 — Machine-Learning Concepts Baseline Diagnostic

**Date:** 17 July 2026  
**Plan stage:** Baseline machine-learning concepts diagnostic  
**Status:** Completed  
**Overall confidence:** Amber  
**Important context:** All seven concepts were broadly familiar, but substantial research was needed to formulate complete answers.

### Ratings

| Concept | Rating | Evidence |
|---|---|---|
| Training, validation and test data | Amber | Core roles understood; validation-set neutrality and its distinction from the final test set need refinement |
| Overfitting | Green | Correctly described learning training-specific patterns that fail to generalise |
| Regularisation | Amber | Correct purpose and loss penalty; explanation of model simplicity needs greater precision |
| Data leakage | Amber | Correctly identified invalid information entering training; definition was too narrow |
| Classification versus regression | Green | Correct distinction between discrete labels and continuous outputs |
| Precision versus recall | Red | Definitions were reversed and described as false-positive/false-negative rates |
| Cross-validation | Amber | Correct resampling idea; should distinguish validation folds from the untouched final test set |

### Strengths demonstrated

- Strong intuitive understanding of overfitting and generalisation.
- Correct distinction between classification and regression.
- Good recognition of the roles of training, validation, and test data.
- Able to research unfamiliar details and produce mostly coherent explanations.

### Weak points and recurring issues

1. Conceptual familiarity does not yet translate into precise definitions from memory.
2. Precision and recall are not secure and were reversed.
3. Validation and cross-validation terminology needs clearer separation from final testing.
4. Data leakage was understood too narrowly as information “outside” the training set.
5. Regularisation needs to be understood as constraining complexity, not necessarily making a model physically smaller.

### Correct retrieval anchors

- **Precision:** Of all predicted positives, how many were actually positive?  
  `TP / (TP + FP)`
- **Recall:** Of all actual positives, how many did the model find?  
  `TP / (TP + FN)`
- **Validation data:** Used during model and hyperparameter selection; repeated use means it is not the final unbiased estimate.
- **Test data:** Touched once after model selection for the final performance estimate.
- **Cross-validation:** Repeatedly rotates validation folds within the training data; it does not replace the final held-out test set.
- **Data leakage:** Any information unavailable at prediction time or from validation/test samples that influences model fitting or preprocessing.

### Reproduction status

- Overfitting: Yes.
- Classification versus regression: Yes.
- Training/validation/test roles: Partial.
- Regularisation: Partial.
- Data leakage: Partial.
- Cross-validation: Partial.
- Precision versus recall: No; must be retrieved again.

### Short no-AI retrieval check

1. Write the precision and recall formulas and explain each in words.
2. Explain why repeated tuning on a validation set makes it unsuitable as the final test set.
3. Give three examples of data leakage.
4. Describe five-fold cross-validation while keeping a separate held-out test set.
5. Explain regularisation without using the phrase “smaller model.”

### Study-plan action

Proceed to NumPy and pandas. Revisit these concepts during the classical machine-learning week rather than delaying the schedule now.

---

## Entry 003 — NumPy Fundamentals

**Date:** 17 July 2026  
**Plan stage:** Week 2 — NumPy, pandas and data analysis  
**Status:** Fundamentals exercise completed  
**Overall confidence:** Amber

### Task

Create a two-dimensional NumPy array, inspect its shape, select a row and column, calculate overall/row/column means, and create a Boolean mask.

### Independent work completed

- Created and indexed a 2D NumPy array.
- Used slicing to select a column.
- Calculated the overall mean.
- First derived row and column means using Python loops.
- Rewrote the solution using `mean(axis=...)`.
- Replaced a manual element-by-element mask with `results > 16`.
- Produced a correct, concise final implementation.

### Material AI interventions

| Area | Help received | Underlying issue | Current status |
|---|---|---|---|
| Vectorisation | Explained whole-array operations instead of nested Python loops | General Python habits were carried into NumPy | Corrected |
| Axes | Explained `axis=0` versus `axis=1` | Axis semantics were unfamiliar | Implemented; needs retrieval |
| Boolean masks | Demonstrated `results > 16` | Element-wise comparison was unfamiliar | Implemented |
| References and copies | Explained that `mask = results` shares the same array | Assignment was mistaken for copying | Needs further practice |
| Dimensions | Identified row/column count confusion in the manual column calculation | Shape indices were mixed up | Corrected |

### Strengths demonstrated

- Array creation, indexing, slicing, and shape inspection were correct.
- The initial loops showed that the underlying calculations were understood.
- The final version is idiomatic, vectorised, and preserves the original array.
- Feedback was applied immediately without unnecessary over-polishing.

### Weak points and recurring issues

1. Defaulting to element-by-element loops before considering vectorisation.
2. `axis=0` and `axis=1` are not yet automatic.
3. Assignment, shared references, views, and copies need more practice.
4. Mutation of an aliased array was not anticipated.
5. Row and column dimensions were briefly confused.

### Diagnostic outcome

**I can already:** create arrays, inspect shape, index rows, slice columns, and perform basic aggregations.

**I need to refresh:** axes, vectorisation, Boolean masks, and reference/copy behaviour.

**I cannot yet:** reliably predict view-versus-copy behaviour for NumPy indexing and slicing.

### Reproduction status

- Array creation and shape: Yes.
- Row/column indexing: Yes.
- Overall mean: Yes.
- Means with `axis`: Likely; verify without notes.
- Boolean mask: Likely; verify without notes.
- View/copy behaviour: Partial.

### Short no-AI retrieval check

1. Explain the output shapes of `results.mean(axis=0)` and `results.mean(axis=1)`.
2. Create a mask for values from 14 through 19 inclusive.
3. Use Boolean indexing to return the matching values.
4. Explain why `mask = results` does not make a copy.
5. Demonstrate `results.copy()`.
6. Predict the shape of `results[:, 1:]`.

### Study-plan action

Continue with dtypes, reshaping, transposition, broadcasting, and random-number generation before beginning pandas.

---

## Entry 004 — NumPy Consolidation Session

**Date:** 28 July 2026  
**Plan stage:** Week 2 recovery — NumPy consolidation before pandas  
**Status:** Completed  
**Overall confidence:** Strong Amber, progressing toward Green

### Task

Consolidate the introductory NumPy material through five linked exercises covering:

- array creation, dimensions and slicing;
- reductions using axes;
- Boolean masks and Boolean indexing;
- transposition, flattening and reshaping;
- broadcasting;
- combining and sorting columns; and
- exporting a summary array to CSV.

### Independent work completed

- Recreated the introductory array exercise from memory.
- Correctly calculated overall, row and column means.
- Created a Boolean mask and used it to extract matching values.
- Explained `axis=0` and `axis=1` accurately from memory.
- Explained assignment versus `.copy()` accurately.
- Selected columns, rows and subsets from a 2D experimental array.
- Used `ndim`, `shape`, `size` and `dtype`.
- Calculated per-sample and per-column aggregates.
- Used `np.argmax()` to identify the sample with the highest mean.
- Used Boolean indexing to return matching rows and sample IDs.
- Counted matching measurements with a Boolean-array reduction.
- Transposed, flattened and reconstructed the original array correctly.
- Applied both column-wise and row-wise broadcasting.
- Diagnosed an incompatible broadcasting operation.
- Built a five-column summary array without explicit loops.
- Sorted full rows using `argsort()`.
- Saved the result using `np.savetxt()`.
- Correctly explained vectorisation, Boolean masks, Boolean indexing and array dimensions during the final retrieval check.

### Material AI interventions

| Area | Help received | Underlying issue | Current status |
|---|---|---|---|
| Boolean indexing | Hint to place a Boolean mask inside square brackets to return matching values | Mask creation and value extraction were initially treated as the same operation | Retrieved correctly at session end |
| Shapes | Identified that single-column integer indexing returns shape `(6,)`, not `(6, 1)` | One-dimensional versus two-dimensional selection was unfamiliar | Corrected |
| Axes | Flagged per-sample means/minima/maxima calculated along the wrong axis | Axis selection was not yet automatic | Corrected and later explained accurately |
| Mask versus selected rows | Pointed out that a comparison produced a mask rather than the requested rows | Boolean condition and indexed result were briefly conflated | Corrected and retrieved accurately |
| Transpose/reshape wording | Clarified the intended operation after an initially confusing exercise instruction | Ambiguous wording rather than a conceptual failure | User's reconstruction was correct |
| Broadcasting | Refined explanations using right-to-left dimension comparison | Initial explanation was intuitive but informal | Can explain equal dimensions and dimensions of size `1` |
| CSV export | Explained `np.savetxt()` scientific notation and formatting options | Default output formatting was unfamiliar | Understood |
| Python documentation | Explained strings, quote style and docstrings | New Python convention | Added to glossary |

### Strengths demonstrated

- Moved from one introductory NumPy exercise to a multi-stage data-processing workflow.
- Used vectorised operations instead of explicit element-by-element loops.
- Correctly distinguished masks from data selected by masks by the end of the session.
- Applied axis-based reductions across both rows and columns.
- Understood two different broadcasting patterns: `(6, 3) + (3,)` and `(6, 3) + (6, 1)`.
- Correctly diagnosed a broadcasting failure between trailing dimensions `3` and `2`.
- Challenged an incorrect suggested reshape and demonstrated why it changed the data order.
- Reconstructed the original array correctly after transposing and flattening it.
- Built, sorted and exported a derived summary table independently.
- Final retrieval answers were concise and accurate.

### Weak points and recurring issues

1. **Axis selection:** per-sample versus per-column operations still required correction during the main exercise.
2. **Dimensionality:** `(6,)` versus `(6, 1)` needs continued attention.
3. **Mask versus result:** a Boolean mask was initially stored when the task requested matching rows.
4. **Broadcasting terminology:** intuitive understanding is stronger than formal explanation.
5. **Views and copies:** simple assignment versus `.copy()` is understood, but general NumPy view behaviour remains untested.
6. **Output formatting:** NumPy's default text-export formatting and mixed-column formats are still new.

### Diagnostic outcome

**I can already:** create and inspect arrays; slice rows and columns; use reductions with axes; create and apply Boolean masks; transpose, flatten and reshape arrays; perform basic broadcasting; combine derived columns; sort rows; and export numeric data.

**I need to refresh:** exact output shapes, axis choice, broadcasting rules, views versus copies, and file-format options.

**I cannot yet:** reliably predict whether every NumPy operation returns a view or copy, or use more advanced broadcasting without checking shapes.

### Reproduction status

- Introductory retrieval exercise: Yes.
- Shape, indexing and slicing: Yes.
- Per-row and per-column reductions: Likely; verify once more without notes.
- Boolean masks and indexing: Yes.
- Transposition and reshaping: Yes for the completed example.
- Broadcasting: Yes for 1D column offsets and `(n, 1)` row offsets.
- Sorting and CSV export: Likely; may need to check exact function names or formatting arguments.
- View versus copy behaviour: Partial.

### Short no-AI retrieval check

Complete later without notes:

1. Predict the shape of `experiment[:, 0]`, `experiment[:, 0:1]` and `experiment[2:4, 1:4]`.
2. Calculate per-row ranges using `max(axis=1) - min(axis=1)`.
3. Return full rows satisfying two Boolean conditions.
4. Explain why `(6, 3)` broadcasts with `(3,)` and `(6, 1)`, but not `(2,)`.
5. Rebuild a summary array and sort it in descending order.
6. Demonstrate one NumPy slice that is a view and prove that mutation affects the source.
7. Save a CSV with a custom header, no comment prefix and different formats by column.

### Weekly reflection

**Most important thing learned:**  
NumPy works best when operations are expressed over complete arrays, axes or Boolean selections rather than through explicit Python loops.

**Recurring error or misconception:**  
The main difficulties came from choosing the correct axis and distinguishing an array of Boolean conditions from the values or rows selected by those conditions.

**First task next:**  
Begin pandas with Series and DataFrames, then load a CSV and practise column selection, row filtering, missing-value inspection and grouped summaries.

---
