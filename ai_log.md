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