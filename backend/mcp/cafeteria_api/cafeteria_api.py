from fastapi import FastAPI
from cafeteria_service import *

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Cafeteria MCP Running"
    }


# -----------------------------
# Discovery Endpoints
# -----------------------------

@app.get("/search")
def search(query: str):
    return search_items(query)


@app.get("/category")
def category(category: str):
    return get_items_by_category(category)


@app.get("/veg")
def veg():
    return get_veg_items(True)


@app.get("/non-veg")
def non_veg():
    return get_veg_items(False)


@app.get("/available")
def available():
    return get_available_items()


@app.get("/under-price")
def under_price(max_price: int):
    return get_under_price(max_price)


# -----------------------------
# Detail Endpoints
# -----------------------------

@app.get("/item")
def item(name: str):
    return get_item_by_name(name)


@app.get("/price")
def price(name: str):
    return get_price(name)


@app.get("/tags")
def tags(name: str):
    return get_item_tags(name)


@app.get("/availability")
def availability(name: str):
    return get_availability(name)


# -----------------------------
# Stats
# -----------------------------

@app.get("/stats")
def stats():
    return get_cafeteria_stats()