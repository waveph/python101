"""
Main game file for Pong Game
Handles game initialization, game loop, collision detection, and scoring
"""
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Initialize game screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turn off auto-update for smooth animation

# Create game objects
r_paddle = Paddle((350, 0))    # Right paddle at x=350
l_paddle = Paddle((-350, 0))   # Left paddle at x=-350
ball = Ball()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")      # Right paddle up
screen.onkey(r_paddle.go_down, "Down")  # Right paddle down
screen.onkey(l_paddle.go_up, "w")       # Left paddle up
screen.onkey(l_paddle.go_down, "s")     # Left paddle down

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control game speed (dynamic)
    screen.update()              # Update screen with all changes
    ball.move()                  # Move ball to new position

    # Detect collision with top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()          # Reverse vertical direction

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()          # Reverse horizontal direction and increase speed

    # Detect when right player scores (ball passes left paddle)
    if ball.xcor() > 380:
        ball.reset_position()    # Reset ball to center
        scoreboard.l_point()     # Increase left player's score

    # Detect when left player scores (ball passes right paddle)
    if ball.xcor() < -380:
        ball.reset_position()    # Reset ball to center
        scoreboard.r_point()     # Increase right player's score

screen.exitonclick()