import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')
connect.commit()
connect.close()

print("worked")