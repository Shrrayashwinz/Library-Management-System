"""
Program Name: main.py

Author: Shrrayash Srinivasan

Purpose: Main file for the library management.

Date: June 10, 2026
 
"""

import json
import os

DATA_FILE = "data.json"

# ----------- Load and Save ------------------------------

def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_data(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)




students = []

books = []

def load_data():
    pass

def save_data():
    pass

# ---------------- FUNCTIONS --------------------------
def add_students():
    try:
        student = input("Enter the student: ")
    
    except TypeError:
        print("ERROR: Not a name")
        return
    




def view_students():
    pass

def search_student():
    for s in students:
        if s["Name"].lower() == name.lower():
            return s
    return None

def delete_pass():
    pass

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
       




