import axios from "axios";

const API_URL = "http://localhost:8000"; // Change if deployed

export const sendMessage = async (message) => {
  try {
    const response = await axios.post(`${API_URL}/chat/`, { user_input: message });
    return response.data.response;
  } catch (error) {
    console.error("Error fetching chatbot response:", error);
    return "Sorry, I couldn't process that.";
  }
};

export const sendFeedback = async (messageId, rating, comment) => {
  try {
    await axios.post(`${API_URL}/feedback/`, { message_id: messageId, rating, comment });
  } catch (error) {
    console.error("Error sending feedback:", error);
  }
};
