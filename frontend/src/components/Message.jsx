export default function Message({ text, sender }) {
    return (
      <div className={`p-2 my-1 max-w-sm ${sender === "user" ? "bg-blue-200 self-end" : "bg-gray-200 self-start"} rounded-lg`}>
        {text}
      </div>
    );
  }
  