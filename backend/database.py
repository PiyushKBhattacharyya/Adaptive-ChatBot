import sqlite3

DB_FILE = "chatbot.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_chat(user_input: str, bot_response: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (user_input, bot_response) VALUES (?, ?)", (user_input, bot_response))
    conn.commit()
    conn.close()

def get_chat_history():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat_history")
    history = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "user_input": row[1], "bot_response": row[2]} for row in history]

# Initialize DB on startup
init_db()
