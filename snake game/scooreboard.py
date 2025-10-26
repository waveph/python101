"""
Scoreboard class for Snake Game
Handles score display and game over messages
"""
from turtle import Turtle

# Display constants
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    """Manages game scoring and display"""

    def __init__(self):
        """Initialize scoreboard with starting score and position"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)  # Position at top of screen
        self.update_score()
        self.hideturtle()  # Hide the turtle cursor

    def update_score(self):
        """Update the score display on screen"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase score by 1 and update display"""
        self.score += 1
        self.clear()  # Clear previous score
        self.update_score()