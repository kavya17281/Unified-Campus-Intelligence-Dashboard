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




#print(chat_library("Who wrote Data Structures and Algorithms?"))
#print(chat_library("Is Clean Code available in the library?"))

# # -----------------------------
# # Search / Discovery
# # -----------------------------
# print(chat_library("Find books about algorithms"))
# print(chat_library("Search books related to machine learning"))
# print(chat_library("Show me books on Python programming"))

# -----------------------------
# Category / Tag filtering
# -----------------------------
print(chat_library("Give me books in the computer science category"))
print(chat_library("Show books tagged with AI"))
print(chat_library("Any books tagged with backend or fastapi?"))

# -----------------------------
# Author-based queries
# -----------------------------
print(chat_library("Books written by Robert C. Martin"))
print(chat_library("What books has Andrew Ng written?"))

# -----------------------------
# Availability + details
# -----------------------------
print(chat_library("Is Clean Code available?"))
print(chat_library("Do you have Introduction to Algorithms?"))
print(chat_library("Give full details of Clean Code"))
print(chat_library("What is the summary of Clean Code?"))

# -----------------------------
# Metadata queries
# -----------------------------
print(chat_library("What category does Clean Code belong to?"))
print(chat_library("Show tags of Clean Code"))
print(chat_library("Where is Clean Code located in the library?"))

# -----------------------------
# Stats / system-level
# -----------------------------
print(chat_library("How many books are in the library?"))
print(chat_library("Give me library statistics"))
print(chat_library("How many books are currently available?"))

# -----------------------------
# Edge / robustness cases
# -----------------------------
print(chat_library("Suggest something good to read"))
print(chat_library("I want a book about quantum teleportation"))
print(chat_library("hello"))
print(chat_library("random gibberish query asdfghjkl"))