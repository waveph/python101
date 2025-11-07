"""
Main game file for Turtle Crossing Game
Handles game initialization, game loop, collision detection, and level progression
"""
import time
from turtle import Screen
import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off auto-update for smooth animation

# Create game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(player.go_up, "Up")  # Move player turtle upward

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Control game speed
    screen.update()  # Update screen with all changes

    car_manager.create_car()  # Randomly generate new cars
    car_manager.move_cars()  # Move all existing cars

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()  # End game if player hits a car

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()  # Reset player position
        car_manager.level_up()  # Increase car speed
        scoreboard.increase_level()  # Increase level display

screen.exitonclick()