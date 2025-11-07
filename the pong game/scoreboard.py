"""
Scoreboard class for Pong Game
Handles score tracking and display for both players
"""
from turtle import Turtle


class Scoreboard(Turtle):
    """Manages and displays scores for both players"""

    def __init__(self):
        """Initialize scoreboard with zero scores and set up display"""
        super().__init__()
        self.hideturtle()  # Hide the turtle cursor
        self.color('white')
        self.penup()
        self.l_score = 0  # Left player score
        self.r_score = 0  # Right player score
        self.update_scoreboard()  # Display initial scores

    def update_scoreboard(self):
        """Update the score display on screen"""
        self.clear()  # Clear previous scores
        self.goto(-100, 200)  # Position for left score
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)  # Position for right score
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        """Increase left player's score and update display"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increase right player's score and update display"""
        self.r_score += 1
        self.update_scoreboard()