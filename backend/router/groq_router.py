import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shared.groq_client import client
from router_prompt import ROUTER_SYSTEM_PROMPT
from fallback_router import fallback_router


def groq_router(message: str):

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": ROUTER_SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0
        )

        content = response.choices[0].message.content

        # Try parsing JSON safely
        try:
            result = json.loads(content)

            if "agent" in result:
                return result
            else:
                return fallback_router(message)

        except json.JSONDecodeError:
            # If model returns invalid JSON → fallback
            return fallback_router(message)

    except Exception:
        # If Groq fails completely → fallback
        return fallback_router(message)
    
print(
    groq_router(
        "hello groqhow are you"
    )
)