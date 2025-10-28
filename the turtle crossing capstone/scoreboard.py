"""
Scoreboard class for Turtle Crossing Game
Handles level tracking and game over display
"""
from turtle import Turtle

# Display constants
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Manages and displays game level and game over messages"""

    def __init__(self):
        """Initialize scoreboard with starting level and display setup"""
        super().__init__()
        self.level = 1  # Current game level
        self.hideturtle()  # Hide the turtle cursor
        self.penup()
        self.goto(-280, 260)  # Position in top-left corner
        self.update_scoreboard()  # Display initial level

    def update_scoreboard(self):
        """Update the level display on screen"""
        self.clear()  # Clear previous level display
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase level by 1 and update display"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display game over message in center of screen"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="left", font=FONT)