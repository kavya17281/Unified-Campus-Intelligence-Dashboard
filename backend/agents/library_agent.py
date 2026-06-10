from base_agent import BaseAgent
from tools.library_tools import LIBRARY_TOOLS
from tools.tool_routes import LIB_TOOL_ROUTES



LIBRARY_PROMPT = """
You are a university library assistant.

Rules:
- Use tools ONLY when required for factual retrieval.
- Never hallucinate books, authors, or availability.
- If tool returns empty data, respond with "not found in library".
- Keep responses concise and useful.
"""



library_agent = BaseAgent(
    system_prompt=LIBRARY_PROMPT,
    tools=LIBRARY_TOOLS,
    tool_routes=LIB_TOOL_ROUTES
)



def chat_library(message: str):
    return library_agent.chat(message)


