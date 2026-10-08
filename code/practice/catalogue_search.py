"""Practice example: case-insensitive searches over catalogue records."""

from typing import TypedDict


class CatalogueEntry(TypedDict):
    title: str
    author: str


def search_catalogue(entries: list[CatalogueEntry], query: str) -> list[CatalogueEntry]:
    """Return records whose title contains a non-empty search phrase."""
    normalized_query = query.strip().casefold()
    if not normalized_query:
        return []

    # A comprehension keeps the filter readable; casefold supports
    # caseless matching more fully than simply lowercasing both strings.
    return [
        entry
        for entry in entries
        if normalized_query in entry['title'].casefold()
    ]


def main() -> None:
    catalogue: list[CatalogueEntry] = [
        {'title': 'The Hobbit', 'author': 'J. R. R. Tolkien'},
        {'title': 'Kindred', 'author': 'Octavia E. Butler'},
        {'title': 'The Left Hand of Darkness', 'author': 'Ursula K. Le Guin'},
    ]

    for result in search_catalogue(catalogue, "the"):
        print(f"{result['title']} — {result['author']}")


if __name__ == "__main__":
    main()
