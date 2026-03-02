import sqlite3, hashlib

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username,email,password):
    try:
        c.execute("INSERT INTO users(username,email,password) VALUES(?,?,?)", 
                  (username,email,hash_password(password)))
        conn.commit()
        return True
    except:
        return False

def login_user(email,password):
    c.execute("SELECT username,password FROM users WHERE email=?", (email,))
    data = c.fetchone()
    if data and data[1]==hash_password(password):
        return data[0]
    return None