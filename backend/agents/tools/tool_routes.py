LIBRARY_BASE = "http://127.0.0.1:8001"
EVENTS_BASE = "http://127.0.0.1:8002"
CAFETERIA_BASE = "http://127.0.0.1:8003"
ACADEMIC_BASE = "http://127.0.0.1:8004"


LIB_TOOL_ROUTES = {

    "search_books" : f"{LIBRARY_BASE}/search",
    "tag_books" : f"{LIBRARY_BASE}/tag-books",
    "author_books" : f"{LIBRARY_BASE}/author-books",
    "category_books" : f"{LIBRARY_BASE}/category-books",
    "latest_books" : f"{LIBRARY_BASE}/latest",
    "popular_books" : f"{LIBRARY_BASE}/popular",
    "book_info" : f"{LIBRARY_BASE}/book",
    "availability" : f"{LIBRARY_BASE}/availability",
    "shelf_location" : f"{LIBRARY_BASE}/shelf",
    "author" : f"{LIBRARY_BASE}/author",
    "category_of_book" : f"{LIBRARY_BASE}/category",
    "summary" : f"{LIBRARY_BASE}/summary",
    "tags" : f"{LIBRARY_BASE}/tags",
    "library_stats" : f"{LIBRARY_BASE}/stats",

}