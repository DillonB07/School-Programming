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

    cursor.execute(f"""
        INSERT INTO Customers
        VALUES (\'{customer["forename"]}\', \'{customer["surname"]}\', \'{customer["town"]}\', \'{customer["telephone"]}\')
        """)
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
    quote["total_price"] = (
        PRICES[quote["underlay"]][1] * quote["square_metres"]) + (math.ceil(
            quote["square_metres"] / AMOUNT_PER_HOUR) * PRICE_PER_HOUR)

    cursor.execute(f"""
INSERT INTO Quotes
VALUES (\'{quote["customer"]}\', \'{quote["length"]}\', \'{quote["width"]}\', \'{quote['underlay']}\', \'{quote["total_price"]}\')
        """)
    db.commit()


def list_quotes():
    """List all quotes"""
    cursor.execute("SELECT * FROM Quotes")
    print(
        f"{'Name':10} | {'Length':10} | {'Width':10} | {'Square Metres':10} | {'Underlay':10} | Total Price"
    )
    for row in cursor.fetchall():
        cursor.execute(
            f"SELECT forename, surname FROM Customers WHERE ROWID = {row[0]}")
        customer = cursor.fetchone()
        print(
            f"{customer[1] + ', ' + customer[0]:10} | {row[1] + 'm':10} | {row[2] + 'm':10} | {str(int(row[1]) * int(row[2])) + 'm^2':10}| {row[3]:10} | £{row[4]}"
        )


def export():
    """Export the database to a CSV file"""
    data = {"users": []}
    cursor.execute("SELECT *, ROWID FROM Customers")
    for row in cursor.fetchall():
        # print(f"{row=}")
        cursor.execute(f"SELECT * FROM Quotes WHERE customer = {row[-1]}")
        quotes = cursor.fetchall()
        user = {
            "surname": row[1],
            "forename": row[0],
            "town": row[2],
            "telephone": row[3],
            "total_quotes": len(quotes),
            "quotes": []
        }
        for quote in quotes:
            # print(f"{quote=}")
            user["quotes"].append({
                "length":
                int(quote[1]),
                "width":
                int(quote[2]),
                "square_metres":
                int(quote[1]) * int(quote[2]),
                "underlay":
                quote[3],
                "total_price":
                float(quote[4]),
            })
        data["users"].append(user)
    json.dump(data, open("data.json", "w", encoding="utf-8"), indent=4)
    with open("customer_data.csv", "w") as f:
        f.write('surname, forename, town, telephone, quotes\n')
        for user in data["users"]:
            # f.write("%s,%s"%(key,data[key]))
            f.write(
                f"{user['surname'].upper()}, {user['forename'].lower()},{user['town']},{user['telephone']},{user['total_quotes']}\n"
            )
    with open('quotes_data.csv', 'w') as f:
        f.write('customer, length, width, square_metres, underlay, total_price\n')
        for user in data["users"]:
            for quote in user["quotes"]:
                f.write(
                    f"{user['surname'].upper()} {user['forename'].lower()},{quote['length']},{quote['width']},{quote['square_metres']},{quote['underlay']},{quote['total_price']:.2f}\n"
                )


def menu():
    """Display the menu"""
    try:
        print("""
    1. Add a customer
    2. List all customers
    3. Add a new quote
    4. List all quotes
    5. Export customers and quotes
    6. Exit
    """)
        option = int(input(">>> "))
        options = {
            1: add_customer,
            2: list_customers,
            3: add_quote,
            4: list_quotes,
            5: export,
            6: sys.exit,
        }
    except ValueError:
        print("Invalid option")
        menu()
    else:
        options[option]()

print(f'{"Decorator Database":=^50}')
while True:
    menu()
