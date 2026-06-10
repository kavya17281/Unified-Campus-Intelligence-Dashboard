LIBRARY_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "search_books",
            "description": "Search books by title or topic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "tag_books",
            "description": "Find books matching a tag.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tag": {"type": "string"}
                },
                "required": ["tag"]
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
            "name": "category_books",
            "description": "Find books belonging to a category.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Examples: Computer Science, Mathematics, Electronics, Literature"
                    }
                },
                "required": ["category"]
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