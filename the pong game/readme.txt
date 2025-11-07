# Pong Game

A classic arcade-style Pong game built with Python's `turtle` library. This project demonstrates a strong understanding of event-driven programming, object-oriented programming, and real-time graphics rendering. It serves as a capstone for the "Game Development" section of my learning journey, showcasing my ability to manage game state, handle user input, and implement collision detection.

## Features

-   **Two-Player Gameplay:** Implements controls for two paddles, allowing for competitive two-player action.
-   **Real-Time Graphics:** Uses the `screen.tracer(0)` for smooth animation and `time.sleep()` for consistent game speed.
-   **Collision Detection:** Includes logic for both wall collisions (top/bottom) and paddle/ball collisions.
-   **Scoring System:** A `Scoreboard` class manages the score for both players.
-   **Object-Oriented Design:** Uses separate classes for `Paddle`, `Ball`, and `Scoreboard` to keep the code clean and maintainable.

## How to Run

1.  Make sure you have Python and the `turtle` library.
2.  Ensure all four files (`main.py`, `paddle.py`, `ball.py`, `scoreboard.py`) are in the same directory.
3.  Run the main script from your terminal:
    ```bash
    python main.py`
    ```
4.  Use the arrow keys to control the paddles. Press 'c' to close the game.

## What I Learned

This project was a pivotal exercise in my journey from a scripter to an application developer. It taught me the fundamental principles of game development:
-   **Game Loop:** The importance of a main loop that updates state and renders the game state.
-   **State Management:** How to manage the state of an application and trigger events.
- **Event-Driven Programming:** How to use `screen.onkey()` to link user input to functions.
- **Collision Detection:** Implementing algorithms to detect when objects intersect in 2D space.

---

## Project Disclaimer

This project is a key milestone in my learning journey. It serves as a capstone for the "Game Development" section of my course. It demonstrates my ability to combine multiple concepts into a single, cohesive application. It is a testament to my progress and my readiness to tackle more complex projects involving APIs and web frameworks.


