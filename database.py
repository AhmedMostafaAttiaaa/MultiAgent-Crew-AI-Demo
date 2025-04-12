# Dummy database file (can be extended)
import sqlite3

def init_db():
    conn = sqlite3.connect("event_management.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_message(msg):
    conn = sqlite3.connect("event_management.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs (message) VALUES (?)", (msg,))
    conn.commit()
    conn.close()
