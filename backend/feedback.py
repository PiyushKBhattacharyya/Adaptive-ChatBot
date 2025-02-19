import sqlite3

DB_FILE = "chatbot.db"

def init_feedback_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message_id INTEGER,
            rating INTEGER,
            comment TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_feedback(message_id: int, rating: int, comment: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (message_id, rating, comment) VALUES (?, ?, ?)", (message_id, rating, comment))
    conn.commit()
    conn.close()

# Initialize feedback DB on startup
init_feedback_db()
