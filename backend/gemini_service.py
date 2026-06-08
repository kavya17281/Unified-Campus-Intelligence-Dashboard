import google.generativeai as genai
from library_tools import TOOLS
import json
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def chat_with_gemini(message):

    prompt = f"""
        You are an assistant.

        Available tools:

        1. get_availability(title)
        2. get_author(title)
        3. get_summary(title)

        User query:

        {message}

        Respond ONLY with valid JSON.

        Do not use markdown.
        Do not use ```json.
        Do not add explanations.

        Example:

        {{"tool":"get_availability","title":"Machine Learning"}}
    """

    response = model.generate_content(prompt)
    raw = response.text.strip()

    print("Gemini Router Output:")
    print(raw)

    if raw.startswith("```"):
        raw = raw.replace("```json", "")
        raw = raw.replace("```", "")
        raw = raw.strip()

    tool_call = json.loads(raw)
    tool_name = tool_call["tool"]
    title = tool_call["title"]

    result = TOOLS[tool_name](title)

    prompt = f"""
    User asked:
    {message}

    Tool result:
    {result}

    Answer naturally.
    """
    response = model.generate_content(prompt)

    return response.text

