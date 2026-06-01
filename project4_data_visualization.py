import sqlite3
import matplotlib.pyplot as plt

# Project 4: Data Visualization
# Author: Nouetakdie Kamgue Clement

# Connect to database from Project 3
conn = sqlite3.connect("ai_data.db")
cur = conn.cursor()

# Read data
cur.execute("SELECT name, age FROM Users")
data = cur.fetchall()

names = []
ages = []

for row in data:
    names.append(row[0])
    ages.append(row[1])

print("DATA LOADED:")
for n, a in zip(names, ages):
    print(n, a)

# -----------------------------
# BAR CHART
# -----------------------------
plt.figure()
plt.bar(names, ages)
plt.title("User Ages")
plt.xlabel("Name")
plt.ylabel("Age")
plt.show()

# -----------------------------
# PIE CHART (Age distribution style)
# -----------------------------
plt.figure()
plt.pie(ages, labels=names, autopct='%1.1f%%')
plt.title("Age Distribution")
plt.show()
