import sqlite3
from sql_commands import *

def pizza_toppings_choice():
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
                break
        
    return

def view_or_change_order():
    print("------------------------------")
    print("-----View/Change Order-----")
    print("------------------------------")
    inp = int(input("If you would like to view or change your order, press 1, if you are finished and would like to checkout, press 2: "))
    if inp == 1:
        print("Your order is as follows: ")
        print("---------------------------")
    


    return

def add_to_order():
    print("")

    return