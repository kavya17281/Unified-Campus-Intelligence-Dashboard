from fastapi import FastAPI


# start code
# cd backend
# uvicorn main:app --reload


app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Main Server Running"
    }


# ----------------------------

from pydantic import BaseModel
from llm_service import chat_with_groq

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):

    response = chat_with_groq(request.message)

    return {"response": response}

# ----------------------------



from router.groq_router import groq_router

# from agents.library_agent import chat_library
# from agents.event_agent import chat_event
# from agents.cafeteria_agent import chat_cafeteria
# from agents.academic_agent import chat_academic
from agents.general_agent import chat_general


def handle_message(message: str):

    route = groq_router(message)
    agent = route["agent"]

    # if agent == "library":
    #     return chat_library(message)

    # if agent == "event":
    #     return chat_event(message)

    # if agent == "cafeteria":
    #     return chat_cafeteria(message)

    # if agent == "academic":
    #     return chat_academic(message)

    if agent == "general":
        return chat_general(message)

    return chat_general(message)