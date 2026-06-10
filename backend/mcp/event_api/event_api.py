from fastapi import FastAPI
from event_service import *


app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Events MCP Running"
    }


@app.get("/all")
def all_events():
    return load_events()


@app.get("/health")
def health():

    events = load_events()
    return {
        "status": "healthy",
        "count": len(events)
    }

# -----------------------------
# Discovery Endpoints
# -----------------------------

@app.get("/search")
def search(query: str):
    return search_events(query)


@app.get("/tag-events")
def tag_events(tag: str):
    return get_events_by_tag(tag)


@app.get("/club-events")
def club_events(club: str):
    return get_events_by_club(club)


@app.get("/category-events")
def category_events(category: str):
    return get_events_by_category(category)


@app.get("/upcoming")
def upcoming():
    return get_upcoming_events()


@app.get("/featured")
def featured():
    return get_featured_events()


@app.get("/next-refreshments")
def next_refreshments():
    return get_next_event_with_refreshments()


# -----------------------------
# Detail Endpoints
# -----------------------------

@app.get("/event")
def event(title: str):
    return get_event_by_title(title)


@app.get("/venue")
def venue(title: str):
    return get_venue(title)


@app.get("/refreshments")
def refreshments(title: str):
    return get_refreshments(title)


@app.get("/registration")
def registration(title: str):
    return get_registration_info(title)


@app.get("/tags")
def tags(title: str):
    return get_tags(title)


# -----------------------------
# Statistics
# -----------------------------

@app.get("/stats")
def stats():
    return get_events_stats()