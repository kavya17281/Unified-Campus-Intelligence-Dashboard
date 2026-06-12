import json

from backend.shared.groq_client import client
from backend.router.router_prompt import ROUTER_SYSTEM_PROMPT
from backend.router.fallback_router import fallback_router


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
