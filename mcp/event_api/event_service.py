from pathlib import Path
import json
from datetime import datetime

FILE_NAME = Path(__file__).parent / "events.json"


# -----------------------------
# DATA LOADING
# -----------------------------

def load_events():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def basic_event_info(event):
    return {
        "id": event["id"],
        "title": event["title"],
        "club": event["club"],
        "date": event["date"]
    }


def find_event(title: str):
    events = load_events()

    for event in events:
        if event["title"].lower() == title.lower():
            return event

    return None


def is_valid_event(event):
    return not event.get("is_cancelled", False)


def event_datetime(event):
    return datetime.strptime(
        f"{event['date']} {event['start_time']}",
        "%Y-%m-%d %H:%M"
    )

# -----------------------------
# DISCOVERY FUNCTIONS
# -----------------------------

def discover_events(query: str):
    events = load_events()
    matches = []
    query = query.lower()

    for event in events:
        if not is_valid_event(event):
            continue

        title_match = query in event["title"].lower()
        desc_match = query in event["description"].lower()

        tag_match = any(query in tag.lower() for tag in event["tags"])

        category_match = query == event["category"].lower()

        if title_match or desc_match or tag_match or category_match:
            matches.append(basic_event_info(event))

    return matches


def get_events_by_club(club: str):
    events = load_events()
    matches = []
    club = club.lower()

    for event in events:
        if not is_valid_event(event):
            continue

        if event["club"].lower() == club:
            matches.append(basic_event_info(event))

    return matches


def get_upcoming_events():
    events = load_events()

    valid_events = [
        event for event in events
        if is_valid_event(event)
    ]

    valid_events.sort(key=event_datetime)

    return [
        basic_event_info(event)
        for event in valid_events
    ]


def get_featured_events():
    events = load_events()
    matches = []

    for event in events:
        if is_valid_event(event) and event.get("featured", False):
            matches.append(basic_event_info(event))

    return matches


def get_next_event_with_refreshments():
    events = get_upcoming_events()

    for event in events:
        full_event = find_event(event["title"])
        if full_event and full_event.get("refreshments"):
            return {
                "id": full_event["id"],
                "title": full_event["title"],
                "club": full_event["club"],
                "date": full_event["date"],
                "refreshments": full_event["refreshments"]
            }

    return None


# -----------------------------
# DETAIL FUNCTIONS
# -----------------------------

def get_event_by_title(title: str):
    event = find_event(title)

    if not event:
        return None

    return event


def get_venue(title: str):
    event = find_event(title)

    if not event:
        return None

    return {
        "venue": event["venue"]
    }


def get_refreshments(title: str):
    event = find_event(title)

    if not event:
        return None

    return {
        "refreshments": event.get("refreshments")
    }


def get_registration_info(title: str):
    event = find_event(title)

    if not event:
        return None

    return {
        "registration_required": event.get("registration_required"),
        "registration_link": event.get("registration_link")
    }


def get_tags(title: str):
    event = find_event(title)

    if not event:
        return None

    return {
        "tags": event["tags"]
    }


# -----------------------------
# STATISTICS
# -----------------------------

def get_events_stats():
    events = load_events()

    valid_events = [
        e for e in events
        if is_valid_event(e)
    ]

    category_set = set()
    club_set = set()
    featured_count = 0

    for event in valid_events:
        category_set.add(event["category"])
        club_set.add(event["club"])

        if event.get("featured", False):
            featured_count += 1

    return {
        "total_events": len(valid_events),
        "featured_events": featured_count,
        "total_categories": len(category_set),
        "total_clubs": len(club_set)
    }