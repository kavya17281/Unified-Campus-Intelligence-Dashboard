import requests
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pydantic import BaseModel
from backend.router.groq_router import groq_router

from backend.agents.library_agent import chat_library
from backend.agents.events_agent import chat_events
from backend.agents.cafeteria_agent import chat_cafeteria
from backend.agents.academics_agent import chat_academic
from backend.agents.general_agent import chat_general


app = FastAPI()

app.mount(
    "/assets",
    StaticFiles(directory="frontend/dist/assets"),
    name="assets"
)


@app.get("/")
def home():
    return FileResponse("frontend/dist/index.html")


@app.get("/dashboard-data")
def dashboard_data():

    library = requests.get("http://127.0.0.1:8001/all").json()
    events = requests.get("http://127.0.0.1:8002/all").json()
    cafeteria = requests.get("http://127.0.0.1:8003/all").json()
    academics = requests.get("http://127.0.0.1:8004/all").json()

    return {
        "library": library,
        "events": events,
        "cafeteria": cafeteria,
        "academics": academics
    }


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    response = handle_message(request.message)

    return {"response": response}


@app.get("/{full_path:path}")
def spa_fallback(full_path: str):
    return FileResponse("frontend/dist/index.html")



def handle_message(message: str):
    route = groq_router(message)
    agent = route["agent"]

    if agent == "library":
        return chat_library(message)

    if agent == "event":
        return chat_events(message)

    if agent == "cafeteria":
        return chat_cafeteria(message)

    if agent == "academic":
        return chat_academic(message)

    if agent == "general":
        return chat_general(message)

    return chat_general(message)