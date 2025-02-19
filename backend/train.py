import os
import json
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "facebook/blenderbot-400M-distill"
MODEL_PATH = "model/model.pth"
FEEDBACK_PATH = "model/feedback_data/"

class ChatbotTrainer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

        if os.path.exists(MODEL_PATH):
            self.model.load_state_dict(torch.load(MODEL_PATH))
            print("Loaded existing model weights.")

    def load_feedback_data(self):
        """Load user feedback data for training."""
        training_data = []
        for file in os.listdir(FEEDBACK_PATH):
            if file.endswith(".json"):
                with open(os.path.join(FEEDBACK_PATH, file), "r") as f:
                    data = json.load(f)
                    training_data.append(data)
        return training_data

    def fine_tune(self):
        """Fine-tune the chatbot on feedback data."""
        training_data = self.load_feedback_data()
        if not training_data:
            print("No new feedback data found.")
            return

        optimizer = torch.optim.AdamW(self.model.parameters(), lr=5e-5)

        for entry in training_data:
            user_input = entry["user_input"]
            correct_response = entry["correct_response"]

            inputs = self.tokenizer(user_input, return_tensors="pt", truncation=True)
            labels = self.tokenizer(correct_response, return_tensors="pt").input_ids

            outputs = self.model(**inputs, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()

        # Save the updated model
        torch.save(self.model.state_dict(), MODEL_PATH)
        print("Chatbot model updated with feedback.")

if __name__ == "__main__":
    trainer = ChatbotTrainer()
    trainer.fine_tune()