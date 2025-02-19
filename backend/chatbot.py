import random

def get_chat_response(user_input: str) -> str:
    responses = [
        "Hello! How can I assist you?",
        "I'm here to help! Ask me anything.",
        "That's interesting! Tell me more.",
        "Could you clarify your question?",
        "I'm learning from our conversations!"
    ]
    return random.choice(responses)
