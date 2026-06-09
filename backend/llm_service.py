from openai import OpenAI
from dotenv import load_dotenv
from mcp.library_service import *

import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

TOOLS = {
    "get_author": get_author,
    "get_availability": get_availability,
    "get_summary": get_summary,
    "get_category": get_category,
    "get_tags": get_tags,
    "search_books": search_books
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_author",
            "description": "Get the author of a book by title",
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
            "name": "get_availability",
            "description": "Check whether a book is available and how many copies exist",
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
            "name": "get_summary",
            "description": "Get a summary of a book",
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
            "name": "get_category",
            "description": "Return the subject category of a book",
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
            "name": "get_tags",
            "description": "Get tags associated with a book",
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
            "name": "search_books",
            "description": "Search books by title or topic",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            }
        }
    }
]


def chat_with_groq(message):

    messages = [
        {
            "role": "system",
            "content":
            """
            You are a university library assistant.

            When tool results are available:
            - Use only the information returned by the tools.
            - Do not invent books.
            - Do not recommend books outside the library database.
            - If the tool returns no results, say so.
            """
        },
        {
            "role": "user",
            "content": message
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message

    if not assistant_message.tool_calls:
        return assistant_message.content

    tool_call = assistant_message.tool_calls[0]

    tool_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    result = TOOLS[tool_name](**arguments)

    messages.append(assistant_message)

    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result)
    })

    final_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    return final_response.choices[0].message.content


print(
    chat_with_groq("hello! how are you")
)

print(
    chat_with_groq("Give me books related to algorithms")
)

print(
    chat_with_groq("Who wrote Data Structures and Algorithms?")
)
