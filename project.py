import json
import os
import sqlite

PRICES = {
        "Carpets": 22.50,
        "Underlay - First Step": 5.99,
        "Underlay - Monarch": 7.99,
        "Underlay - Royal": 60,
        "Gripper": 1.10
        "hour": 65
    }

AMOUNT_PER_HOUR = 16 # Amount of square metres he can do per hour

db = sqlite3.connect('Proj.db')
cursor = db.cursor()

def add_customer(customer):
    customer = {}
    customer['forename'] = input('Forename: ')
    customer['surname'] = input('Surname: ')
    customer['town'] = input('Town: ')
    customer['telephone'] = input('Telephone number: ')

    cursor.execute(f'INSERT INTO Customers ({customer["forename"], {customer["surname"]}, {customer["town"]}, {customer["telephone"]})')
    db.commit()


