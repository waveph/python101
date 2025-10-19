# Import the data structures needed for the functions to operate.
from menu_resources import MENU, resources

def not_enough_resource(user_order):
    """
    Checks if there are insufficient resources to make the requested drink.
    Returns True if any ingredient is insufficient, otherwise False.
    """
    # Check for espresso ingredients.
    if user_order == 'espresso':
        if MENU["espresso"]["ingredients"]["water"] > resources["water"]["quantity"]:
            print("Sorry, we don't have enough water!")
            return True
        if MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]["quantity"]:
            print("Sorry, we don't have enough coffee!")
            return True

    # Check for latte ingredients.
    elif user_order == 'latte':
        if MENU["latte"]["ingredients"]["water"] > resources["water"]["quantity"]:
            print("Sorry, we don't have enough water!")
            return True
        if MENU["latte"]["ingredients"]["milk"] > resources["milk"]["quantity"]:
            print("Sorry, we don't have enough milk!")
            return True
        if MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]["quantity"]:
            print("Sorry, we don't have enough coffee")
            return True

    # Check for cappuccino ingredients.
    elif user_order == 'cappuccino':
        if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]["quantity"]:
            print("Sorry, we don't have enough water!")
            return True
        if MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]["quantity"]:
            print("Sorry, we don't have enough milk!")
            return True
        if MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]["quantity"]:
            print("Sorry, we don't have enough coffee")
            return True
    # If none of the above conditions were met, resources are sufficient.
    return False


def enough_resource(user_order):
    """
    Checks if there are enough resources to make the requested drink.
    Returns True only if ALL required ingredients are sufficient.
    """
    # Check for espresso ingredients (water and coffee).
    if user_order == 'espresso':
        if (MENU["espresso"]["ingredients"]["water"] < resources["water"]["quantity"] and
            MENU["espresso"]["ingredients"]["coffee"] < resources["coffee"]["quantity"]):
            return True
    # Check for latte ingredients (water, milk, and coffee).
    elif user_order == 'latte':
        if (MENU["latte"]["ingredients"]["water"] < resources["water"]["quantity"] and
                MENU["latte"]["ingredients"]["milk"] < resources["milk"]["quantity"] and
                MENU["latte"]["ingredients"]["coffee"] < resources["coffee"]["quantity"]):
            return True
    # Check for cappuccino ingredients (water, milk, and coffee).
    elif user_order == 'cappuccino':
        if (MENU["cappuccino"]["ingredients"]["water"] < resources["water"]["quantity"] and
        MENU["cappuccino"]["ingredients"]["milk"] < resources["milk"]["quantity"] and
        MENU["cappuccino"]["ingredients"]["coffee"] < resources["coffee"]["quantity"]):
            return True

def update_resource(user_order):
    """
    Updates the global 'resources' dictionary by subtracting the ingredients
    used for the given drink and adding the money earned.
    """
    # Deduct resources for an espresso.
    if user_order == 'espresso':
        resources["water"]["quantity"] = resources["water"]["quantity"] - 50
        resources["coffee"]["quantity"] = resources["coffee"]["quantity"] - 18
        resources["money"]["quantity"] = resources["money"]["quantity"] + 1.50
    # Deduct resources for a latte.
    elif user_order == 'latte':
        resources["water"]["quantity"] = resources["water"]["quantity"] - 200
        resources["milk"]["quantity"] = resources["milk"]["quantity"] - 150
        resources["coffee"]["quantity"] = resources["coffee"]["quantity"] - 24
        resources["money"]["quantity"] = resources["money"]["quantity"] + 2.50
    # Deduct resources for a cappuccino.
    elif user_order == 'cappuccino':
        resources["water"]["quantity"] = resources["water"]["quantity"] - 250
        resources["milk"]["quantity"] = resources["milk"]["quantity"] - 100
        resources["coffee"]["quantity"] = resources["coffee"]["quantity"] - 24
        resources["money"]["quantity"] = resources["money"]["quantity"] + 3.00