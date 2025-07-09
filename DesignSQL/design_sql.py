import sqlite3
import os
from datetime import datetime

DB_FILE = 'ecommerce.db'

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES Users(id),
            FOREIGN KEY (product_id) REFERENCES Products(id)
        )
    ''')

    conn.commit()

except sqlite3.Error:
    conn.rollback()
    conn.close()
    exit()

users_data = [
    ('Alice Smith', 'alice@example.com'),
    ('Bob Johnson', 'bob@example.com'),
    ('Charlie Brown', 'charlie@example.com')
]
try:
    cursor.executemany("INSERT INTO Users (name, email) VALUES (?, ?)", users_data)
    conn.commit()
except sqlite3.Error:
    conn.rollback()

products_data = [
    ('Laptop', 1200.00),
    ('Mouse', 25.00),
    ('Keyboard', 75.00),
    ('Monitor', 300.00)
]
try:
    cursor.executemany("INSERT INTO Products (name, price) VALUES (?, ?)", products_data)
    conn.commit()
except sqlite3.Error:
    conn.rollback()

cursor.execute("SELECT id FROM Users WHERE email = 'alice@example.com'")
alice_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM Users WHERE email = 'bob@example.com'")
bob_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM Users WHERE email = 'charlie@example.com'")
charlie_id = cursor.fetchone()[0]

cursor.execute("SELECT id FROM Products WHERE name = 'Laptop'")
laptop_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM Products WHERE name = 'Mouse'")
mouse_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM Products WHERE name = 'Keyboard'")
keyboard_id = cursor.fetchone()[0]

orders_data = [
    (alice_id, laptop_id, 1, datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
    (bob_id, mouse_id, 2, datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
    (alice_id, keyboard_id, 1, datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
    (charlie_id, laptop_id, 1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
]
try:
    cursor.executemany("INSERT INTO Orders (user_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?)", orders_data)
    conn.commit()
except sqlite3.Error:
    conn.rollback()

query_sql = '''
    SELECT
        O.id AS order_id,
        U.name AS user_name,
        P.name AS product_name,
        O.quantity,
        P.price AS unit_price,
        (O.quantity * P.price) AS total_price,
        O.order_date
    FROM Orders AS O
    JOIN Users AS U ON O.user_id = U.id
    JOIN Products AS P ON O.product_id = P.id
    ORDER BY O.order_date DESC;
'''

try:
    cursor.execute(query_sql)
    results = cursor.fetchall()

    for row in results:
        print(row)

except sqlite3.Error:
    pass

finally:
    conn.close()