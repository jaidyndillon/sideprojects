#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:13:37 2024

@author: jaidyndillon
"""

aisles = ["Food", "Health", "Cosmetics", "Pets", "Checkout"]
food_shelf = {"Apples": 2.99, "Pear": 1.99, "Yogurt": 2.99, "Cereal": 7.99, "Cake": 10.99, "Nothing": "Leave Aisle"}
health_shelf = {"Advil": 9.99, "Tylenol": 8.99, "Benadryl": 9.99, "Mucinex": 10.99, "Nothing": "Leave Aisle"}
cosmetic_shelf = {"Liptstick": 5.99, "Nailpolish": 7.99, "Chapstick": 1.99, "Eyeliner": 1.99, "Nothing": "Leave Aisle"}
pets_shelf = {"Bone": 2.99, "Pet food": 16.99, "Bed": 15.99, "Leash": 10.99,"Nothing": "Leave Aisle"}

basket_items = []
price_of_basket = []   

budget = float(input("How much do you have to spend?  "))

def path(budget, aisles, aisle_choice, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket): 
    if aisle_choice in aisles and aisle_choice == "Food": 
        print("Going to {}!".format(aisle_choice))
        for key, value in food_shelf.items(): 
            print("{}: {}".format(key, value))
        item_choice = str(input("What would you like to put in your cart?    "))
        item_choice = item_choice.title()
        item_selection(budget, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, item_choice, aisle_choice)
    elif aisle_choice in aisles and aisle_choice == "Health": 
        print("Going to {}!".format(aisle_choice))
        for key, value in health_shelf.items(): 
            print("{}: {}".format(key, value))
        item_choice = str(input("What would you like to put in your cart?    "))
        item_choice = item_choice.title()
        item_selection(budget, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, item_choice, aisle_choice)
    elif aisle_choice in aisles and aisle_choice == "Cosmetics": 
        print("Going to {}!".format(aisle_choice))
        for key, value in cosmetic_shelf.items(): 
            print("{}: {}".format(key, value))
        item_choice = str(input("What would you like to put in your cart?    "))
        item_choice = item_choice.title()
        item_selection(budget, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, item_choice, aisle_choice)
    elif aisle_choice in aisles and aisle_choice == "Pets": 
        print("Going to {}!".format(aisle_choice))
        for key, value in pets_shelf.items(): 
            print("{}: {}".format(key, value))
        item_choice = str(input("What would you like to put in your cart?    "))
        item_choice = item_choice.title()
        item_selection(budget, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, item_choice, aisle_choice)
    elif aisle_choice in aisles and aisle_choice == "Checkout": 
        print("Going to {}!".format(aisle_choice))
        print("Your total is ${}".format(sum(price_of_basket)))
        payment = str(input("Would you like to pay Cash or Card?    "))
        payment = payment.title()
        if payment == "Cash": 
            cash_given = float(input("Please insert cash amount:    "))
            if cash_given > sum(price_of_basket): 
                remainder = cash_given - sum(price_of_basket)
                print("Here's your change of ${}. Thank you!".format(remainder))
                return
            else: 
                remainder = float(sum(price_of_basket)) - cash_given
              
            if remainder == 0: 
                print("Thank you!")
            
            while remainder > 0: 
                if remainder < 0.01: 
                    print("Thank you!")
                    return
                amount_remaining = float(input("Please insert remaining amount of ${}:   ".format(remainder)))
                if amount_remaining < remainder: 
                    remainder -= amount_remaining
                elif amount_remaining == remainder: 
                    print("Thank you!")
                    return
                elif remainder == 0: 
                    print("Thank you!")
                    return
                elif amount_remaining > remainder: 
                    change = amount_remaining - remainder
                    print("Here's your change of ${}. Thank you!".format(change))
                    return
        elif payment == "Card": 
            print("A charge of ${} has been placed on your card. Thank you!".format(sum(price_of_basket)))
            return
    else: 
        print("Please select an aisle")
        

def item_selection(budget, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, item_choice, aisle_choice): 
    if item_choice in food_shelf and item_choice != "Nothing": 
        basket_items.append(item_choice)
        price_of_basket.append(food_shelf.get(item_choice))
        if sum(price_of_basket) < budget:
            print("Adding {} to your cart".format(item_choice))
            print("Your current total is ${}".format(sum(price_of_basket)))
            return
        elif sum(price_of_basket) > budget:
            while sum(price_of_basket) > budget: 
                print("Your current total of ${} is over your budget of ${}".format(sum(price_of_basket), budget))
                print(" \t ".join(basket_items))
                removal_choice = str(input("What would you like to remove?    "))
                removal_choice = removal_choice.title()
                nope(budget, aisles, aisle_choice, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, removal_choice)
                return
    elif item_choice in health_shelf and item_choice != "Nothing": 
        basket_items.append(item_choice)
        price_of_basket.append(health_shelf.get(item_choice))
        if sum(price_of_basket) < budget:
            print("Adding {} to your cart".format(item_choice))
            print("Your current total is ${}".format(sum(price_of_basket)))
            return
        elif sum(price_of_basket) > budget:
            while sum(price_of_basket) > budget: 
                print("Your current total of ${} is over your budget of ${}".format(sum(price_of_basket), budget))
                print(" \t ".join(basket_items))
                removal_choice = str(input("What would you like to remove?    "))
                removal_choice = removal_choice.title()
                nope(budget, aisles, aisle_choice, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, removal_choice)
                return
    elif item_choice in cosmetic_shelf and item_choice != "Nothing": 
        basket_items.append(item_choice)
        price_of_basket.append(cosmetic_shelf.get(item_choice))
        if sum(price_of_basket) < budget:
            print("Adding {} to your cart".format(item_choice))
            print("Your current total is ${}".format(sum(price_of_basket)))
            return
        elif sum(price_of_basket) > budget:
            while sum(price_of_basket) > budget: 
                print("Your current total of ${} is over your budget of ${}".format(sum(price_of_basket), budget))
                print(" \t ".join(basket_items))
                removal_choice = str(input("What would you like to remove?    "))
                removal_choice = removal_choice.title()
                nope(budget, aisles, aisle_choice, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, removal_choice)
                return
    elif item_choice in pets_shelf and item_choice != "Nothing": 
        basket_items.append(item_choice)
        price_of_basket.append(pets_shelf.get(item_choice))
        if sum(price_of_basket) < budget:
            print("Adding {} to your cart".format(item_choice))
            print("Your current total is ${}".format(sum(price_of_basket)))
            return
        elif sum(price_of_basket) > budget:
            while sum(price_of_basket) > budget: 
                print("Your current total of ${} is over your budget of ${}".format(sum(price_of_basket), budget))
                print(" \t ".join(basket_items))
                removal_choice = str(input("What would you like to remove?    "))
                removal_choice = removal_choice.title()
                nope(budget, aisles, aisle_choice, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, removal_choice)
                return
    elif item_choice == "Nothing": 
        return("Leaving aisle")

        
def nope(budget, aisles, aisle_choice, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket, removal_choice): 
    if removal_choice in basket_items and removal_choice in food_shelf: 
        print("Removing {} from your cart".format(removal_choice))
        basket_items.remove(removal_choice)
        price_of_basket.remove(float(food_shelf.get(removal_choice)))
        print("Your new total is ${}".format(sum(price_of_basket)))
        return
    elif removal_choice in basket_items and removal_choice in health_shelf: 
        print("Removing {} from your cart".format(removal_choice))
        basket_items.remove(removal_choice)
        price_of_basket.remove(float(health_shelf.get(removal_choice)))
        print("Your new total is ${}".format(sum(price_of_basket)))
        return
    elif removal_choice in basket_items and removal_choice in cosmetic_shelf: 
        print("Removing {} from your cart".format(removal_choice))
        basket_items.remove(removal_choice)
        price_of_basket.remove(float(cosmetic_shelf.get(removal_choice)))
        print("Your new total is ${}".format(sum(price_of_basket)))
        return
    elif removal_choice in basket_items and removal_choice in pets_shelf: 
        print("Removing {} from your cart".format(removal_choice))
        basket_items.remove(removal_choice)
        price_of_basket.remove(float(pets_shelf.get(removal_choice)))
        print("Your new total is ${}".format(sum(price_of_basket)))
        return
    else: 
        print("Please choose something in your cart")
        return
    
while True: 
    print(" \t ".join(aisles))
    aisle_choice = str(input("Where would you like to go?    "))
    aisle_choice = aisle_choice.title() 
    path(budget, aisles, aisle_choice, food_shelf, health_shelf, cosmetic_shelf, pets_shelf, basket_items, price_of_basket)
    if aisle_choice == "Checkout": 
        break