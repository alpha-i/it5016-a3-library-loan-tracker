# Research notes: choosing where a rule belongs

## Question explored

**When should logic be a method on an object, and when should it be a plain function?**

The tracker uses methods on `Library` for adding, loaning, returning, and searching because those actions work with the catalogue's shared state. The late-fee example is a plain function because its answer depends only on the supplied day count and rate. It does not need to own or change a library object.

This is a practical design choice rather than a rule that every program needs classes. A class is useful when related data and operations need to stay together. A small calculation can stay simpler as a function. In both cases, keeping one clear responsibility makes the code easier to inspect and change.

## Design evidence in this repository

- `code/original/library_tracker.py` keeps catalogue rules in `Library` and command-line input/output in `main()` and `display_books()`.
- `Book.is_available` derives availability from the borrower field, so the program does not store two values that could contradict one another.
- `code/practice/catalogue_search.py` isolates a search operation and uses `casefold()` to compare titles without case differences.
- `code/concepts/late_fee_policy.py` demonstrates a small policy function with validation and no input/output side effects.

## Limitations to investigate

The tracker stores one copy of each book and loses its data when it exits. A next iteration could add multiple copies and save catalogue and loan data to a file or database. The example fee rule is hypothetical; an actual library would need an agreed policy before this calculation was used.

## Reflection

The clearest design choice for me was keeping the library’s loan rules separate from the menu. This makes the program easier to change because the way a user interacts with it can be updated without changing the loan logic. Next, I would add data storage so books and loans are not lost when the program closes.
