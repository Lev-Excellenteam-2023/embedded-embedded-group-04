import sqlite3
from datetime import datetime

conn = sqlite3.connect('potholes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS potholes (
    id INTEGER PRIMARY KEY,
    longitude REAL,
    latitude REAL,
    type TEXT,
    date TEXT
)
''')

conn.commit()
