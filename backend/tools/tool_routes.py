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


EVENTS_TOOL_ROUTES = {

    "search_events": f"{EVENTS_BASE}/search",
    "club_events": f"{EVENTS_BASE}/club-events",

    "upcoming": f"{EVENTS_BASE}/upcoming",
    "featured": f"{EVENTS_BASE}/featured",
    "next_refreshments": f"{EVENTS_BASE}/next-refreshments",

    "event_info": f"{EVENTS_BASE}/event",
    "venue": f"{EVENTS_BASE}/venue",
    "refreshments": f"{EVENTS_BASE}/refreshments",
    "registration": f"{EVENTS_BASE}/registration",
    "tags": f"{EVENTS_BASE}/tags",

    "stats": f"{EVENTS_BASE}/stats"
}


CAFETERIA_TOOL_ROUTES = {

    "search_items": f"{CAFETERIA_BASE}/search",
    "category_items": f"{CAFETERIA_BASE}/category",

    "veg_items": f"{CAFETERIA_BASE}/veg",
    "non_veg_items": f"{CAFETERIA_BASE}/non-veg",

    "available_items": f"{CAFETERIA_BASE}/available",
    "under_price": f"{CAFETERIA_BASE}/under-price",

    "item_info": f"{CAFETERIA_BASE}/item",
    "price": f"{CAFETERIA_BASE}/price",
    "availability": f"{CAFETERIA_BASE}/availability",

    "stats": f"{CAFETERIA_BASE}/stats"
}


ACADEMIC_TOOL_ROUTES = {

    "today": f"{ACADEMIC_BASE}/today",
    "tomorrow": f"{ACADEMIC_BASE}/tomorrow",
    "day": f"{ACADEMIC_BASE}/day",

    "subject_schedule": f"{ACADEMIC_BASE}/subject",

    "exams": f"{ACADEMIC_BASE}/exams",
    "next_exam": f"{ACADEMIC_BASE}/next-exam",
    "next_exam_subject": f"{ACADEMIC_BASE}/next-exam-subject",

    "stats": f"{ACADEMIC_BASE}/stats"
}