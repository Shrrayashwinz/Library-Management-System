"""
Program Name: main.py

Author: Shrrayash Srinivasan

Purpose: Main file for the library management.

Date: June 10, 2026
 
"""
import os
import json
import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")

conn.commit()

DATA_FILE = "data.json"

# ----------- Load and Save ------------------------------
students = []

books = []


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:    
        return []


def save_data(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


def load_data():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
         return []


# ---------------- FUNCTIONS --------------------------
def add_student():
    name = input("Enter name: ")
    sid = int(input("Enter ID: "))
    cur.execute("INSERT INTO students (id, name) VALUES (?, ?)", (sid, name))
    conn.commit()
    print("Student added!")

def view_students():
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)

def search_student():
    name = input("Enter name to search: ")
    cur.execute("SELECT * FROM students WHERE name = ?", (name,))
    result = cur.fetchone()
    print(result if result else "Not found")

def delete_student():
    sid = int(input("Enter ID to delete: "))
    cur.execute("DELETE FROM students WHERE id = ?", (sid,))
    conn.commit()
    print("Deleted!")

# -------------------------------------
# main function
# -------------------------------------

def main():


    while True:
        print("\n Welcome to the Library management system!")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        option = input("Select Option")

        if option == "1":
            pass
   
        elif option == "2":
            pass

        elif option == "3":
            pass
 
        elif option == "4":
            pass

        elif option == "5":
            pass

        else:
            print("Invalid Choice!") 
       

menu()
