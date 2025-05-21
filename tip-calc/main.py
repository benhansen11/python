import sqlite3
from sql_commands import *
from functions import *

order_name = ""
order_food = ""
food = ""
price = ""
food_update = ""
user_food_ = []




def burger_toppings():
    global food
    global order_name
    user_food_ = []
    user_price = ""
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
            print(result)
            print("You have chosen the following toppings: ")
            print("-----------")
            for x in result:
                print(f"{burger_top()[x-1][0]}")
                user_food_.append(burger_top()[x-1][0])
            result_ = ', '.join(user_food_)
            print("-----------")
            inpt = str(input("Would you like to change your toppings? (y/n): "))
            if inpt.lower() == "y":
                choices.clear()
                burger_toppings()
            elif inpt.lower() == "n":
                print("---------------------------")
                print("Your order has been placed!")
                print("---------------------------")
                insert_order(order_name, food, result_, '', price)
            break
        
    return

def pizza_toppings_choice():
    global order_food
    global user_food_
    choices = []
    #result_ = ""
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
                    #user_food_.append(pizza_toppings()[x-1][0])
                #result_ = ', '.join(user_food_)    
                print("----------")   
                inpt = str(input("Would you like to change your toppings? (y/n): "))
                if inpt.lower() == "y":
                    choices.clear()
                    pizza_toppings_choice() 
                elif inpt.lower() == "n":
                    print("---------------------------")
                    print("Your order has been placed!")
                    for x in result:
                        user_food_.append(pizza_toppings()[x-1][0])
                    result_ = ', '.join(user_food_)
                    print(result_)
                    print("---------------------------")
                    insert_order(order_name, food, '', result_, price)
                break
        
    return


def view_or_change_order():
    global order_name
    global order_food
    global food
    global food_update
    global price
    global user_food_

    result_ = ', '.join(user_food_)

    while True:
        print("-----View/Change Order-----")
        print("---------------------------")
        inp = int(input("If you would like to view or change your order, press 1, if you are finished and would like to checkout, press 2: "))
        if inp == 1:
            print("Your order is as follows: ")
            print("---------------------------")
            print(f"Order Name: {order_name}")
            print(f"Food: {food}")
            print(f"Toppings: {result_}")
            print(f"Price: {price}")
            inpt = str(input("Would you like to change your order? (y/n): "))
            if inpt.lower() == "y": 
                result_ = None
                menu()
                update_order(food, order_name, result_)
                break
            elif inpt.lower() == "n":
                print("")
                break
        elif inp == 2:
            print("---------------------------")
            print("Your order has been placed!")
            print("---------------------------")
            print(f"You ordered a {food}.")
            print(f"You're order total is {price} dollars.")
            print("Thank you for shopping with us today!")
            print("---------------------------")
            break
            

        
def menu(): 
    global order_name
    global order_food
    global food
    global price
    while True:
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
            view_or_change_order()
            break
        elif choice == "2":
            food = "Medium Pizza"
            price = "$8"
            print("----------------------------------")
            print("You chose a Medium Pizza!")
            print("----------------------------------")
            pizza_toppings_choice()
            view_or_change_order()
            break
        elif choice == "3":
            food = "Large Pizza"
            price = "$10"
            print("----------------------------------")
            print("You chose Large Pizza!")
            print("----------------------------------")
            pizza_toppings_choice()
            view_or_change_order()
        elif choice == "4": 
            food = "Cheeseburger"
            price = "$8"
            print("You chose Cheeseburger!")
            burger_toppings()
            view_or_change_order()
        elif choice == "5":
            print("You chose Loaded Fries!")
        elif choice == "6":
            print("You chose a Club Sandwich")
        else:
            print("Invalid choice!")
            continue    


def main():
    global order_name
    global order_food
    global food
    global price
    print("-----------------------------------")
    print("-----Welcome to my Restaurant!-----")
    print("-----------------------------------")
    name = str(input("Please enter a name for the order: "))
    order_name += name
    menu()
    


main()
#burger_top()    
#orders()
