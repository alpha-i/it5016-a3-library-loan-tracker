# IT5016 Assessment 3: Programming Principles and Concepts

**GitHub repository:** https://github.com/alpha-i/it5016-a3-library-loan-tracker  
**Student number:** 20267608

## Project overview

This repository explores how a small Python library loan tracker can be organised so its code is readable, maintainable, and easier to extend. The tracker can list books, search titles, loan a book, and record a return. Its data is held in memory, so it resets when the program closes; it is a learning project rather than a production library system.

## Repository contents

| Folder or file | Purpose |
| --- | --- |
| `code/original/library_tracker.py` | Original command-line tracker with a `Book` model and `Library` operations. |
| `code/practice/catalogue_search.py` | A focused search example practising case-insensitive matching and list comprehensions. |
| `code/concepts/late_fee_policy.py` | A small concept example that keeps a hypothetical fee rule in a plain function. |
| `research/research-notes.md` | Design question, evidence from the code, limitations, and a reflection prompt. |

## Running the examples

The examples use only the Python standard library and require Python 3.10 or later.

```text
python code/original/library_tracker.py
python code/practice/catalogue_search.py
python code/concepts/late_fee_policy.py
```

## Research question

**When should logic belong to an object, and when is a plain function simpler?**

The project gives examples of both choices. The `Library` object owns the shared catalogue and enforces actions that change its state, such as loaning and returning books. The late-fee calculation is a plain function because it only needs the values passed to it and does not need to access or change the catalogue. This suggests that classes are useful when data and related state-changing operations belong together; small independent calculations can remain functions.

## Design-principle analysis

### Separation of concerns and single responsibility

The `Library` class manages catalogue data and loan rules. `main()` handles user input and menu flow, while `display_books()` formats output. This division means a change to the menu or wording does not have to change the loan rules. It also gives each part a clear job, which makes it easier to locate and understand future changes.

### Avoiding duplicated state

`Book.is_available` derives availability from whether a borrower is recorded. The program does not store a separate availability flag that could contradict the borrower field. This keeps one source of truth for the loan state.

### Validation and meaningful errors

The library checks for blank book details, duplicate IDs, unknown book IDs, blank borrower names, and invalid loan or return operations. It raises `ValueError` for these invalid values; the menu catches that specific error and displays a helpful message. This keeps expected user mistakes from becoming unhandled tracebacks.

### Practice example: searching

`catalogue_search.py` isolates title searching in one function. It trims the user's query and uses `casefold()` for case-insensitive matching. The same search behaviour is used in the main tracker, which makes the practice example relevant to the larger program.

### Concept example: a focused policy function

`late_fee_policy.py` demonstrates a hypothetical fee calculation as a small function with input validation. It returns a value and does not request input, print output, or change shared data. Keeping the policy separate would make it easier to revise the fee rule without mixing it with menu or storage code. The example rate is illustrative only and is not presented as a real library policy.

## Limitations and possible extensions

The tracker supports one copy of each book and keeps data only while it runs. A next version could store multiple copies, keep member records, add due dates, and save data to a file or database. Before adding these features, I would keep the library rules separate from storage and the user interface so each part can change with less impact on the others.

## Personal reflection to complete

Before submitting, add your own short reflection based on using the examples: Which separation made the code easiest for you to understand or change, and what would you improve next? The notes in `research/research-notes.md` can help you form your answer.

## Sources consulted

- Python documentation, [Data Classes](https://docs.python.org/3/library/dataclasses.html).
- Python documentation, [`str.casefold`](https://docs.python.org/3/library/stdtypes.html#str.casefold).
- Python documentation, [Built-in Exceptions: `ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError).
- Python Enhancement Proposal 8, [Style Guide for Python Code](https://peps.python.org/pep-0008/).

The Python references informed the use of dataclasses, case-insensitive searching, value validation, and consistent formatting. The design analysis above explains how those choices apply to this particular project.
