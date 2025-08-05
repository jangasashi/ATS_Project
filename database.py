#database py

import sqlite3

DB_NAME = "ats_users.db"

def connect():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def create_users_table():
    conn = connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    role TEXT
                )''')
    conn.commit()
    conn.close()

def create_match_log_table():
    conn = connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS match_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    resume_filename TEXT,
                    jd_filename TEXT,
                    match_score REAL,
                    match_percentage TEXT,
                    matched_on TEXT
                )''')
    conn.commit()
    conn.close()

def add_user(username, password, role):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if row:
        return {"username": row[0], "password": row[1], "role": row[2]}
    return None

def get_all_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT username, role FROM users")
    users = c.fetchall()
    conn.close()
    return users

def log_match_result(username, resume_filename, jd_filename, match_score, match_percentage, matched_on):
    conn = connect()
    c = conn.cursor()
    c.execute('''INSERT INTO match_logs (username, resume_filename, jd_filename, match_score, match_percentage, matched_on)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (username, resume_filename, jd_filename, match_score, match_percentage, matched_on))
    conn.commit()
    conn.close()

def get_match_history(username=None):
    conn = connect()
    c = conn.cursor()
    if username:
        c.execute("SELECT * FROM match_logs WHERE username = ?", (username,))
    else:
        c.execute("SELECT * FROM match_logs")
    rows = c.fetchall()
    conn.close()
    return rows