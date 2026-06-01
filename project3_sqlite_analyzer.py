import sqlite3

# Project 3: SQLite Database Analyzer
# Author: Nouetakdie Kamgue Clement

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("ai_data.db")
cur = conn.cursor()

# Create table
cur.execute("""
DROP TABLE IF EXISTS Users
""")

cur.execute("""
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

# Insert sample data
data = [
    ("Clement", 41),
    ("Alice", 25),
    ("Bob", 30),
    ("Maria", 22),
    ("John", 35)
]

cur.executemany("INSERT INTO Users (name, age) VALUES (?, ?)", data)

conn.commit()

# Read data
cur.execute("SELECT * FROM Users")

print("DATABASE CONTENT")
print("-" * 30)

for row in cur.fetchall():
    print(row)

# Analysis: average age
cur.execute("SELECT AVG(age) FROM Users")
avg_age = cur.fetchone()[0]

print("\nAverage Age:", round(avg_age, 2))

conn.close()
