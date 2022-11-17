import json
import os
import sqlite3

PRICES = [
    {"Carpets": 22.50},
    {"Underlay - First Step": 5.99},
    {"Underlay - Monarch": 7.99},
    {"Underlay - Royal": 60},
    {"Gripper": 1.10},
]

PRICE_PER_HOUR = 65
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
    quote = {}
    customers = []
    cursor.execute("SELECT forename, surname, ROWID FROM Customers")
    for i, row in enumerate(cursor.fetchall()):
        customers.append({"id": row[2], "forename": row[0], "surname": row[1]})
        print(f"{i}) {row[1]}, {row[0]}")

    quote["customer"] = customers[int(input("Select a customer: ")) - 1]["id"]
    quote["length"] = input("Length: ")
    quote["width"] = input("Width: ")
    quote["square_metres"] = quote["length"] * quote["width"]
    for i, item in enumerate(PRICES):
        print(f"{i + 1}) {list(item.keys())[0]}")
    quote["underlay"] = int(input("Select an underlay: ")) - 1
    quote["total_price"] = input("Total Price: ")

    cursor.execute(
        f"""
        INSERT INTO Quotes
        VALUES (\'{quote["name"]}\', \'{quote["length"]}\', \'{quote["width"]}\', \'{quote["square_metres"]}\', \'{quote['underlay']}\', \'{quote["total_price"]}\')
        """
    )
    db.commit()


def list_quotes():
    """List all quotes"""
    cursor.execute("SELECT * FROM Quotes")
    print("Name | Length | Width | Square Metres | Underlay | Total Price")
    for row in cursor.fetchall():
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")


def menu():
    """Display the menu"""
    try:
        print(
            """
    1. Add a customer
    2. List all customers
    3. Add a new quote [WIP]
    4. List all quotes
    5. Export customers and quotes [TO DO]
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
