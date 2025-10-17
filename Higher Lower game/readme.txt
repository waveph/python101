# Higher Lower Game

A fun and interactive command-line game inspired by the "Higher Lower" web challenge. The player is presented with two entities and must guess which one has more Instagram followers. The game continues until the player makes an incorrect guess.

## Features

-   **Randomized Comparisons:** Uses `random.sample()` to select two unique entities for each round, ensuring no repeats in a single round.
-   **Data Handling:** Works with a complex data structure (a list of dictionaries) to store and access entity information.
-   **Input Validation:** Robustly checks for user input to ensure only 'a' or 'b' are accepted, preventing crashes from bad input.
-   **Score Tracking:** Keeps track of the player's current score and displays it at the beginning of each round.
-   **Game Flow Logic:** Correctly ends the game immediately upon the first wrong answer.

## How to Run

1.  Make sure you have Python installed on your system.
2.  You will need the `art` package. Install it with pip:
    ```bash
    pip install art
    ```
3.  Save the code as a Python file (e.g., `higher_lower.py`).
4.  Run the script from your terminal:
    ```bash
    python higher_lower.py
    ```
5.  Follow the on-screen prompts to play!

## What I Learned

This project was a fantastic exercise in:
-   **Working with Dictionaries:** Accessing data within a list of dictionaries using keys (e.g., `item_a['follower_count']`).
-   **Python's `random` Module:** Using `random.sample()` to select multiple unique items from a list.
-   **Input Validation:** Using a `while` loop to ensure the user provides valid input before proceeding.
-   **Conditional Logic:** Combining multiple conditions in a single `if` statement to check for a correct answer.
-   **Game Loop Control:** Using the `break` statement to exit the main game loop when the player loses.

---

## ⚠️ Learning Project Disclaimer

This is a project from my Python automation learning journey. The code is a reflection of my progress and is not intended to be a final, production-ready application. It was built to practice specific concepts and may contain "messy" or inefficient code as part of the learning process.