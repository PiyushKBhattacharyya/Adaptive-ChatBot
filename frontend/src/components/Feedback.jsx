import { sendFeedback } from "../api/chatbotApi";

export default function Feedback({ messageId }) {
  const handleFeedback = (rating) => {
    sendFeedback(messageId, rating, "");
  };

  return (
    <div className="flex gap-2 mt-2">
      <button className="text-green-500" onClick={() => handleFeedback(5)}>👍</button>
      <button className="text-red-500" onClick={() => handleFeedback(1)}>👎</button>
    </div>
  );
}
