# Import the necessary classes from the turtle library.
from turtle import Turtle, Screen

# --- Turtle and Screen Setup ---
# Create a turtle object that will act as our pen.
tom = Turtle()
# Create a screen object to listen for keyboard input.
screen = Screen()

# --- Function Definitions ---
# These functions will be called when the user presses a key.
def move_forward():
    """Move the turtle forward by 10 pixels."""
    tom.forward(10)

def move_backward():
    """Move the turtle backward by 10 pixels."""
    tom.backward(10)

def clock_wise():
    """Turn the turtle to the right (clockwise) by 10 degrees."""
    tom.right(10)

def counter_clock_wise():
    """Turn the turtle to the left (counter-clockwise) by 10 degrees."""
    tom.left(10)

def clear_screen():
    """Clear the screen and return the turtle to the starting position."""
    tom.penup()
    tom.home()
    tom.clear()
    tom.pendown()

# --- Event Listeners ---
# Link specific keyboard keys to the functions defined above.
# The 'fun' argument tells the screen to call the function when the key is pressed.
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=counter_clock_wise)
screen.onkey(key="c", fun=clear_screen)

# --- Main Loop ---
# The screen will listen for events (key presses) until it is clicked.
screen.exitonclick()