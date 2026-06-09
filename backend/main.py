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

