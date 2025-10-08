# Import necessary modules for the logo and mathematical operations (though math isn't used, it's good practice)
import math
import logo


# --- Function Definitions ---

def operation():
    """
    Asks the user to pick an operation from the predefined list.
    It will keep asking until a valid operation (+, -, *, /) is entered.
    Returns:
        str: The valid operation symbol chosen by the user.
    """
    while True:
        the_operation = input('Pick an operation: ').strip()
        if the_operation in operations:
            return the_operation  # Return the valid operation to where the function was called
        print('Invalid input. Try again.')


def calculation(first_number, the_next_number, the_operation):
    """
    Performs a single calculation based on the two numbers and the operation provided.
    Args:
        first_number (float): The first number in the calculation.
        the_next_number (float): The second number in the calculation.
        the_operation (str): The operation symbol (+, -, *, /).
    Returns:
        float: The result of the calculation.
    """
    if the_operation == '+':
        return first_number + the_next_number
    elif the_operation == '-':
        return first_number - the_next_number
    elif the_operation == '*':
        return first_number * the_next_number
    else:
        return first_number / the_next_number


# --- Main Program Execution ---

# Print the ASCII art logo at the start
print(logo.logo())

# Initialize global variables to manage the program's state
decision = ''  # Stores whether the user wants to continue ('y') or start over ('n')
operations = ('+', '-', '*', '/')  # A tuple of valid operation symbols
result = 0  # Stores the result of the latest calculation

# This is the main loop for the entire calculator program.
# It allows the user to perform completely new calculations.
while True:
    # --- Step 1: Get the first set of inputs for a new calculation ---
    first_number = float(input('What is the first number?: '))
    print('+\n''-\n''*\n''/')

    # --- Step 2: Get the operation and the second number ---
    the_operation = operation()  # Call the function to get a valid operation
    the_next_number = float(input("What\'s the next number?: "))

    # --- Step 3: Perform the first calculation ---
    result = calculation(first_number, the_next_number, the_operation)

    # --- Step 4: Show the result and ask for user's decision ---
    print(f'{first_number} {the_operation} {the_next_number} = {result:.2f}')
    decision = input(f"Type 'y' to continue with {result:.2f} or type 'n' to start a new calculation: ").strip().lower()

    # --- Step 5: Handle the user's decision ---
    if decision == 'y':
        # This nested loop handles continuous calculations from the previous result
        while decision == 'y':
            # The previous result becomes the first number for the next calculation
            first_number = result

            # Get the next operation and number
            the_operation = operation()
            the_next_number = float(input("What's the next number?: "))

            # Perform the new calculation using the running total
            result = calculation(first_number, the_next_number, the_operation)

            # Show the new result and ask again
            print(f'{first_number:.2f} {the_operation} {the_next_number} = {result:.2f}')
            decision = input(
                f"Type 'y' to continue with {result:.2f} or type 'n' to start a new calculation: ").strip().lower()

        # If the user decides not to continue in the nested loop, break out of the main loop
        if decision == 'n':
            break

    # If the user decides to start a new calculation from the beginning, break the main loop
    elif decision == 'n':
        break