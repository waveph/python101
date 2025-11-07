"""
Player class for Turtle Crossing Game
Handles player turtle movement and position tracking
"""
from turtle import Turtle

# Game constants
STARTING_POSITION = (0, -280)  # Bottom center of screen
MOVE_DISTANCE = 10  # Pixels to move per key press
FINISH_LINE_Y = 280  # Y-coordinate for successful crossing


class Player(Turtle):
    """Represents the player-controlled turtle"""

    def __init__(self):
        """Initialize player turtle with starting position and appearance"""
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)  # Face upward
        self.go_to_start()  # Move to starting position

    def go_up(self):
        """Move player upward by MOVE_DISTANCE pixels"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Reset player to starting position at bottom of screen"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if player has reached the top finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False