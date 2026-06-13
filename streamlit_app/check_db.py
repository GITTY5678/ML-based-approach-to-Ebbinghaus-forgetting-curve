import sqlite3

conn = sqlite3.connect(
    "memory_retention.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM study_sessions"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
