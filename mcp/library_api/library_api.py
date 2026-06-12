from fastapi import FastAPI
from mcp.library_api.library_service import *


app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Library MCP Running"
    }


@app.get("/all")
def all_books():
    return load_books()


@app.get("/health")
def health():
    books = load_books()
    
    return {
        "status": "healthy",
        "count": len(books)
    }

# -----------------------------
# Discovery Endpoints
# -----------------------------

@app.get("/search")
def search(query: str):
    return discover_books(query)


@app.get("/author-books")
def author_books(author: str):
    return get_books_by_author(author)


@app.get("/latest")
def latest():
    return get_latest_books()


@app.get("/popular")
def popular():
    return get_popular_books()

# -----------------------------
# Detail Endpoints
# -----------------------------

@app.get("/book")
def book(title: str):
    return get_book_by_title(title)


@app.get("/availability")
def availability(title: str):
    return get_availability(title)


@app.get("/shelf")
def shelf(title: str):
    return get_shelf_location(title)


@app.get("/author")
def author(title: str):
    return get_author(title)


@app.get("/category")
def category(title: str):
    return get_category(title)


@app.get("/summary")
def summary(title: str):
    return get_summary(title)


@app.get("/tags")
def tags(title: str):
    return get_tags(title)


# -----------------------------
# Statistics
# -----------------------------

@app.get("/stats")
def stats():
    return get_library_stats()

