LIBRARY_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "discover_books",
            "description": "Search books using title, description, tags, or category matching.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search keyword for book title, description, tags, or category."
                    }
                },
                "required": ["query"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "author_books",
            "description": "Find all books written by an author.",
            "parameters": {
                "type": "object",
                "properties": {
                    "author": {"type": "string"}
                },
                "required": ["author"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "latest_books",
            "description": "Get recently added books.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "popular_books",
            "description": "Get most popular books.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "book_info",
            "description": "Get complete information about a book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "availability",
            "description": "Check availability of a book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "shelf_location",
            "description": "Get shelf location of a book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "author",
            "description": "Get author of a book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "category_of_book",
            "description": "Get category of a book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "summary",
            "description": "Get summary of a book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "tags",
            "description": "Get tags associated with a book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "library_stats",
            "description": "Get overall library statistics.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]