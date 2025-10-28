"""
Car Manager class for Turtle Crossing Game
Handles car generation, movement, and difficulty progression
"""
from turtle import Turtle
import random

# Game constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # Initial car speed
MOVE_INCREMENT = 10  # Speed increase per level


class CarManager:
    """Manages all cars in the game including creation and movement"""

    def __init__(self):
        """Initialize car manager with empty car list and starting speed"""
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Current car speed

    def create_car(self):
        """Randomly create new cars with 1 in 5 chance each frame"""
        random_chance = random.randint(1, 5)
        if random_chance == 1:  # 20% chance to create a car each frame
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))  # Random color
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make car rectangular
            random_y = random.randint(-250, 250)  # Random lane position
            new_car.goto(300, random_y)  # Start at right edge of screen
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars leftward across the screen"""
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move cars toward left

    def level_up(self):
        """Increase car speed when player advances to next level"""
        self.car_speed += MOVE_INCREMENT