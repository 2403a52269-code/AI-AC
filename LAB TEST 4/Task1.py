import sqlite3
import random
from datetime import datetime, timedelta

# Create/connect to database
conn = sqlite3.connect('food_delivery.db')
cursor = conn.cursor()

# Create tables
cursor.executescript('''
CREATE TABLE IF NOT EXISTS Restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    rating FLOAT
);

CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    address TEXT
);

CREATE TABLE IF NOT EXISTS Menu_Items (
    item_id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    name TEXT NOT NULL,
    price DECIMAL(10,2),
    category TEXT,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
);

CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    restaurant_id INTEGER,
    item_id INTEGER,
    order_date DATETIME,
    status TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id),
    FOREIGN KEY (item_id) REFERENCES Menu_Items(item_id)
);
''')

# Insert sample data
# Restaurants
restaurants_data = [
    (1, 'Spice Garden', 'MG Road, Bangalore', 4.5),
    (2, 'Royal Kitchen', 'HSR Layout, Bangalore', 4.2),
    (3, 'Food Paradise', 'Koramangala, Bangalore', 4.7)
]
cursor.executemany('INSERT OR REPLACE INTO Restaurants VALUES (?,?,?,?)', restaurants_data)

# Customers
customers_data = [
    (1, 'Rahul Kumar', 'rahul@email.com', '9876543210', 'Indiranagar'),
    (2, 'Priya Singh', 'priya@email.com', '9876543211', 'JP Nagar'),
    (3, 'Amit Shah', 'amit@email.com', '9876543212', 'Whitefield')
]
cursor.executemany('INSERT OR REPLACE INTO Customers VALUES (?,?,?,?,?)', customers_data)

# Menu Items
menu_items_data = [
    (1, 1, 'Butter Chicken', 550.00, 'Main Course'),
    (2, 1, 'Biryani', 450.00, 'Main Course'),
    (3, 2, 'Seafood Platter', 850.00, 'Main Course'),
    (4, 2, 'Pizza', 600.00, 'Italian'),
    (5, 3, 'Sushi Combo', 750.00, 'Japanese')
]
cursor.executemany('INSERT OR REPLACE INTO Menu_Items VALUES (?,?,?,?,?)', menu_items_data)

# Orders
orders_data = [
    (1, 1, 1, 1, '2023-11-01 12:00:00', 'Delivered'),
    (2, 2, 2, 3, '2023-11-01 13:00:00', 'Delivered'),
    (3, 3, 3, 5, '2023-11-01 14:00:00', 'Delivered'),
    (4, 1, 2, 4, '2023-11-01 15:00:00', 'Delivered')
]
cursor.executemany('INSERT OR REPLACE INTO Orders VALUES (?,?,?,?,?,?)', orders_data)

# Query to list customers who ordered items costing above ₹500
query = '''
SELECT DISTINCT c.name, c.email, m.name as item_name, m.price
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Menu_Items m ON o.item_id = m.item_id
WHERE m.price > 500
ORDER BY m.price DESC;
'''

print("\nCustomers who ordered items costing above ₹500:")
print("------------------------------------------------")
for row in cursor.execute(query):
    print(f"Customer: {row[0]}")
    print(f"Email: {row[1]}")
    print(f"Item: {row[2]}")
    print(f"Price: ₹{row[3]}")
    print("------------------------------------------------")

# Commit changes and close connection
conn.commit()
conn.close()