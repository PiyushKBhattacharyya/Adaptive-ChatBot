from fastapi import FastAPI, HTTPException
from chatbot import generate_chat_response
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
    """Handles chat requests and saves conversation history."""
    try:
        response = generate_chat_response(request.user_input)
        save_chat(request.user_input, response)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/feedback/")
async def feedback(request: FeedbackRequest):
    """Handles user feedback and stores it for model improvement."""
    try:
        save_feedback(request.message_id, request.rating, request.comment)
        return {"message": "Feedback recorded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history/")
async def history():
    """Retrieves chat history."""
    try:
        return get_chat_history()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
