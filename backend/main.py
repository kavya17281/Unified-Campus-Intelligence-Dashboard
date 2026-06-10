import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from router.groq_router import groq_router

# from agents.library_agent import chat_library
# from agents.event_agent import chat_event
# from agents.cafeteria_agent import chat_cafeteria
# from agents.academic_agent import chat_academic
from agents.general_agent import chat_general


app = FastAPI()


@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/dashboard-data")
def dashboard_data():

    library = requests.get("http://127.0.0.1:8001/all").json()
    events = requests.get("http://127.0.0.1:8002/all").json()

    return {
        "library": library,
        "events": events
    }


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    response = handle_message(request.message)

    return {"response": response}


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