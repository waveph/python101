"""
Ball class for Pong Game
Handles ball movement, bouncing, and reset logic
"""
from turtle import Turtle


class Ball(Turtle):
    """Represents the game ball with movement and collision behavior"""

    def __init__(self):
        """Initialize ball with starting position, movement values, and speed"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10  # Horizontal movement per frame
        self.y_move = 10  # Vertical movement per frame
        self.move_speed = 0.1  # Initial game speed (time between frames)

    def move(self):
        """Move ball to new position based on current movement values"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse vertical direction (when hitting top/bottom walls)"""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse horizontal direction and increase speed (when hitting paddles)"""
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase speed by reducing sleep time

    def reset_position(self):
        """Reset ball to center and restore initial speed"""
        self.goto(0, 0)
        self.move_speed = 0.1  # Reset to initial speed
        self.bounce_x()  # Start moving toward opposite player