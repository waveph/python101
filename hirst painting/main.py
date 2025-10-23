# Import the necessary classes from the turtle library.
from turtle import Turtle, Screen
import random

# --- Turtle and Screen Setup ---
# Create a turtle object for drawing.
tom = Turtle()
tom.pensize(20)
tom.hideturtle()
tom.speed("fastest")

# Create the screen object for our canvas.
screen = Screen()
screen.setup(700,700)
# Set the color mode to accept RGB values from 0-255.
screen.colormode(255)
# Set the background color to black for better contrast.
screen.bgcolor("black")

# --- Color Data ---
# A pre-extracted list of RGB color tuples to be used for the dots.
# This is more efficient than extracting colors every time the program runs.
color_list = [(234, 220, 96), (174, 81, 22), (236, 48, 85), (233, 162, 89), (69, 187, 230),
              (171, 54, 106), (250, 54, 16), (93, 197, 129), (231, 128, 155),
              (111, 218, 246), (123, 233, 208), (19, 126, 212), (51, 121, 41),
              (249, 222, 0), (22, 178, 214), (247, 144, 156), (54, 177, 84), (83, 24, 34),
              (95, 39, 18), (29, 88, 36), (187, 23, 13), (30, 65, 37), (186, 18, 32),
              (245, 160, 151), (178, 135, 38), (254, 5, 18), (37, 128, 230), (255, 9, 5), (126, 88, 0)]

# --- Main Drawing Logic ---
# Set the initial color for the turtle's pen (not the dots).
tom.color("black")
# Set the starting y-coordinate for the first row of dots.
y_position = -200

# The outer loop iterates through each row.
for i in range(10):
    # Set the starting x-coordinate for the first dot in the current row.
    x_position = -200
    # The inner loop iterates through each column within the current row.
    for j in range(10):
        # Move the turtle to the correct starting position for the dot.
        tom.goto(x_position, y_position)
        # Lower the pen to the canvas to start drawing.
        tom.pendown()
        # Choose a random color from our list for the current dot.
        # tom.color(random.choice(color_list))
        # Draw a dot with a diameter of 20.
        tom.dot(20, random.choice(color_list))
        # Lift the pen up to move to the next position without drawing a line.
        tom.penup()
        # Increment the x-coordinate to move to the next column.
        x_position += 50
    # After completing a row, increment the y-coordinate to move to the next row.
    y_position += 50

# --- Final Step ---
# Keep the window open until it is clicked.
screen.exitonclick()