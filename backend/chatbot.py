import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Model path
MODEL_NAME = "facebook/blenderbot-400M-distill"
MODEL_PATH = "model/model.pth"

class Chatbot:
    def __init__(self):
        """Initialize chatbot with pre-trained model and tokenizer."""
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

        # Load fine-tuned model if available
        try:
            self.model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
            print("✅ Loaded fine-tuned chatbot model.")
        except FileNotFoundError:
            print("⚠️ No fine-tuned model found. Using pre-trained model.")

    def get_response(self, user_input):
        """Generate response for user input."""
        inputs = self.tokenizer(user_input, return_tensors="pt")
        output = self.model.generate(**inputs)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

# Create chatbot instance
chatbot = Chatbot()

# Function to generate responses
def generate_chat_response(user_input):
    return chatbot.get_response(user_input)
