EVENTS_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "search_events",
            "description": "Search events by title, description, or tags.",
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
            "name": "club_events",
            "description": "Get events by club.",
            "parameters": {
                "type": "object",
                "properties": {
                    "club": {"type": "string"}
                },
                "required": ["club"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "upcoming",
            "description": "Get upcoming events.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "featured",
            "description": "Get featured events.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "next_refreshments",
            "description": "Get next event with refreshments.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "event_info",
            "description": "Get full details of an event.",
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
            "name": "venue",
            "description": "Look up the room or location where a session is being held. Use this for any question about where a talk takes place, which room it is in, or its location. ",
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
            "name": "refreshments_given",
            "description": "Get refreshments info for an event.",
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
            "name": "registration",
            "description": "Get registration details for an event.",
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
            "description": "Get tags associated with an event.",
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
            "name": "stats",
            "description": "Get overall event statistics.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]