# Import the necessary classes from the turtle library.
import turtle
from turtle import Turtle, Screen
import random

# --- Setup ---
# Create a screen object to act as our canvas.
screen = Screen()
screen.setup(500, 400)
# Prompt the user to place a bet on which turtle will win.
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
# A list of color strings to assign to each turtle.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# An empty list to hold all of our turtle objects.
all_turtles = []

# --- Turtle Creation ---
# Set the starting y-coordinate for the first turtle.
y = -120
# Loop 6 times to create 6 turtles.
for turtle_index in range(0, 6):
    # Create a new turtle object.
    new_turtle = Turtle("turtle")
    # Assign a unique color from the list to each turtle.
    new_turtle.color(colors[turtle_index])
    # Lift the pen to move to the starting position without drawing.
    new_turtle.penup()
    # Position the turtle at the starting line.
    new_turtle.goto(x= -230, y= y)
    # Increment the y-coordinate for the next turtle.
    y += 50
    # Add the newly created turtle to our list.
    all_turtles.append(new_turtle)

# --- Race Logic ---
# A flag to control the main race loop.
is_race_one = True

# The main loop continues as long as the race is active.
while is_race_one:
    # Iterate through each turtle in the race.
    for turtle in all_turtles:
        # Check if any turtle has crossed the finish line (xcor > 230).
        if turtle.xcor() > 230:
            # The race is over, so set the flag to False to stop the loop.
            is_race_one = False
            # Get the color of the winning turtle.
            winning_color = turtle.pencolor()
            # Compare the winning color to the user's bet and print the result.
            if winning_color == user_bet:
                print(f"You've win! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        # Make each turtle move a random distance forward in each step of the loop.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# --- End of Game ---
# Keep the window open until the user clicks on it.
screen.exitonclick()