from backend.config import *


LIB_TOOL_ROUTES = {

    "discover_books" : f"{LIBRARY_API}/search",
    "author_books" : f"{LIBRARY_API}/author-books",
    "latest_books" : f"{LIBRARY_API}/latest",
    "popular_books" : f"{LIBRARY_API}/popular",
    "book_info" : f"{LIBRARY_API}/book",
    "availability_of_book" : f"{LIBRARY_API}/availability",
    "shelf_location" : f"{LIBRARY_API}/shelf",
    "author_who" : f"{LIBRARY_API}/author",
    "category_of_book" : f"{LIBRARY_API}/category",
    "summary" : f"{LIBRARY_API}/summary",
    "tags" : f"{LIBRARY_API}/tags",
    "library_stats" : f"{LIBRARY_API}/stats",

}


EVENTS_TOOL_ROUTES = {

    "search_events": f"{EVENTS_API}/search",
    "club_events": f"{EVENTS_API}/club-events",

    "upcoming": f"{EVENTS_API}/upcoming",
    "featured": f"{EVENTS_API}/featured",
    "next_refreshments": f"{EVENTS_API}/next-refreshments",

    "event_info": f"{EVENTS_API}/event",
    "venue": f"{EVENTS_API}/venue",
    "refreshments_given": f"{EVENTS_API}/refreshments",
    "registration": f"{EVENTS_API}/registration",
    "tags": f"{EVENTS_API}/tags",

    "stats": f"{EVENTS_API}/stats"
}


CAFETERIA_TOOL_ROUTES = {

    "search_food": f"{CAFETERIA_API}/search",
    "category_items": f"{CAFETERIA_API}/category",

    "veg_items": f"{CAFETERIA_API}/veg",
    "non_veg_items": f"{CAFETERIA_API}/non-veg",

    "available_items": f"{CAFETERIA_API}/available",
    "under_price": f"{CAFETERIA_API}/under-price",

    "item_info": f"{CAFETERIA_API}/item",
    "price": f"{CAFETERIA_API}/price",
    "availability": f"{CAFETERIA_API}/availability",

    "stats": f"{CAFETERIA_API}/stats"
}


ACADEMIC_TOOL_ROUTES = {

    "today": f"{ACADEMICS_API}/today",
    "tomorrow": f"{ACADEMICS_API}/tomorrow",
    "day": f"{ACADEMICS_API}/day",

    "subject_schedule": f"{ACADEMICS_API}/subject",

    "exams": f"{ACADEMICS_API}/exams",
    "next_exam": f"{ACADEMICS_API}/next-exam",
    "next_exam_subject": f"{ACADEMICS_API}/next-exam-subject",

    "stats": f"{ACADEMICS_API}/stats"
}