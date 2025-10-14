import random

print("Welcome to the number guessing game!".title)
print("I'm thinking of a number between 1 and 100.")

user_decision = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if user_decision == 'easy':
    print("You have 10 attemps remaining to guess the number.")
    u_attempts = 10
elif user_decision == 'hard':
    print("You have 5 attemps remaining to guess the number.")
    u_attempts = 5

def computer_guess():
    global COMPUTER_GUESS
    COMPUTER_GUESS = random.randint(1,100)
    return COMPUTER_GUESS 

def game():
    global u_attempts
    c_guess = computer_guess()
    user_guess = int(input("Make a guess: "))

    print(c_guess)

    while u_attempts > 1:
        if user_guess > 100 or user_guess < 0:
            print("Out of range, try again")   
        elif user_guess > c_guess:
            print("Too high\nGuess again")
        elif user_guess < c_guess:
            print("Too low\nGuess again")
        elif user_guess == c_guess:
            print(f"You got it! the answer was {c_guess}")       
            break

        u_attempts -= 1
        print(f"You have {u_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        
    if user_guess != c_guess:
        print("You ran out of attempts")
        

print(game())

user_play_decisoin = input("do you want to play again? type 'y' or 'n': ")

if user_play_decisoin == 'y':
    c_guess = computer_guess()
    print(game())
else:
    print("Thank you for playing.")







    
    
    

