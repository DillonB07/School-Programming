import json
import os
import sqlite3

PRICES = {
    "Carpets": 22.50,
    "Underlay - First Step": 5.99,
    "Underlay - Monarch": 7.99,
    "Underlay - Royal": 60,
    "Gripper": 1.10,
    "hour": 65,
}

AMOUNT_PER_HOUR = 16  # Amount of square metres he can do per hour

db = sqlite3.connect("Proj.db")
cursor = db.cursor()


def add_customer():
    """Add a customer to the database"""

    customer = {}
    customer["forename"] = input("Forename: ")
    customer["surname"] = input("Surname: ")
    customer["town"] = input("Town: ")
    customer["telephone"] = input("Telephone number: ")

    cursor.execute(
        f"""
        INSERT INTO Customers
        VALUES (\'{customer["forename"]}\', \'{customer["surname"]}\', \'{customer["town"]}\', \'{customer["telephone"]}\')
        """
    )
    db.commit()


def list_customers():
    """List all customers"""
    cursor.execute("SELECT * FROM Customers")
    print("Forename | Surname | Town | Telephone")
    for row in cursor.fetchall():
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")


def add_quote():
    """Add a quote to the database"""
    pass

def list_quotes():
    """List all quotes"""
    cursor.execute("SELECT * FROM Quotes")
    print("Name | Date | Time | Square Metres | Total Price")
    for row in cursor.fetchall():
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

def menu():
    """Display the menu"""
    try:
        print(
            """
    1. Add a customer
    2. List all customers
    3. Add a new quote
    4. List all quotes
    5. Export customers and quotes
    6. Exit
    """
        )
        option = int(input(">>> "))
        if option == 1:
            add_customer()
        elif option == 2:
            list_customers()
        elif option == 3:
            add_quote()
        elif option == 4:
            list_quotes()
        elif option == 5:
            pass
        elif option == 6:
            raise KeyboardInterrupt
    except ValueError:
        print("Invalid option")
        menu()


while True:
    menu()
