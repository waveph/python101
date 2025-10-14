import random

def computer_guess():
    """Generate random number between 1-100"""
    COMPUTER_GUESS = random.randint(1,100)
    return COMPUTER_GUESS 

def game():
    """Main game logic for guessing the number"""
    global u_attempts
    c_guess = computer_guess()
    user_guess = int(input("Make a guess: "))

    # Loop until user runs out of attempts
    while u_attempts > 1:
        # Check if guess is out of valid range
        if user_guess > 100 or user_guess < 0:
            print("Out of range, try again")   
        # Check if guess is too high
        elif user_guess > c_guess:
            print("Too high\nGuess again")
        # Check if guess is too low
        elif user_guess < c_guess:
            print("Too low\nGuess again")
        # User guessed correctly
        elif user_guess == c_guess:
            print(f"You got it! the answer was {c_guess}")       
            break

        # Decrement attempts and show remaining
        u_attempts -= 1
        print(f"You have {u_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
    
    # User ran out of attempts without guessing correctly
    if user_guess != c_guess:
        print("You ran out of attempts")

# Game welcome message
print("Welcome to the number guessing game!".title)
print("I'm thinking of a number between 1 and 100.")

# Main game loop - allows replay
user_play_decisoin = 'y'
while user_play_decisoin == 'y':
    # Get difficulty choice from user
    user_decision = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    # Set attempts based on difficulty
    if user_decision == 'easy':
        print("You have 10 attemps remaining to guess the number.")
        u_attempts = 10
    elif user_decision == 'hard':
        print("You have 5 attemps remaining to guess the number.")
        u_attempts = 5

    # Start the game
    game()
    
    # Ask if user wants to play again
    user_play_decisoin = input("do you want to play again? type 'y' or 'n': ")
    
    # If yes, ask for difficulty again
    if user_play_decisoin == 'y':
        user_decision = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    # If no, exit the game
    elif user_play_decisoin == 'n':
        break