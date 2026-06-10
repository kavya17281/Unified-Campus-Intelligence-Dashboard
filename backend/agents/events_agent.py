from backend.agents.base_agent import BaseAgent
from backend.tools.events_tool import EVENTS_TOOLS
from backend.tools.tool_routes import EVENTS_TOOL_ROUTES


EVENTS_PROMPT = """
You are a university events assistant.

Rules:
- Use tools ONLY when required for factual retrieval about events.
- Never invent events, dates, venues, or registrations.
- If tool returns empty data, respond with "no matching events found".
- Treat all events as official university information.
- Keep responses concise and structured.
"""


events_agent = BaseAgent(
    system_prompt=EVENTS_PROMPT,
    tools=EVENTS_TOOLS,
    tool_routes=EVENTS_TOOL_ROUTES
)


def chat_events(message: str):
    return events_agent.chat(message)
