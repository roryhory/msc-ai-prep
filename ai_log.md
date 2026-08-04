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

## Entry 005 — pandas Fundamentals, Cleaning and Grouped Summaries

**Date:** 29 July 2026  
**Plan stage:** Week 2 recovery — pandas and tabular-data analysis  
**Status:** Completed; Week 2 pandas foundations achieved  
**Overall confidence:** Green for the current minimum outcome; grouped aggregation remains a review item

### Tasks

Complete two linked pandas sessions:

1. Build a labelled DataFrame from the existing NumPy experiment, select columns, filter rows, create derived columns, sort the result and export it.
2. Load a CSV containing missing values and a duplicate row, inspect its structure, apply cleaning rules in a specified order, calculate a derived measurement, create a grouped summary and export both cleaned and summarised datasets.

### Independent work completed

- Created a DataFrame from a NumPy array with explicit column labels.
- Correctly predicted its shape, column names and dtypes.
- Distinguished a Series from a one-column DataFrame.
- Selected individual columns and sets of columns.
- Used `.loc` with Boolean conditions to return matching sample IDs.
- Created mean, minimum and maximum result columns.
- Sorted a DataFrame by a named column.
- Exported a DataFrame to CSV without the pandas-generated index.
- Loaded a CSV with `pd.read_csv()`.
- Inspected rows, shape, column names, dtypes and `.info()`.
- Counted missing values and exactly duplicated rows.
- Preserved the raw DataFrame and created a separate cleaned copy.
- Removed exact duplicate rows.
- Filled a missing temperature with the median calculated after duplicate removal.
- Removed rows with missing measurement values.
- Created a row-wise mean measurement.
- First produced the required grouped statistics through several separate `groupby()` operations.
- Reworked the grouped summary into one named aggregation with one `groupby()` and one `.agg()` call.
- Preserved the treatment labels as a normal column and exported both final CSV files correctly.
- Wrote accurate explanations of missing-value handling, duplicates, grouping and preservation of raw data.

### Material AI interventions

| Area | Help received | Underlying issue | Current status |
|---|---|---|---|
| Series versus DataFrame | Explained why `df['column']` returns a Series while `df[['column']]` returns a one-column DataFrame | One-dimensional versus two-dimensional pandas selection was new | Understood |
| Shape reasoning | Reinforced reasoning from input shape through the axis removed by a reduction | Axis output shapes needed a clearer retrieval method | Helpful and retained |
| Exercise wording | Acknowledged that “return samples” was ambiguous between returning IDs and full rows | Prompt ambiguity, not a learner error | Future exercises must specify the exact output type |
| Derived columns | Identified that minimum and maximum values had been calculated but not assigned into the DataFrame | Difference between calculating a Series and modifying the DataFrame | Corrected |
| Object naming | Pointed out that variables ending in `_df` contained Series | Naming did not reflect the returned object type | Understood |
| Cleaning order | Identified that the median was initially calculated from the raw DataFrame rather than after duplicate removal | Ordered cleaning operations can change the result | Corrected |
| Grouped aggregation | Suggested reducing five separate grouped calculations to one `groupby()` and one `.agg()` | The first correct solution was more complicated than necessary | Rewritten |
| MultiIndex columns | Explained why dictionary-style multi-aggregation produced two header levels | Multiple aggregations on one source column create hierarchical column labels | Understood |
| Named aggregation | Explained `output_name=('source_column', 'function')` | Needed a direct way to control grouped-output column names | Implemented |
| Index handling | Identified that treatment labels would be lost when an index-based summary was exported with `index=False` | Index versus data-column distinction | Corrected |
| CSV export | Identified one missing `index=False` argument | Export defaults were not yet automatic | Corrected |
| Method chaining syntax | Identified a misplaced full stop before `.agg()` | New multiline chaining syntax | Corrected |

### Strengths demonstrated

- Transferred NumPy axis knowledge into row-wise pandas calculations.
- Correctly predicted that all columns created from the homogeneous NumPy array would initially use `float64`.
- Asked focused questions about dimensionality instead of memorising bracket syntax.
- Correctly interpreted the ambiguous filtering task as returning sample IDs and challenged the feedback when the wording did not support a single answer.
- Completed the initial grouped summary independently, even though it was verbose.
- Recognised that the first grouped solution was more complicated than necessary.
- Persisted through unfamiliar `groupby()` and `.agg()` behaviour rather than abandoning the task.
- Understood the source-column, aggregation-function and output-column relationship in named aggregation.
- Applied corrections without replacing the entire program.
- Completed both pandas sessions with working exports and accurate conceptual explanations.

### Weak points and recurring issues

1. **Output contracts:** exercises should explicitly state whether the result must be a Series, DataFrame, mask, IDs, values or full rows.
2. **Object types:** variable names should reflect whether the result is a Series or DataFrame.
3. **Cleaning order:** each transformation should be checked against the requested sequence because earlier operations may alter later statistics.
4. **Grouped aggregation syntax:** named aggregation is understood after guidance but is not yet retrievable from memory.
5. **Index versus column:** pandas indexes can disappear during export when `index=False` is used.
6. **Method chaining:** multiline syntax still needs care.
7. **Proofreading:** explanatory comments contained a few spelling and wording errors after the technical work was complete.

### Diagnostic outcome

**I can already:** create, inspect, select, filter, derive, sort, clean, group and export labelled tabular data using pandas.

**I need to refresh:** named aggregation syntax, index handling, cleaning-order consequences, and selection output types.

**I cannot yet:** claim fluent independent use of complex `groupby()` operations, hierarchical indexes or advanced reshaping.

### Reproduction status

- DataFrame creation and inspection: Yes.
- Series versus one-column DataFrame: Yes.
- Label-based filtering with `.loc`: Yes.
- Derived columns and sorting: Yes.
- Missing-value and duplicate inspection: Yes.
- Basic cleaning operations: Likely yes.
- Named grouped aggregation: Partial; reproduce once without notes.
- MultiIndex columns: Conceptually understood; not yet practised beyond this example.
- CSV export without the index: Yes.

### Short no-AI retrieval check

1. Explain the outputs of `df['sample_id']` and `df[['sample_id']]`, including their dimensionality.
2. Explain the difference between `.loc` and `.iloc`.
3. Recreate the missing-value and duplicate inspection steps from memory.
4. Explain why calculating the median before versus after duplicate removal can produce different values.
5. Write one named aggregation that calculates count, mean, minimum and maximum by treatment.
6. Explain the roles of `as_index=False` and `reset_index()`.
7. Explain why `index=False` is normally useful when exporting a DataFrame to CSV.
8. Distinguish an exact duplicate row from a duplicated identifier.

### Weekly reflection

**Most important thing learned:**  
pandas makes tabular analysis easier by attaching labels to rows and columns, but it also introduces an index whose behaviour must be considered during grouping and export.

**Recurring error or misconception:**  
The hardest part was not calculating the statistics; it was controlling the exact structure and names of the grouped output.

**First task next:**  
Build the exploratory-data-analysis notebook using the cleaned dataset, descriptive statistics, labelled plots, written interpretations and explicit limitations.

---

---

## Entry 006 — Exploratory Data Analysis Notebook

**Date:** 30 July 2026  
**Plan stage:** Week 2 recovery — exploratory data analysis and notebook workflow  
**Status:** Completed; Week 2 EDA minimum outcome achieved  
**Overall confidence:** Green for notebook structure and the pandas workflow; Amber for Matplotlib syntax and statistical interpretation

### Tasks

Create a reproducible Jupyter notebook that:

1. presents an analysis question and dataset overview;
2. documents data-quality checks and earlier cleaning decisions;
3. calculates descriptive statistics and grouped summaries;
4. creates labelled visualisations;
5. interprets observed patterns without claiming causation;
6. records limitations and a session reflection;
7. runs successfully from a clean kernel state.

The session also included diagnosing notebook path and kernel problems in VS Code.

### Independent work completed

- Adapted quickly to the `.ipynb` format after an initial period of orientation.
- Organised the analysis into separate Markdown sections with nearby code, output and interpretation cells.
- Loaded and displayed both the raw and cleaned experimental datasets.
- Counted missing values and displayed the exact duplicated row.
- Explained the cleaning decisions and compared the original and cleaned dataset shapes.
- Added a row-wise `mean_result` column.
- Generated descriptive statistics with `describe()`.
- Recreated the flat named grouped aggregation, although the exact `.agg()` syntax was checked.
- Correctly reported the remaining observations in each treatment group.
- Created a labelled histogram of `mean_result`.
- Looked up unfamiliar Matplotlib functions rather than requesting a complete generated solution.
- Replaced the initial group-mean bar chart with a box plot based on individual observations.
- Repeatedly acknowledged that groups of two or three observations cannot support strong conclusions.
- Identified treatment–temperature confounding as a dataset-specific limitation.
- Explained the difference between describing an association and claiming causation.
- Recorded the requirements for notebook reproducibility.
- Restarted the kernel and successfully ran the notebook after resolving the `ipykernel` compatibility issue.

### Material AI interventions

| Area | Help received | Underlying issue | Current status |
|---|---|---|---|
| Relative file paths | Explained that relative paths begin from the current working directory rather than the selected virtual environment | The notebook had accidentally been started from the `tests` directory | Understood after checking the working directory |
| Interpreter versus working directory | Distinguished the `.venv` interpreter from the folder used to resolve relative paths | Kernel selection and file location were initially conflated | Understood |
| Kernel hang | Connected repeated VS Code `Run All` hangs with `ipykernel 7.3.0` and advised pinning below version 7 | Notebook execution queue became stuck despite valid code | Reverting to version 6 resolved the issue |
| Notebook structure | Recommended separate Markdown cells for each analysis section | The relationship between headings, code and interpretation was new | Applied successfully |
| Plot choice | Identified that a bar chart of group means hid the individual observations and did not meet the requested plot type | Visualisation should match both the task and the data structure | Replaced with a box plot |
| Box-plot input | Explained that the plot must use observation-level `clean_df`, not the one-row-per-group summary | A box plot needs a distribution within each group | Understood and implemented |
| Histogram bins | Suggested reducing the number of bins for only eight observations | Too many bins can make a tiny dataset look artificially fragmented | Reduced to six |
| Reproducibility | Expanded the reflection beyond a virtual environment to include inputs, dependencies, cell order, hidden state and a clean top-to-bottom run | Environment isolation alone does not make a notebook reproducible | Corrected |
| Sampling language | Clarified that larger samples reduce sampling variability rather than eliminating randomness | Statistical wording was too absolute | Review needed |
| Missing-data interpretation | Clarified that median imputation is a trade-off rather than automatically bad practice | Cleaning choices were being judged categorically | Review needed; notebook wording remains too absolute |
| Association and causation | Reinforced cautious interpretation and identified treatment–temperature confounding | Group differences cannot establish which variable caused the pattern | Applied |

### Strengths demonstrated

- The pandas operations were straightforward once the notebook interface was understood, showing that the previous two sessions had transferred.
- The notebook has a clear narrative structure rather than being a collection of disconnected code cells.
- The user independently consulted documentation for unfamiliar Matplotlib functions.
- Data-quality checks, descriptive statistics and grouped summaries were reproduced successfully.
- The user consistently resisted overclaiming from a sample of only eight cleaned observations.
- A specific confounding variable was identified rather than relying only on a generic small-sample limitation.
- The environment problem was diagnosed using the active interpreter and `ipykernel` version rather than changing working analysis code.
- The final notebook could be run after restarting the kernel, which is an important reproducibility check.

### Weak points and recurring issues

1. **Matplotlib retrieval:** plotting syntax is new and was looked up; it is not yet independently reproducible.
2. **Named aggregation retrieval:** the relationship `output=('source_column', 'function')` was understood but still needed reference material.
3. **Statistical precision:** larger samples reduce sampling variability; they do not remove the inherent randomness of sampling.
4. **Imputation trade-offs:** median imputation can reduce variability and distort relationships, while deleting a row can also bias results or waste information. It should not be labelled universally as bad practice.
5. **Plot selection:** a box plot technically met the task, but groups of only two or three points make quartiles and whiskers unstable; an individual-point plot would often communicate this dataset more directly.
6. **Conciseness:** repeatedly restating the tiny sample size made some interpretations repetitive. State the limitation clearly once, then refer back to it where necessary.
7. **Proofreading:** several spelling and grammar errors remained after the technical work, including `limitiation`, `respectivley`, `an trend` and `do not known`.

### Diagnostic outcome

**I can already:** create and organise a notebook; combine Markdown, code, outputs and interpretation; reproduce core pandas inspection and grouping operations; create basic labelled plots with reference material; and run a notebook from a clean kernel state.

**I need to refresh:** Matplotlib syntax, named aggregation syntax, the distinction between kernel/interpreter/working directory, sampling-variability language, and balanced discussion of missing-data choices.

**I cannot yet:** independently choose and implement the most informative plot for every dataset, make inferential statistical claims from grouped data, or troubleshoot all Jupyter/VS Code kernel problems without guidance.

### Reproduction status

- Notebook and Markdown-cell structure: Yes.
- Raw and cleaned-data inspection: Yes.
- Descriptive statistics with `describe()`: Likely yes.
- Named grouped aggregation: Partial; exact syntax was looked up.
- Histogram creation and labelling: Partial; Matplotlib is new.
- Box-plot creation and labelling: Partial; implemented after direct guidance.
- Association versus causation: Yes at a conceptual level.
- Confounding: Likely; correctly identified in this dataset.
- Reproducible restart-and-run-all workflow: Yes.
- Virtual environment, kernel and working-directory distinctions: Partial.
- Diagnosing or pinning `ipykernel`: Partial; completed with guidance.

### Short no-AI retrieval check

Complete later using a fresh dataset rather than this experimental-results file:

1. Print the active interpreter and current working directory, and explain why they may point to different folders.
2. Explain the roles of a virtual environment, notebook kernel and `ipykernel`.
3. Explain hidden notebook state and why restarting the kernel before running all cells matters.
4. Create and label a histogram from memory.
5. Create a grouped plot using observation-level data and explain why a one-row-per-group summary is insufficient for a box plot.
6. Write one named aggregation without notes.
7. Explain why increasing sample size reduces sampling variability rather than eliminating randomness.
8. Distinguish association, causation and confounding using a new example.
9. Give one advantage and one disadvantage of median imputation and row deletion.

### Weekly reflection

**Most important thing learned:**  
A notebook is not just Python split into cells: it combines executable analysis, stored outputs and written reasoning, and it is only reproducible when it runs correctly from a clean kernel in a logical top-to-bottom order.

**Recurring error or misconception:**  
The main remaining difficulties were not the pandas calculations. They were environment distinctions, unfamiliar plotting syntax and precise statistical language.

**First task next:**  
Complete a brief no-notes retrieval exercise with a fresh dataset, then move to the next subject in the preparation plan rather than continuing to reuse the eight-row experiment dataset.

---

## Entry 007 — Vectors, Dot Products and Matrix Transformations

**Date:** 4 August 2026  
**Plan stage:** Week 3 — linear algebra foundations  
**Status:** Completed; first linear-algebra notebook achieved  
**Overall confidence:** Green for vector calculations, matrix-shape reasoning and basic transformations

### Tasks

Create a notebook that:

1. retrieves earlier NumPy shape, axis and matrix-multiplication knowledge;
2. calculates vector addition, scalar multiplication, dot products, norms and Euclidean distance;
3. verifies a dot product manually;
4. applies a matrix transformation to two vectors;
5. predicts whether several matrix products are valid and states their output shapes;
6. reflects on vectors, NumPy arrays and matrices as transformations.

### Independent work completed

- Correctly identified the shapes `(3,)`, `(1, 3)` and `(3, 1)`.
- Correctly explained that `axis=0` removes the row axis and `axis=1` removes the column axis.
- Retrieved the matrix-multiplication rule that the inner dimensions must match.
- Distinguished element-wise multiplication from matrix multiplication.
- Calculated vector addition and scalar multiplication correctly.
- Calculated and manually verified the dot product.
- Calculated the norm of each vector and the Euclidean distance between them.
- Applied a two-dimensional transformation matrix to both vectors.
- Predicted the validity and output shape of all four matrix products correctly.
- Explained a matrix as a mapping from an input vector to an output vector.
- Restarted the kernel and successfully ran the notebook in order.

### Material AI interventions

| Area | Help received | Underlying issue | Current status |
|---|---|---|---|
| Vector versus list | Explained that a Python list is a generic container, while a NumPy array can represent a vector and supports numerical vector operations | The stored values looked similar, obscuring their different behaviour | Understood |
| One-dimensional shape | Clarified that shape `(n,)` has no explicit row or column dimension | NumPy's one-dimensional vectors differ from formal row and column vectors | Review |
| Matrix transformation | Refined the interpretation of `(x, y) → (2x + y, y)` as horizontal scaling combined with shear rather than only shear | Geometric terminology was less precise than the calculation | Corrected |
| Reflection prompt | Clarified that “Which shape rule caused the most uncertainty?” asked for honest reflection rather than another calculation | Prompt intent was unclear | Understood |

### Strengths demonstrated

- Retrieval from the NumPy sessions was accurate.
- Shape reasoning was completed before calculation rather than inferred from output.
- Manual arithmetic agreed with NumPy results.
- Matrix-vector multiplication was connected to a geometric coordinate transformation.
- Unclear reflective questions were challenged instead of answered mechanically.
- The technical work was correct before feedback.

### Weak points and recurring issues

1. A one-dimensional NumPy array does not explicitly encode whether a vector is a row or column.
2. Formal mathematical language sometimes lags behind correct computational work.
3. Geometric descriptions of transformations need to identify each component of the mapping precisely.
4. Reflection prompts should state whether they are asking for mathematics or self-assessment.

### Reproduction status

- Vector addition and scalar multiplication: Yes.
- Dot product, norm and Euclidean distance: Yes.
- Manual dot-product verification: Yes.
- Matrix-vector multiplication: Yes.
- Matrix-product shape rules: Yes.
- Geometric interpretation of a new transformation: Likely; retrieve once with a different matrix.
- Vector versus Python list explanation: Yes after clarification.

### Short no-AI retrieval check

1. Explain why `[2, 1] * 3` behaves differently from `np.array([2, 1]) * 3`.
2. State the output shape of `(4, 2) @ (2,)`.
3. Calculate a two-dimensional dot product manually and with NumPy.
4. Explain what a vector norm represents.
5. Describe the mapping produced by a new `2 × 2` transformation matrix.

### Session reflection

**Most important thing learned:**  
A matrix can be interpreted as a transformation that maps each input vector to a new vector, rather than only as a rectangular table of values.

**Recurring error or misconception:**  
The main conceptual uncertainty was the distinction between a mathematical vector, a NumPy representation of a vector and an ordinary Python list.

**First task next:**  
Use linear combinations to study span, basis, linear dependence, linear independence and matrix rank.

---

## Entry 008 — Span, Basis, Linear Independence and Rank

**Date:** 4 August 2026  
**Plan stage:** Week 3 — linear algebra foundations  
**Status:** Completed; span, basis and rank minimum outcome achieved  
**Overall confidence:** Green for the current two-dimensional concepts and calculations

### Tasks

Create a notebook that:

1. defines linear combinations, span, basis, linear dependence and linear independence;
2. calculates several linear combinations;
3. forms matrices from column vectors;
4. predicts and calculates matrix rank;
5. decides whether column vectors are independent and whether they span two-dimensional space;
6. solves for the coefficients representing a target vector;
7. verifies the reconstructed target;
8. reasons about membership in a span without solving;
9. connects basis conditions with rank.

### Independent work completed

- Defined linear combinations, span and basis in geometric terms.
- Calculated all requested linear combinations correctly.
- Used `np.column_stack()` to create matrices from pairs of vectors.
- Correctly predicted rank 1 for the dependent pair and rank 2 for the independent pair.
- Correctly explained that the dependent vectors span a line while the independent pair spans the plane.
- Solved the target-vector coefficients manually before using `np.linalg.solve()`.
- Printed the coefficient shape and verified the reconstruction with matrix multiplication and `np.allclose()`.
- Correctly identified which target vectors belonged to the dependent pair's span.
- Correctly concluded which vector pair formed a basis for two-dimensional space.
- Corrected the scalar-multiple relationship between the dependent vectors.
- Added formal zero-vector definitions of dependence and independence.
- Distinguished basis requirements from consequences and equivalent rank tests.

### Material AI interventions

| Area | Help received | Underlying issue | Current status |
|---|---|---|---|
| Learning sequence | The first plan introduced rank without a dedicated explanation; a separate rank explanation was added before its use | Concept introduction and practice were not sequenced clearly enough | Corrected |
| Scalar relationship | Identified a reversed scalar equation for the dependent vectors | The conclusion was correct but the written equation was not | Corrected |
| Formal dependence | Added the non-trivial zero-vector definition | The initial explanation was intuitive but not fully formal | Review |
| Formal independence | Added the all-zero-coefficients definition | The initial inequality did not specify the coefficient conditions | Review |
| Requested outputs | Suggested printing matrix shapes, ranks and coefficient shape explicitly | Values were calculated but not all requested outputs were displayed | Corrected |
| Floating comparison | Replaced exact array equality with `np.allclose()` for numerical verification | Floating-point solutions should be compared approximately | Implemented |
| Basis feedback | AI initially treated spanning as an additional condition for exactly two independent vectors in two-dimensional space; the user correctly challenged this | Equivalent finite-dimensional conditions were presented as independent requirements | AI correction withdrawn |
| Rank feedback | AI initially phrased rank `n` as a third requirement alongside independence and spanning; the user correctly distinguished it as a consequence or equivalent test | Defining conditions were conflated with consequences | Corrected |

### Strengths demonstrated

- Connected algebraic rank calculations with the geometry of a line versus a plane.
- Predicted ranks before calling NumPy.
- Solved a linear system manually and then verified it computationally.
- Reasoned about span membership without relying on `np.linalg.solve()`.
- Understood that redundant vectors do not add a new dimension to a span.
- Critically evaluated feedback and identified two incorrect or misleading claims.
- Made the important distinction between a definition, a logical consequence and an equivalent test.
- Applied corrections without losing the original reasoning.

### Weak points and recurring issues

1. Formal definitions should be checked against the zero-vector formulation after developing geometric intuition.
2. Written scalar relationships need a quick arithmetic verification.
3. Rank conditions should be stated exactly, such as rank 2 for a two-dimensional basis.
4. Proofreading remains necessary after the mathematics is complete.
5. `np.linalg.solve()` and `np.allclose()` have only been used once and need retrieval on new values.

### Diagnostic outcome

**I can already:** calculate and interpret linear combinations, identify dependent and independent vector pairs, determine their span, use rank to describe the dimension represented by matrix columns, solve a full-rank two-dimensional system and verify its reconstruction.

**I need to refresh:** the formal zero-vector definitions, NumPy's linear-algebra function syntax, and the exact assumptions required by `np.linalg.solve()`.

**I cannot yet:** claim independent fluency with determinants, inverses, eigenvalues, eigenvectors, higher-dimensional bases or PCA.

### Reproduction status

- Linear combinations: Yes.
- Geometric meaning of span: Yes.
- Dependence and independence from scalar relationships: Yes.
- Formal zero-vector definitions: Partial; retrieve without notes.
- Basis reasoning in two-dimensional space: Yes.
- Rank prediction and `np.linalg.matrix_rank()`: Likely yes.
- Manual two-equation solve: Yes.
- `np.linalg.solve()` syntax: Partial; retrieve once.
- Verification with `np.allclose()`: Partial; retrieve once.
- Distinction between basis conditions and rank consequences: Yes.

### Short no-AI retrieval check

1. State the formal zero-vector definitions of linear dependence and independence.
2. Explain the difference between a span and a basis.
3. Predict the rank and span of a new pair of two-dimensional vectors.
4. Explain why exactly two independent vectors in a two-dimensional space automatically span that space.
5. Explain why rank `n` is a consequence or equivalent test for a basis in an `n`-dimensional space, not a third separate requirement.
6. Solve a new full-rank `2 × 2` system with `np.linalg.solve()` and verify it with `np.allclose()`.

### Session reflection

**Most important thing learned:**  
Rank records the number of independent dimensions represented by the matrix columns, linking an algebraic calculation to the geometry of their span.

**Recurring error or misconception:**  
The main issue was wording: intuitive geometric conclusions were correct, but formal definitions and logical relationships needed to distinguish requirements, consequences and equivalent conditions.

**First task next:**  
Study determinants and invertibility as geometric and algebraic properties, then connect them to eigenvalues, eigenvectors and the later PCA implementation.

---
