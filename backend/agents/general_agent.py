from backend.shared.groq_client import client


def chat_general(message: str):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                    You are a helpful university assistant chatbot.

                    You do NOT use tools.

                    You can:
                    - greet users
                    - answer general conversational questions
                    - be polite and conversational

                    Keep responses short and natural.
                    """
            },
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content