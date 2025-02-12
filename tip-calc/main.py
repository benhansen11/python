import sqlite3
from sql_commands import *
from functions import *

order_name = ""
order_food = ""
food = ""
price = ""


def burger_toppings():
    global food
    global order_name
    choices = []
    while True:
        print("------------------------------------")
        print("-----Burger Topping-----")
        print("0. Back to Menu")
        for x in enumerate(burger_top()):
                print(f"{x[0]+1}. {x[1][0]}")
        inp = int(input("What would you like on your Cheseburger?: "))
        if inp == 0:
            break
        else:
            choices.append(inp)
            result = [int(digit) for digit in str(choices[0])]
            print("You have chosen the following toppings: ")
            print("-----------")
            for x in result:
                print(f"{burger_top()[x-1][0]}")
            print("-----------")
            inpt = str(input("Would you like to change your toppings? (y/n): "))
            if inpt.lower() == "y":
                choices.clear()
                burger_toppings()
            elif inpt.lower() == "n":
                print("---------------------------")
                print("Your order has been placed!")
                print("---------------------------")
                insert_order(order_name, food, '', '', price)
            break
        
    return

def pizza_toppings_choice():
    global order_food
    choices = []
    while True:
        print("-----Pizza Toppings-----")
        print("0. Back to Menu")
        for x in enumerate(pizza_toppings()):
            print(f"{x[0]+1}. {x[1][0]} - {x[1][1]}")
        choice = int(input("Please choose up to 3 toppings for your pizza using the numbers below or enter 0 to go back to the menu: "))
        if len(str(choice)) > 3:
            print("You can only choose up to 3 toppings. Please try again.")
            pizza_toppings_choice()
        else:
            if choice == 0:
                break
            else:
                choices.append(choice)
                result = [int(digit) for digit in str(choices[0])]
                #print(result)
                print("You have chosen the following toppings: ")
                print("----------")
                for x in result:
                    print(f"{pizza_toppings()[x-1][0]}")
                print("----------")   
                inpt = str(input("Would you like to change your toppings? (y/n): "))
                if inpt.lower() == "y":
                    choices.clear()
                    pizza_toppings_choice()
                elif inpt.lower() == "n":
                    print("---------------------------")
                    print("Your order has been placed!")
                    print("---------------------------")
                    insert_order(order_name, food, '', '', price)
                break
        
    return

def view_or_change_order():
    conn = sqlite3.connect('food.db')
    cur = conn.cursor()
    cur.execute("Pragma foreign_keys = ON;")
    query = '''SELECT (orderName AS "Order", totalFood AS "Food Items", pizzaTop As "Pizza Toppings", burgerTop AS "Burger Toppings", totalPrice AS "Price") FROM orders
                WHERE pizzaTop IS NOT NULL AND burgerTop IS NOT NULL;'''
    while True:
        print("------------------------------")
        print("-----View/Change Order-----")
        print("------------------------------")
        inp = int(input("If you would like to view or change your order, press 1, if you are finished and would like to checkout, press 2: "))
        if inp == 1:
            print("Your order is as follows: ")
            print("---------------------------")
            
                        
    cur.execute(query)
    
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def menu():


    global order_name
    global order_food
    global food
    global price
    while True:
        print("-----------------------------------")
        print("-----Welcome to my Restaurant!-----")
        print("-----------------------------------")
        name = str(input("Please enter a name for the order: "))
        order_name += name
        print(order_name)
        print("-----------------------------------")
        print("0. Exit")
        for x in enumerate(food_items()):
            print(f"{x[0]+1}. {x[1][0]} - {x[1][1]}")
        choice = str(input("What would you like to order?: "))
        order_food += choice
        if choice == "0":
            print("You have exited the menu. Goodbye!")
            break
        if choice == "1":
            food = "Small Pizza"
            price = "$6"
            print("----------------------------------")
            print("You chose a small Pizza!")
            print("----------------------------------")
            pizza_toppings_choice()
        elif choice == "2":
            food = "Medium Pizza"
            price = "$8"
            print("----------------------------------")
            print("You chose a Medium Pizza!")
            print("----------------------------------")
            pizza_toppings_choice()
        elif choice == "3":
            food = "Large Pizza"
            price = "$10"
            print("----------------------------------")
            print("You chose Large Pizza!")
            print("----------------------------------")
            pizza_toppings_choice()
        elif choice == "4": 
            food = "Cheeseburger"
            price = "$8"
            print("You chose Cheeseburger!")
            burger_toppings()
        elif choice == "5":
            print("You chose Loaded Fries!")
        elif choice == "6":
            print("You chose a Club Sandwich")
        else:
            print("Invalid choice!")
            continue

        
        


menu()
#burger_top()    
#orders()
