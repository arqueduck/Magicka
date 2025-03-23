import sqlite3

def init_db():
    conn = sqlite3.connect("scores.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_score(name: str, score: int):
    conn = sqlite3.connect("scores.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

def get_top_scores(limit=10):
    conn = sqlite3.connect("scores.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, score, timestamp FROM scores ORDER BY score DESC LIMIT ?", (limit,))
    results = cursor.fetchall()
    conn.close()
    return results