from turtle import Turtle
import random as rd

class Food(Turtle):
    COUNTER = 0

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = rd.randint(-280, 280)
        random_y = rd.randint(-280, 280)
        self.goto(random_x, random_y)

    def counter(self):
        if self.refresh():
            self.COUNTER += 1