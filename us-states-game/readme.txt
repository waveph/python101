# 🗺 U.S. States Guessing Game

An interactive geographical quiz built with Python’s `turtle` graphics and `pandas` libraries. The game challenges players to name all 50 U.S. states by typing their names, dynamically displaying each correct guess on a blank map. Designed to strengthen data handling and coordinate mapping skills while combining visualization and user interaction.

## 🎮 Features

- Interactive Gameplay: Players type in state names and see them appear directly on the U.S. map in real time.
- Dynamic Score Tracking: Displays live progress (e.g., “23/50 States Correct”).
- Data-Driven Logic: Uses `pandas` to read state names and coordinates from a CSV file.
- Learning Mode: If the user exits early, the program automatically generates a `states_to_learn.csv` file containing the states that were not guessed.
- Turtle Graphics Integration: Leverages the `turtle` module to render the map, handle coordinates, and draw state names at accurate positions.
- Clean Structure: Organized logic for user input validation, data processing, and graphical updates.

## 🧩 How to Run

1. Make sure you have Python 3 installed on your system.
2. Place all files in the same directory:
   - main.py
   - 50_states.csv
   - blank_states_img.gif
3. Run the program from your terminal:
   python main.py
4. Type in the name of a U.S. state (e.g., Texas, California, New York).
5. To exit the game and save your progress, type: Exit
   This will create a file called states_to_learn.csv listing the states you missed.

## 🧭 Project Context

This project represents the transition point where I moved from basic logic-based coding toward data-oriented automation and graphical applications.
It demonstrates my ability to combine data processing, user interaction, and visual feedback in a cohesive and functional program.

## 📂 Project Files

| File | Description |
|------|--------------|
| main.py | Core game logic and user interaction loop |
| 50_states.csv | Contains all state names and coordinates |
| blank_states_img.gif | Map image used as the game background |
| states_to_learn.csv | Generated automatically — lists unguessed states |

## 🪶 Project Note

This project is part of my Python Automation roadmap.
It represents my independent progress and hands-on experience combining logic, data manipulation, and visualization in Python.
