from backend.agents.base_agent import BaseAgent
from backend.tools.cafeteria_tool import CAFETERIA_TOOLS
from backend.tools.tool_routes import CAFETERIA_TOOL_ROUTES


CAFETERIA_PROMPT = """
You are a university cafeteria assistant.

Rules:
- Use tools ONLY when required for factual retrieval about food, menus, or availability.
- Never invent menu items, prices, or availability.
- If tool returns empty data, respond with "item not available".
- Assume all menu data must come from the cafeteria system.
- Keep responses short, practical, and student-friendly.
"""


cafeteria_agent = BaseAgent(
    system_prompt=CAFETERIA_PROMPT,
    tools=CAFETERIA_TOOLS,
    tool_routes=CAFETERIA_TOOL_ROUTES
)


def chat_cafeteria(message: str):
    return cafeteria_agent.chat(message)
