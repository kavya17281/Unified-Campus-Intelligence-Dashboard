CAFETERIA_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "search_items",
            "description": "Search cafeteria items by name or keyword.",
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
            "name": "category_items",
            "description": "Get items by category.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"}
                },
                "required": ["category"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "veg_items",
            "description": "Get vegetarian cafeteria items.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "non_veg_items",
            "description": "Get non-vegetarian cafeteria items.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "available_items",
            "description": "Get all currently available cafeteria items.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "under_price",
            "description": "Get cafeteria items under a given price.",
            "parameters": {
                "type": "object",
                "properties": {
                    "max_price": {"type": "integer"}
                },
                "required": ["max_price"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "item_info",
            "description": "Get full details of a cafeteria item.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "price",
            "description": "Get price of a cafeteria item.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "availability",
            "description": "Check availability of a cafeteria item.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "stats",
            "description": "Get cafeteria statistics.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]