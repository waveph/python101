# Import the logo for display and all custom functions from the 'functions' module.
from logo import logo
from functions import not_enough_resource
from functions import enough_resource
from functions import update_resource
# Import the data structures for the menu and available resources.
from menu_resources import MENU, resources

# Display the coffee machine logo at the start of the program.
print(logo)

# 'game' is a flag that controls the main operational loop of the coffee machine.
game = True
while game:
    # This inner loop handles the initial user input for their drink choice.
    # It continues until a valid command is entered.
    while True:
        try:
            # Prompt the user for their order and standardize the input.
            user_order = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

            # Validate the user's input against the list of valid commands.
            if (user_order != "espresso"
                    and user_order != "latte"
                    and user_order != "cappuccino"
                    and user_order != "report"
                    and user_order != "off"):
                print("Wrong input")
            else:
                # If the input is valid, break out of the input validation loop.
                break
        except NameError:
            # This except block is likely unreachable but is kept for robustness.
            print("Please enter a valid order! (espresso/latte/cappuccino)")

    # Handle the 'report' command to display current resource levels.
    if user_order == "report":
        print(f"Water: {resources['water']['quantity']}{resources['water']['unit']}")
        print(f"Milk: {resources['milk']['quantity']}{resources['milk']['unit']}")
        print(f"Coffee: {resources['coffee']['quantity']}{resources['coffee']['unit']}")
        print(f"Money: {resources['money']['unit']}{resources['money']['quantity']}")

    # Check if there are enough resources to make the requested drink.
    # The not_enough_resource function returns True if any ingredient is insufficient.
    if not_enough_resource(user_order) == True:
        print("Sorry, cannot make your drink. Resources insufficient.")
        # Set 'game' to False to shut down the machine.
        game = False
        # 'continue' skips the rest of the loop and starts the next iteration.
        continue

    # Check if there are enough resources (this function is somewhat redundant with the one above).
    if enough_resource(user_order) == True:
        print("Insert your coins.")
        # A series of loops to process each type of coin, with input validation.
        while True:
            try:
                quarters = float(input("How many quarters?: "))
                break
            except ValueError:
                    print("Please insert only coins! 🪙")

        while True:
            try:
                dimes = float(input("How many dimes?: "))
                break
            except ValueError:
                    print("Please insert only coins! 🪙")

        while True:
            try:
                nickles = float(input("How many nickles?: "))
                break
            except ValueError:
                    print("Please insert only coins! 🪙")

        while True:
            try:
                pennies = float(input("How many pennies?: "))
                break
            except ValueError:
                    print("Please insert only coins! 🪙")

        # Calculate the total amount of money inserted by the user.
        sum = float(quarters * 0.25  + dimes * 0.10  + nickles * 0.05  + pennies * 0.01)

    # Handle the 'off' command to turn off the machine.
    if user_order == "off":
        game = False
    # Handle the 'espresso' order.
    elif user_order == 'espresso':
        # Check if the inserted money is enough to cover the cost.
        if sum < MENU["espresso"]["cost"]:
            print("Sorry, not enough money! insert more.")
        else:
            # Calculate and give back change.
            difference = sum - MENU["espresso"]["cost"]
            print(f"Here is ${difference:.2f} in change.")
            print("Here is your espresso ⋆.˚☕︎ Enjoy!")
    # Handle the 'latte' order.
    elif user_order == 'latte':
        if sum < MENU["latte"]["cost"]:
            print("Sorry, not enough money! insert more.")
        else:
            difference = sum - MENU["latte"]["cost"]
            print(f"Here is ${difference:.2f} in change.")
            print("Here is your latte ☕︎︎ Enjoy!")
    # Handle the 'cappuccino' order.
    elif user_order == 'cappuccino':
        if sum < MENU["cappuccino"]["cost"]:
            print("Sorry, not enough money! insert more.")
        else:
            difference = sum - MENU["cappuccino"]["cost"]
            print(f"Here is ${difference:.2f} in change.")
            print("Here is your cappuccino ˗ˏˋ☕ˎˊ˗︎ Enjoy!")

    # After a successful transaction, update the resource quantities.
    update_resource(user_order)