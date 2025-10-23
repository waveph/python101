# Interactive Turtle Applications

A collection of two interactive applications built with Python's `turtle` library. These projects demonstrate a strong understanding of event-driven programming, state management, and user interaction.

## Projects

### 1. Turtle Race Game

A classic racing simulation where multiple turtles compete to cross the finish line. The user places a bet, and the program announces the winner.

**Features:**
-   **Dynamic Turtle Creation:** Programmatically creates and positions multiple turtle objects.
-   **User Input:** Takes user input at the start to place a bet.
-   **State Management:** Tracks the state of the race and determines a winner.
-   **Random Movement:** Each turtle moves a random distance in each step, simulating a real race.

### 2. Etch-A-Sketch

A digital recreation of the classic Etch-A-Sketch toy. The user can control a turtle on the screen using keyboard inputs to draw lines and shapes.

**Features:**
-   **Event Listeners:** Uses the `screen.onkey()` method to bind keyboard keys to specific functions.
-   **Control Functions:** Provides functions for movement (forward/backward), turning (clockwise/counter-clockwise), and clearing the screen.
-   **Real-Time Interaction:** The turtle responds instantly to user input, providing immediate visual feedback.

## How to Run

1.  Make sure you have Python installed on your system.
2.  Ensure you have the `turtle` library, which comes pre-installed with most Python distributions.
3.  Save the code for each project into its own Python file (e.g., `turtle_race.py`, `etch_a_sketch.py`).
4.  Run a script from your terminal:
    ```bash
    python turtle_race.py
    ```
5.  Follow the on-screen prompts or use the keyboard controls to interact with the application.

## What I Learned

These projects were a pivotal exercise in:
-   **Event-Driven Programming:** Understanding how to write programs that react to user input, a core concept in GUIs and web development.
-   **State Management:** Tracking the state of an application (e.g., the race is over) and changing behavior based on that state.
-   **Object-Oriented Programming:** Creating and managing multiple objects (turtles) in a single application.
-   **API Design:** Designing a simple API for the Etch-A-Sketch app (e.g., the set of functions like `move_forward`).

---

## Project Disclaimer

These projects are a snapshot of my skills at a specific point in time. They serve as a key milestone in my journey, demonstrating my ability to build interactive applications and manage user input and state. The focus here is on making applications that are dynamic and responsive to user actions.