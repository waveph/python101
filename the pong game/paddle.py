"""
Paddle class for Pong Game
Handles paddle creation and movement controls
"""
from turtle import Turtle


class Paddle(Turtle):
    """Represents a player paddle with vertical movement controls"""

    def __init__(self, position):
        """Initialize paddle at specified position with size and appearance"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Make paddle taller
        self.penup()
        self.goto(position)  # Move to starting position

    def go_up(self):
        """Move paddle upward by 20 pixels"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move paddle downward by 20 pixels"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)