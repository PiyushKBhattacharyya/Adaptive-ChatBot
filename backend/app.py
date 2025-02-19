from fastapi import FastAPI, HTTPException, Depends
from chatbot import get_chat_response
from database import save_chat, get_chat_history
from feedback import save_feedback
from pydantic import BaseModel

app = FastAPI(title="AI Chatbot API")

# Request models
class ChatRequest(BaseModel):
    user_input: str

class FeedbackRequest(BaseModel):
    message_id: int
    rating: int  # 1 to 5
    comment: str = ""

@app.post("/chat/")
async def chat(request: ChatRequest):
    response = get_chat_response(request.user_input)
    save_chat(request.user_input, response)
    return {"response": response}

@app.post("/feedback/")
async def feedback(request: FeedbackRequest):
    save_feedback(request.message_id, request.rating, request.comment)
    return {"message": "Feedback recorded successfully"}

@app.get("/history/")
async def history():
    return get_chat_history()
