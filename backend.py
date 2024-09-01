# backend.py
import sqlite3

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_scores (
            id INTEGER PRIMARY KEY,
            score INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Function to save the score to the database
def save_score(score):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO quiz_scores (score) VALUES (?)', (score,))
    conn.commit()
    conn.close()

# Function to retrieve the highest score from the database
def get_highscore():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(score) FROM quiz_scores')
    highscore = cursor.fetchone()[0]
    conn.close()
    return highscore if highscore is not None else 0

# Function to clear the database (optional, for testing purposes)
def clear_scores():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM quiz_scores')
    conn.commit()
    conn.close()
