import sqlite3
from sqlite3 import Error


def foodItems_table():
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute('''DROP TABLE IF EXISTS food_items;''')
    
    cur.execute('''CREATE TABLE food_items
                    (foodName TEXT PRIMARY KEY, 
                    price TEXT 
                    );''')

    cur.execute('''INSERT INTO food_items (foodName, price) VALUES 
                        ('Small Pizza', '$6'), 
                        ('Medium Pizza', '$8'), 
                        ('Large Pizza', '$10'),
                        ('Cheeseburger', '$5'),
                        ('Loaded Fries', '$6'),
                        ('Club Sandwich', '$10');''')

    cur.execute("SELECT * FROM food_items;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()
    return rows


def pizzaToppings_table():
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON")
    cur.execute('''DROP TABLE IF EXISTS pizza_toppings;
                ''')

    cur.execute('''CREATE TABLE pizza_toppings
                   (toppingNum INTEGER PRIMARY KEY,
                    toppingName TEXT,
                    price TEXT
                    )
    ''')

    cur.execute('''INSERT INTO pizza_toppings (toppingNum, toppingName, price) VALUES
                        (1, 'Pepperoni', '$1'),
                        (2, 'Mushrooms', '$1'),
                        (3, 'Onions', '$1'),
                        (4, 'Sausage', '$1'),
                        (5, 'Bacon', '$1'),
                        (6, 'Extra Cheese', '$1'),
                        (7, 'Black Olives', '$1'),
                        (8, 'Green Peppers', '$1'),
                        (9, 'Pineapple', '$1'),
                        (10, 'Spinach', '$1')''')

    cur.execute("SELECT * FROM pizza_toppings")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()
    return rows


def food_items():
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute('''DROP TABLE IF EXISTS food_items;''')
    
    cur.execute('''CREATE TABLE food_items
                    (foodName TEXT PRIMARY KEY, 
                    price TEXT 
                    );''')

    cur.execute('''INSERT INTO food_items (foodName, price) VALUES 
                        ('Small Pizza', '$6'), 
                        ('Medium Pizza', '$8'), 
                        ('Large Pizza', '$10'),
                        ('Cheeseburger', '$8'),
                        ('Loaded Fries', '$6'),
                        ('Club Sandwich', '$10');''')

    cur.execute("SELECT foodName, price FROM food_items;")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def pizza_toppings():
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute('''DROP TABLE IF EXISTS pizza_toppings;''')

    cur.execute('''CREATE TABLE pizza_toppings
                    (toppingName TEXT PRIMARY KEY,
                    price TEXT
                    )
    ''')

    cur.execute('''INSERT INTO pizza_toppings (toppingName, price) VALUES
                        ('Pepperoni', '$1'),
                        ('Mushrooms', '$1'),
                        ('Onions', '$1'),
                        ('Sausage', '$1'),
                        ('Bacon', '$1'),
                        ('Black Olives', '$1'),
                        ('Green Peppers', '$1'),
                        ('Pineapple', '$1'),
                        ('Spinach', '$1')''')

    cur.execute("SELECT * FROM pizza_toppings")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def orders():
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute('''DROP TABLE IF EXISTS orders;''')
    cur.execute('''CREATE TABLE orders
                    (orderID INTEGER PRIMARY KEY AUTOINCREMENT,
                    orderName TEXT,
                    totalFood TEXT,
                    pizzaTop TEXT, 
                    burgerTop TEXT,
                    totalPrice TEXT
                    )
    ''') 
    #cur.execute('''INSERT INTO orders (orderName, totalFood, totalPrice) VALUES ('Ben Hansen', 'Cheeseburger + Loaded Fries', '$11')''')
    

    cur.execute("SELECT * FROM orders;")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows 

def insert_order(orderName, totalFood, burgerTop, pizzaTop, totalPrice):
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute('''INSERT INTO orders (orderName, totalFood, burgerTop, pizzaTop, totalPrice) VALUES ((?), (?), (?), (?), (?)) ''', (orderName, totalFood, burgerTop, pizzaTop, totalPrice,))
    conn.commit()
    conn.close()
    return 

def burger_top():
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute('''DROP TABLE IF EXISTS burger;''')
    cur.execute('''CREATE TABLE burger (
                    toppingName TEXT PEIMARY KEY               
    ) 
                ''')       
    cur.execute('''INSERT INTO burger (toppingName) VALUES 
                                                ('Ketchup'),
                                                ('Mustard'),
                                                ('Mayo'), 
                                                ('Pickels'),
                                                ('Lettuce'),
                                                ('Tomato'),
                                                ('Onion')
                                                ''')
    
    cur.execute("SELECT * FROM burger;")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def show_order(orderID):
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute("SELECT  FROM orders;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()
    return rows

def fetch_orderID(id):
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute("SELECT orderID FROM orders WHERE orderID = (?);", (id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def change_pizza():
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute('''
            ''')
    cur.execute("SELECT * FROM pizza;")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def update_order(foodItem):
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    cur.execute('''UPDATE orders SET food_item = (?) WHERE orderID = 4 ;''', (foodItem, ))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows