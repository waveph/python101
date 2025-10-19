# OOP Coffee Machine

A sophisticated, object-oriented command-line simulation of a professional coffee machine. This project demonstrates a clean separation of concerns by using distinct classes to manage the machine's resources, financial transactions, and menu. The main application serves as an orchestrator, coordinating these objects to fulfill drink orders.

## Features

-   **Object-Oriented Design:** Built with a clean OOP architecture using `CoffeeMaker`, `MoneyMachine`, and `Menu` classes.
-   **Separation of Concerns:** Each class has a single responsibility (e.g., `MoneyMachine` only handles payments), making the code modular, maintainable, and easy to understand.
-   **Resource Management:** The `CoffeeMaker` object tracks ingredient levels and prevents orders when resources are insufficient.
-   **Transaction Processing:** The `MoneyMachine` object securely handles coin payments and provides transaction reporting.
-   **Interactive Menu:** A user-friendly command-line interface for ordering drinks, viewing reports, and turning the machine off.
-   **Code Orchestration:** The main script cleanly orchestrates the interactions between objects, demonstrating high-level application flow control.

## How to Run

1.  Make sure you have Python installed on your system.
2.  Ensure all files (`main.py`, `menu.py`, `coffee_maker.py`, `money_machine.py`, and the `logo.py` file) are in the same directory.
3.  Run the main script from your terminal:
    ```bash
    python main.py
    ```
4.  Follow the on-screen prompts to place an order or generate a report.

## What I Learned

This project was a pivotal exercise in:
-   **Object-Oriented Programming (OOP):** Moving from procedural scripts to a class-based architecture to model real-world entities.
-   **Abstraction:** Hiding complex implementation details within methods (e.g., `make_payment`) and exposing a simple interface to the main application.
-   **Code Orchestration:** Learning how to write a main program that creates and coordinates objects to achieve a goal.
-   **Separation of Concerns:** Structuring an application so that each component has a distinct and isolated responsibility.
-   **Code Reusability:** Understanding how objects like `MoneyMachine` could potentially be reused in other applications.

---

## Project Disclaimer

This project is a snapshot of my skills at a specific point in time. It serves as a key milestone in my journey, demonstrating my transition from procedural to object-oriented thinking. The focus here is on architectural design and demonstrating a solid understanding of core programming principles.