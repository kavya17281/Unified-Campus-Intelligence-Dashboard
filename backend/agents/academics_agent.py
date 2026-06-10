from backend.agents.base_agent import BaseAgent
from backend.tools.academics_tool import ACADEMICS_TOOLS
from backend.tools.tool_routes import ACADEMIC_TOOL_ROUTES


ACADEMIC_PROMPT = """
You are a university academic assistant.

Rules:
- Use tools ONLY for factual academic information (courses, faculty, schedules, credits).
- Never hallucinate course details, professors, or schedules.
- If tool returns empty data, respond with "information not found in academic system".
- Prioritize accuracy over completeness.
- Keep explanations clear and minimal unless user asks for depth.
"""


academic_agent = BaseAgent(
    system_prompt=ACADEMIC_PROMPT,
    tools=ACADEMICS_TOOLS,
    tool_routes=ACADEMIC_TOOL_ROUTES
)


def chat_academic(message: str):
    return academic_agent.chat(message)
