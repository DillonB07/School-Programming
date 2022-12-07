import csv
import sqlite3
import sys
import math
import json

PRICES = [
    ["Carpets", 22.50],
    ["Underlay - First Step", 5.99],
    ["Underlay - Monarch", 7.99],
    ["Underlay - Royal", 60],
    ["Gripper", 1.10],
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
    print(f"{'Forename':10} | {'Surname':10} | {'Town':10} | Telephone")
    for row in cursor.fetchall():
        print(f"{row[0]:10} | {row[1]:10} | {row[2]:10} | {row[3]}")


def add_quote():
    """Add a quote to the database"""
    quote = {}
    customers = []
    cursor.execute("SELECT forename, surname, ROWID FROM Customers")
    for i, row in enumerate(cursor.fetchall()):
        customers.append({"id": row[2], "forename": row[0], "surname": row[1]})
        print(f"{i+1}) {row[1]}, {row[0]}")

    quote["customer"] = customers[int(input("Select a customer: ")) - 1]["id"]
    quote["length"] = int(input("Length: "))
    quote["width"] = int(input("Width: "))
    quote["square_metres"] = quote["length"] * quote["width"]
    for i, item in enumerate(PRICES):
        print(f"{i + 1}) {item[0]}")
    quote["underlay"] = int(input("Select an underlay: ")) - 1
    quote["total_price"] = (PRICES[quote["underlay"]][1] * quote["square_metres"]) + (
        math.ceil(quote["square_metres"] / AMOUNT_PER_HOUR) * PRICE_PER_HOUR
    )

    cursor.execute(
        f"""
INSERT INTO Quotes
VALUES (\'{quote["customer"]}\', \'{quote["length"]}\', \'{quote["width"]}\', \'{quote['underlay']}\', \'{quote["total_price"]}\')
        """
    )
    db.commit()


def list_quotes():
    """List all quotes"""
    cursor.execute("SELECT * FROM Quotes")
    print(
        f"{'Name':10} | {'Length':10} | {'Width':10} | {'Square Metres':10} | {'Underlay':10} | Total Price"
    )
    for row in cursor.fetchall():
        cursor.execute(
            f"SELECT forename, surname FROM Customers WHERE ROWID = {row[0]}"
        )
        customer = cursor.fetchone()
        print(
            f"{customer[0] + ' ' + customer[1]:10} | {row[1] + 'm':10} | {row[2] + 'm':10} | {str(int(row[1]) * int(row[2])) + 'm^2':10}| {row[3]:10} | £{row[4]}"
        )  # NOQA


def export():
    """Export the database to a CSV file"""
    data = {"users": []}
    cursor.execute("SELECT *, ROWID FROM Customers")
    for row in cursor.fetchall():
        # print(f"{row=}")
        user = {
                "surname": row[1],
                "forename": row[0],
                "town": row[2],
                "telephone": row[3],
                "quotes": []
            }
        cursor.execute(f"SELECT * FROM Quotes WHERE customer = {row[-1]}")
        for quote in cursor.fetchall():
            # print(f"{quote=}")
            user['quotes'].append({"length": int(quote[0]),
                "width": int(quote[1]),
                "square_metres": int(quote[0]) * int(quote[1]),
                "underlay": quote[2],
                "total_price": int(quote[3]),
            })
        data['users'].append(user)
    print(f"{data=}")
    json.dump(data, open("data.json", "w", encoding='utf-8'), indent=4)
    # with open('test.csv', 'w') as f:
    #     for key in my_dict.keys():
    #         f.write("%s,%s"%(key,my_dict[key])) # NOQA


def menu():
    """Display the menu"""
    try:
        print(
            """
    1. Add a customer
    2. List all customers
    3. Add a new quote
    4. List all quotes
    5. Export customers and quotes [TO DO]
    6. Exit
    """
        )
        option = int(input(">>> "))
        options = {
            1: add_customer,
            2: list_customers,
            3: add_quote,
            4: list_quotes,
            5: export,
            6: sys.exit,
        }
        options[option]()
        # if option == 1:
        #     add_customer()
        # elif option == 2:
        #     list_customers()
        # elif option == 3:
        #     add_quote()
        # elif option == 4:
        #     list_quotes()
        # elif option == 5:
        #     export()
        # elif option == 6:
        #     sys.exit()
    except ValueError:
        print("Invalid option")
        menu()


# Using options dictionary, call the function

while True:
    menu()
