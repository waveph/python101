# Import the necessary classes from the custom modules.
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import logo

# Display the coffee machine logo at the start of the program.
print(logo.logo)

# --- Create Instances of Our Objects ---
# Create a CoffeeMaker object to handle the machine's resources and actions.
my_machine = CoffeeMaker()
# Create a MoneyMachine object to handle all financial transactions.
payments = MoneyMachine()
# Create a Menu object to access the drink menu and find items.
drink = Menu()

# 'making' is the main flag that controls the entire coffee machine's operational loop.
making = True
while making:
    # 'game' is a flag for the inner loop that handles user input validation.
    game = True
    while game:
        try:
            # Prompt the user to enter their order.
            order = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
            # Validate the user's input against the list of accepted commands.
            if (order != "espresso"
                    and order != "latte"
                    and order != "cappuccino"
                    and order != "report"
                    and order != "off"):
                print("wrong input")
            else:
                # If the input is valid, break out of the validation loop.
                break
        except NameError:
            # This except block is likely unreachable but serves as a fallback for robustness.
            print("You didn't select a valid order, try again.")

    # Handle the 'off' command to shut down the machine.
    if order == "off":
        # Set the main flag to False to exit the outer loop and end the program.
        break

    # Handle the 'report' command to print current resource and money reports.
    if order == "report":
        # Call the report method on the CoffeeMaker and MoneyMachine objects.
        my_machine.report()
        payments.report()
        # Use 'continue' to skip the rest of the loop and ask for a new order.
        continue

    # --- The Main Order Fulfillment Process ---
    # Check if the machine has enough resources to make the requested drink.
    # The find_drink method returns a MenuItem object for the given order name.
    if not my_machine.is_resource_sufficient(drink.find_drink(order)):
        # A 'continue' here allow for a new order.
        continue

    # Process the payment for the drink.
    # The 'value' flag controls the payment input loop.
    value = True
    while value:
        try:
            # Call the make_payment method, passing the cost of the drink.
            # This method will handle all coin processing and validation.
            payments.make_payment(drink.find_drink(order).cost)
            # If payment is successful, break out of the payment loop.
            break
        except ValueError:
            # If the user enters invalid input for coins, prompt them again.
            print("Please enter valid coins!")

    # If payment was successful, make the coffee.
    # The make_coffee method will deduct the resources from the machine.
    my_machine.make_coffee(drink.find_drink(order))