# The MENU dictionary holds the recipes and costs for each drink.
# Each drink has 'ingredients' (a dictionary of required amounts) and a 'cost'.
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

# The resource dictionary tracks the current inventory of the machine.
# Each resource has a 'quantity' and a 'unit' for display purposes.
resources = {
    "water": {"quantity": 300, "unit": "ml"},
    "milk": {"quantity": 200, "unit": "ml"},
    "coffee": {"quantity": 100, "unit": "mg"},
    "money": {"quantity": 0, "unit": "$"}
}
