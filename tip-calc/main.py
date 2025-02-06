import sqlite3
from sql_commands import *
from functions import *
    
def menu():
    while True:
        print("-----Welcome to my Restaurant!-----")
        print("0. Exit")
        for x in enumerate(food_items()):
            print(f"{x[0]+1}. {x[1][0]} - {x[1][1]}")
        choice = str(input("What would you like to order?: "))
        if choice == "0":
            print("You have exited the menu. Goodbye!")
            break
        if choice == "1":
            print("----------------------------------")
            print("You chose a small Pizza!")
            print("----------------------------------")
            pizza_toppings_choice()
        elif choice == "2":
            print("----------------------------------")
            print("You chose a Medium Pizza!")
            print("----------------------------------")
            pizza_toppings_choice()
        elif choice == "3":
            print("----------------------------------")
            print("You chose Large Pizza!")
            print("----------------------------------")
            pizza_toppings_choice()
        elif choice == "4":
            print("You chose Cheeseburger!")
        elif choice == "5":
            print("You chose Loaded Fries!")
        elif choice == "6":
            print("You chose a Club Sandwich")
        else:
            print("Invalid choice!")
            continue
        
        



menu()

