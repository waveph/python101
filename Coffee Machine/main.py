from operator import contains

from logo import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": {"quantity": 300, "unit": "ml"},
    "milk": {"quantity": 200, "unit": "ml"},
    "coffee": {"quantity": 100, "unit": "mg"},
    "money": {"quantity": 0, "unit": "$"}
}



print(logo)

user_order = input("“What would you like? (espresso/latte/cappuccino): ")

if user_order == 'espresso':
    if (MENU["espresso"]["ingredients"]["water"] < resources["water"]["quantity"] or
            MENU["espresso"]["ingredients"]["coffee"] < resources["coffee"]["quantity"]):
        print("Sorry, you don't have enough resources")
elif user_order == 'latte':
    if (MENU["latte"]["ingredients"]["water"] < resources["water"]["quantity"] or
            MENU["latte"]["ingredients"]["milk"] < resources["milk"]["quantity"] or
            MENU["latte"]["ingredients"]["coffee"] < resources["coffee"]["quantity"]):
        print("Sorry, you don't have enough resources")
elif user_order == 'cappuccino':
    if (MENU["cappuccino"]["ingredients"]["water"] < resources["water"]["quantity"] or
            MENU["cappuccino"]["ingredients"]["milk"] < resources["milk"]["quantity"] or
            MENU["cappuccino"]["ingredients"]["coffee"] < resources["coffee"]["quantity"]):
        print("Sorry, you don't have enough resources")

# TODO: 1. Print report of all coffee machine resources
if user_order == "report":
    print(f"Water: {resources['water']['quantity']}{resources['water']['unit']}")
    print(f"Milk: {resources['milk']['quantity']}{resources['milk']['unit']}")
    print(f"Coffee: {resources['coffee']['quantity']}{resources['coffee']['unit']}")
    print(f"Money: {resources['money']['unit']}{resources['money']['quantity']}")



