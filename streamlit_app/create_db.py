from database.db import get_connection

conn = get_connection()

cursor = conn.cursor()

with open(
    "database/schema.sql",
    "r"
) as file:

    cursor.executescript(
        file.read()
    )

conn.commit()

conn.close()

print(
    "Database Created Successfully"
)