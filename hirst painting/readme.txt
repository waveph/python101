# Hirst Dot Painting Generator

A Python program that generates beautiful, colorful dot matrix art inspired by the artist Damien Hirst. Using Python's `turtle` graphics library, this script creates a 10x10 grid of dots, with each dot colored randomly from a curated palette extracted from an image.

## Features

-   **Generative Art:** Creates a unique piece of art every time it runs, thanks to the random color selection.
-   **Grid-Based Layout:** Uses nested `for` loops to precisely position dots in a clean 10x10 grid.
-   **Color Palette:** Utilizes a pre-extracted list of RGB color tuples to ensure a harmonious and visually appealing color scheme.
-   **Clean Graphics:** Properly manages the turtle's state with `penup()` and `pendown()` to draw dots without connecting lines.
-   **Interactive:** The canvas window remains open until the user clicks on it, allowing time to view the result.

## How to Run

1.  Make sure you have Python installed on your system.
2.  Ensure you have the `turtle` library, which comes pre-installed with most Python distributions.
3.  Save the code as a Python file (e.g., `hirst_painting.py`).
4.  Run the script from your terminal:
    ```bash
    python hirst_painting.py
    ```
5.  A new window will appear with the generated art. Click on the window to close it.

## What I Learned

This project was a fun and creative exercise in:
-   **Nested Loops:** Using a `for` loop inside another `for` loop to create a two-dimensional grid.
-   **Coordinate System:** Managing `(x, y)` coordinates to position elements precisely on the canvas.
-   **State Management:** Using `penup()` and `pendown()` to control the turtle's drawing state between movements.
-   **Data Structures:** Working with a list of tuples to store and retrieve color data.
-   **Randomization:** Using the `random` module to introduce variability and uniqueness to the output.

---

## Project Disclaimer

This project is a creative exploration of generative art. It serves as a fun and practical application of fundamental programming concepts like loops and coordinates, demonstrating how code can be used as a medium for artistic expression.