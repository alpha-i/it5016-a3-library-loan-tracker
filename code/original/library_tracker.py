"""A small, in-memory library loan tracker for IT5016 Assessment 3."""

from dataclasses import dataclass


@dataclass
class Book:
    """Represent one book and its current loan state."""

    book_id: str
    title: str
    author: str
    borrower: str | None = None

    @property
    def is_available(self) -> bool:
        """Derive availability from the loan state instead of duplicating it."""
        return self.borrower is None


class Library:
    """Own the catalogue and enforce the basic loan rules."""

    def __init__(self) -> None:
        # A dictionary gives each book one stable ID and a direct lookup path.
        self._books: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        """Add a book after checking the catalogue invariant."""
        if not book.book_id.strip() or not book.title.strip() or not book.author.strip():
            raise ValueError("Book ID, title, and author are required.")
        if book.book_id in self._books:
            raise ValueError(f"Book ID {book.book_id!r} already exists.")
        self._books[book.book_id] = book

    def find_book(self, book_id: str) -> Book:
        """Return a book by ID, translating a low-level lookup error."""
        try:
            return self._books[book_id]
        except KeyError:
            raise ValueError(f"No book found with ID {book_id!r}.") from None

    def loan_book(self, book_id: str, borrower: str) -> None:
        """Loan an available book to a non-empty borrower name."""
        if not borrower.strip():
            raise ValueError("Borrower name cannot be empty.")

        book = self.find_book(book_id)
        if not book.is_available:
            raise ValueError(f"{book.title!r} is already on loan.")

        book.borrower = borrower.strip()

    def return_book(self, book_id: str) -> None:
        """Return a book that is currently on loan."""
        book = self.find_book(book_id)
        if book.is_available:
            raise ValueError(f"{book.title!r} is not currently on loan.")

        book.borrower = None

    def search_titles(self, query: str) -> list[Book]:
        """Find titles containing the query, ignoring letter case."""
        normalized_query = query.strip().casefold()
        if not normalized_query:
            return []
        return [
            book
            for book in self._books.values()
            if normalized_query in book.title.casefold()
        ]

    def list_books(self) -> list[Book]:
        """Return the catalogue in a predictable title order."""
        return sorted(self._books.values(), key=lambda book: book.title.casefold())


def display_books(books: list[Book]) -> None:
    """Format books for the command-line interface, not for the domain model."""
    if not books:
        print("No matching books.")
        return

    for book in books:
        status = f"On loan to {book.borrower}" if book.borrower else "Available"
        print(f"{book.book_id}: {book.title} by {book.author} — {status}")


def build_sample_library() -> Library:
    """Create a small catalogue so the program can be tried immediately."""
    library = Library()
    library.add_book(Book('B001', 'The Hobbit', 'J. R. R. Tolkien'))
    library.add_book(Book('B002', 'Kindred', 'Octavia E. Butler'))
    library.add_book(Book('B003', 'The Left Hand of Darkness', 'Ursula K. Le Guin'))
    return library


def main() -> None:
    """Run the text menu and translate expected rule errors into messages."""
    library = build_sample_library()

    while True:
        print("\nLibrary Loan Tracker")
        print("1. List books")
        print("2. Search by title")
        print("3. Loan a book")
        print("4. Return a book")
        print("5. Quit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                display_books(library.list_books())
            elif choice == "2":
                query = input("Title search: ")
                display_books(library.search_titles(query))
            elif choice == "3":
                book_id = input("Book ID: ").strip()
                borrower = input("Borrower name: ")
                library.loan_book(book_id, borrower)
                print("Loan recorded.")
            elif choice == "4":
                book_id = input("Book ID: ").strip()
                library.return_book(book_id)
                print("Return recorded.")
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Choose 1, 2, 3, 4, or 5.")
        except ValueError as error:
            print(f"Unable to complete that action: {error}")


if __name__ == "__main__":
    main()
