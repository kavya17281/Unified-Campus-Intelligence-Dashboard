from pathlib import Path
import json

FILE_NAME = Path(__file__).parent / "books.json"


def load_books():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def basic_book_info(book):
    return {
        "id": book["id"],
        "title": book["title"]
    }


def find_book(title:str):
    books = load_books()

    for book in books:
        if book["title"].lower() == title.lower():
            return book

    return None


# -----------------------------
# Discovery Functions
# -----------------------------

def search_books(query:str):
    books = load_books()
    matches = []
    query = query.lower()

    for book in books:
        title_match = (query in book["title"].lower())
        tag_match = any(query in tag.lower() for tag in book["tags"])

        if title_match or tag_match:
            matches.append(basic_book_info(book))

    return matches


def get_books_by_tag(tag:str):
    books = load_books()
    matches = []
    tag = tag.lower()

    for book in books:
        for book_tag in book["tags"]:
            if tag in book_tag.lower():
                matches.append(basic_book_info(book))
                break

    return matches


def get_books_by_author(author:str):
    books = load_books()
    matches = []

    for book in books:
        if book["author"].lower() == author.lower():
            matches.append(basic_book_info(book))

    return matches


def get_books_by_category(category:str):
    books = load_books()
    matches = []

    for book in books:
        if book["category"].lower() == category.lower():
            matches.append(basic_book_info(book))

    return matches


def get_latest_books(limit=5):
    books = load_books()

    books.sort(
        key=lambda book: book["added_on"],
        reverse=True
    )

    return [
        basic_book_info(book)
        for book in books[:limit]
    ]


def get_popular_books(limit=5):
    books = load_books()

    books.sort(
        key=lambda book: book["popularity"],
        reverse=True
    )

    return [
        basic_book_info(book)
        for book in books[:limit]
    ]


# -----------------------------
# Detail Functions
# -----------------------------

def get_book_by_title(title:str):
    book = find_book(title)

    if not book:
        return None

    return {
        "id": book["id"],
        "title": book["title"],
        "author": book["author"],
        "category": book["category"],
        "summary": book["summary"],
        "tags": book["tags"]
    }


def get_availability(title:str):
    book = find_book(title)

    if not book:
        return None

    return {
        "available": book["available"],
        "copies": book["copies"]
    }


def get_shelf_location(title:str):
    book = find_book(title)

    if not book:
        return None

    return {
        "shelf": book["shelf"]
    }


def get_author(title:str):
    book = find_book(title)

    if not book:
        return None

    return {
        "author": book["author"]
    }


def get_category(title:str):
    book = find_book(title)

    if not book:
        return None

    return {
        "category": book["category"]
    }


def get_summary(title:str):
    book = find_book(title)

    if not book:
        return None

    return {
        "summary": book["summary"]
    }


def get_tags(title:str):
    book = find_book(title)

    if not book:
        return None

    return {
        "tags": book["tags"]
    }


# -----------------------------
# Statistics
# -----------------------------

def get_library_stats():
    books = load_books()

    return {
        "total_books": len(books),
        "available_books": sum(
            book["available"]
            for book in books
        ),
        "categories": len(
            set(
                book["category"]
                for book in books
            )
        )
    }