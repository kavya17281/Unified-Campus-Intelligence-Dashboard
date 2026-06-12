from backend.shared.groq_client import client
import json
import requests

ANSWER_PROMPT = """
You have already received tool results.

Use only the information available in the conversation.

Answer naturally.

Do not call tools.

If the tool returned an error, explain that the information could not be retrieved.
"""

class BaseAgent:

    def __init__(self, system_prompt, tools, tool_routes):
        self.system_prompt = system_prompt
        self.tools = tools
        self.tool_routes = tool_routes


    def run_tool_llm(self, messages):
        return client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=self.tools,
            tool_choice="auto",
            temperature=0
        )


    def run_answer_llm(self, messages):
        return client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0
        )


    def execute_tool(self, tool_call):
        name = tool_call.function.name
        try:
            args = json.loads(tool_call.function.arguments)
        except Exception:
            return {"error": "invalid tool arguments"}

        if name not in self.tool_routes:
            return {"error": "tool not found"}

        url = self.tool_routes[name]

        try:
            response = requests.get(url, params=args, timeout=5)
            return response.json()

        except Exception as e:
            return {"error": str(e)}


    def chat(self, message: str):
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": message
            }
        ]


        # Step 1: Tool selection
        response = self.run_tool_llm(messages)
        #print(response)
        assistant_message = response.choices[0].message

        if not assistant_message.tool_calls:
            return assistant_message.content


        # Step 2: Execute tool
        tool_call = assistant_message.tool_calls[0]
        tool_result = self.execute_tool(tool_call)


        # Step 3: Build answer prompt
        answer_messages = [
            {
                "role": "system",
                "content": ANSWER_PROMPT
            }
        ]

        answer_messages.extend(messages)
        answer_messages.append(assistant_message)

        answer_messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(tool_result)
            }
        )

        # Step 4: Final natural-language answer
        final_response = self.run_answer_llm(answer_messages)
        #print(final_response)

        return final_response.choices[0].message.content