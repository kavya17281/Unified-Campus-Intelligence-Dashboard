ACADEMICS_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "today",
            "description": "Get today's class schedule.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "tomorrow",
            "description": "Get tomorrow's class schedule.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "day",
            "description": "Get class schedule for a specific day.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {"type": "string"}
                },
                "required": ["day"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "subject_schedule",
            "description": "Get schedule for a specific subject.",
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {"type": "string"}
                },
                "required": ["subject"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "exams",
            "description": "Get full exam schedule.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "next_exam",
            "description": "Get next upcoming exam.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "next_exam_subject",
            "description": "Get next exam for a specific subject.",
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {"type": "string"}
                },
                "required": ["subject"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "stats",
            "description": "Get academic statistics.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]