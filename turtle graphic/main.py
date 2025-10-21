from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.pensize(15)

colors = ["red", "blue", "green", "yellow", "purple", "orange",
          "pink", "cyan", "magenta", "lime", "gold", "coral",
          "teal", "navy", "violet", "maroon", "silver", "gray",
          "brown", "black"]

walk = [0, 90, 180, 270]


for i in range(200):
    tim.forward(30)
    tim.pencolor(random.choice(colors))
    tim.setheading(random.choice(walk))
    tim.speed("fastest")


screen.exitonclick()