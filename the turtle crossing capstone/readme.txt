Turtle Crossing Game
====================

A Python game built with Turtle graphics where the player controls a turtle trying to cross a busy road filled with moving cars.

Game Description
----------------
The player controls a turtle that starts at the bottom of the screen and must navigate through traffic to reach the top. With each successful crossing, the game level increases and cars move faster, making it progressively more challenging.

Features
--------
* Player-controlled turtle movement
* Randomly generated colored cars
* Progressive difficulty (cars speed up each level)
* Collision detection system
* Level tracking and display
* Game over screen

Files Structure
---------------
main.py        - Main game loop and coordination
player.py      - Player turtle class and movement
car_manager.py - Car generation, movement, and level progression  
scoreboard.py  - Level tracking and game over display

How to Play
-----------
1. Run `python main.py` to start the game
2. Use the UP arrow key to move the turtle forward
3. Avoid the colored cars moving across the screen
4. Reach the top of the screen to advance to the next level
5. Each level increases the speed of the cars
6. Game ends if the turtle collides with any car

Controls
--------
UP ARROW - Move turtle forward

Technical Details
-----------------
* Built with Python Turtle graphics module
* Object-Oriented Programming architecture
* Center-point collision detection system
* Random car generation with color variation
* Dynamic difficulty scaling

Requirements
------------
* Python 3.x
* Turtle module (standard library)

Game Rules
----------
* Start at level 1 with slow-moving cars
* Each successful crossing increases level by 1
* Car speed increases with each level
* Collision with any car ends the game
* No time limit - focus on safe crossing!

## Project Disclaimer

This project is a key milestone in my learning journey. It serves as a capstone for the "Game Development" section of my course. It demonstrates my ability to combine multiple concepts into a single, cohesive application. It is a testament to my progress and my readiness to tackle more complex projects involving APIs and web frameworks.