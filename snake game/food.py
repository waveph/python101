"""
Food class for Snake Game
Handles food appearance and random positioning
"""
from turtle import Turtle
import random as rd


class Food(Turtle):
    """Represents the food that the snake eats to grow and score points"""

    COUNTER = 0  # Class variable to track total food created

    def __init__(self):
        """Initialize food with random position and appearance"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Make circle smaller
        self.color("orange")
        self.speed("fastest")  # Instant movement
        self.refresh()

    def refresh(self):
        """Move food to random position on screen"""
        random_x = rd.randint(-280, 280)
        random_y = rd.randint(-280, 280)
        self.goto(random_x, random_y)

    def counter(self):
        """Track food consumption count (currently unused in main game)"""
        if self.refresh():
            self.COUNTER += 1