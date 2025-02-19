import { useState } from "react";
import { sendMessage } from "../api/chatbotApi";
import Message from "./Message";

export default function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { text: input, sender: "user" };
    setMessages([...messages, userMessage]);
    setInput("");

    const botResponse = await sendMessage(input);
    setMessages([...messages, userMessage, { text: botResponse, sender: "bot" }]);
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-gray-100 rounded-xl shadow-md">
      <div className="h-80 overflow-y-auto p-4 border border-gray-300 rounded-lg">
        {messages.map((msg, index) => (
          <Message key={index} text={msg.text} sender={msg.sender} />
        ))}
      </div>
      <div className="mt-4 flex">
        <input
          className="flex-1 p-2 border rounded-l-lg"
          type="text"
          placeholder="Type a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleSend()}
        />
        <button className="bg-blue-500 text-white px-4 py-2 rounded-r-lg" onClick={handleSend}>
          Send
        </button>
      </div>
    </div>
  );
}
