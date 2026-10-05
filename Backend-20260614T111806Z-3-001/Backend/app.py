from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import (
    ChatRequest,
    ChatResponse
)

from agent import build_agent

from langchain_core.chat_history import InMemoryChatMessageHistory


# --------------------------------------------------
# Chat History
# --------------------------------------------------

chat_history = InMemoryChatMessageHistory()


# --------------------------------------------------
# Global Agent
# --------------------------------------------------

agent_executor = None


# --------------------------------------------------
# Application Lifespan
# --------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    global agent_executor

    print("Loading Agent...")

    agent_executor = build_agent()

    print("Agent Ready!")

    yield

    print("Application Shutdown")


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="University Admission Assistant",
    lifespan=lifespan
)


# --------------------------------------------------
# CORS Configuration
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/")
def health_check():

    return {
        "status": "running"
    }


# --------------------------------------------------
# Chat API
# --------------------------------------------------

@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    response = agent_executor.invoke(
        {
            "input": request.question,
            "chat_history": chat_history.messages
        }
    )

    print("FULL RESPONSE:", response)

    chat_history.add_user_message(
        request.question
    )

    chat_history.add_ai_message(
        response["output"]
    )

    return ChatResponse(
        answer=response["output"]
    )


# --------------------------------------------------
# Run using:
# uvicorn app:app --reload
# --------------------------------------------------