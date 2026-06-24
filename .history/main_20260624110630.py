import sqlite3

# -----------------------------
# DATABASE INITIALIZATION
# -----------------------------
conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")
conn.commit()


# -----------------------------
# FUNCTIONS
# -----------------------------
def add_student():
    try:
        name = input("Enter student name: ")
        sid = int(input("Enter student ID: "))

        cur.execute("INSERT INTO students (id, name) VALUES (?, ?)", (sid, name))
        conn.commit()
        print("✅ Student added successfully!")

    except sqlite3.IntegrityError:
        print("❌ Error: A student with this ID already exists.")
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")


def view_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    if not rows:
        print("📭 No students found.")
        return

    print("\n--- All Students ---")
    for r in rows:
        print(f"ID: {r[0]} | Name: {r[1]}")


def search_student():
    name = input("Enter name to search: ")

    cur.execute("SELECT * FROM students WHERE name = ?", (name,))
    result = cur.fetchone()

    if result:
        print(f"🎯 Found: ID={result[0]}, Name={result[1]}")
    else:
        print("❌ Student not found.")


def delete_student():
    try:
        sid = int(input("Enter student ID to delete: "))

        cur.execute("DELETE FROM students WHERE id = ?", (sid,))
        conn.commit()

        if cur.rowcount > 0:
            print("🗑️ Student deleted successfully!")
        else:
            print("❌ No student found with that ID.")

    except ValueError:
        print("❌ Invalid ID. Please enter a number.")


# -----------------------------
# MENU LOOP
# -----------------------------
def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting system...")
            break
        else:
            print(" Invalid choice. Try again.")


# -----------------------------
# RUN PROGRAM
# -----------------------------
menu()
conn.close()

