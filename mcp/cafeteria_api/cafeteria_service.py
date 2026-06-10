from pathlib import Path
import json

FILE_NAME = Path(__file__).parent / "menu.json"


# -----------------------------
# DATA LOADING
# -----------------------------

def load_items():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def basic_item_info(item):
    return {
        "id": item["id"],
        "name": item["name"],
        "price": item["price"],
        "category": item["category"]
    }


def find_item(name: str):
    items = load_items()

    for item in items:
        if item["name"].lower() == name.lower():
            return item

    return None


# -----------------------------
# DISCOVERY FUNCTIONS
# -----------------------------

def search_items(query: str):
    items = load_items()
    matches = []
    query = query.lower()

    for item in items:
        title_match = query in item["name"].lower()
        tag_match = any(query in tag.lower() for tag in item["tags"])

        if title_match or tag_match:
            matches.append(basic_item_info(item))

    return matches


def get_items_by_category(category: str):
    items = load_items()
    matches = []
    category = category.lower()

    for item in items:
        if item["category"].lower() == category:
            matches.append(basic_item_info(item))

    return matches


def get_veg_items(is_veg: bool = True):
    items = load_items()

    return [
        basic_item_info(item)
        for item in items
        if item.get("is_veg") == is_veg
    ]


def get_available_items():
    items = load_items()

    return [
        basic_item_info(item)
        for item in items
        if item.get("available", True)
    ]


def get_under_price(max_price: int):
    items = load_items()

    return [
        basic_item_info(item)
        for item in items
        if item["price"] <= max_price
    ]


# -----------------------------
# DETAIL FUNCTIONS
# -----------------------------

def get_item_by_name(name: str):
    item = find_item(name)

    if not item:
        return None

    return item


def get_price(name: str):
    item = find_item(name)

    if not item:
        return None

    return {
        "price": item["price"]
    }


def get_item_tags(name: str):
    item = find_item(name)

    if not item:
        return None

    return {
        "tags": item["tags"]
    }


def get_availability(name: str):
    item = find_item(name)

    if not item:
        return None

    return {
        "available": item["available"]
    }


# -----------------------------
# STATS
# -----------------------------

def get_cafeteria_stats():
    items = load_items()

    return {
        "total_items": len(items),
        "veg_items": sum(1 for i in items if i.get("is_veg")),
        "non_veg_items": sum(1 for i in items if not i.get("is_veg")),
        "available_items": sum(1 for i in items if i.get("available", True))
    }