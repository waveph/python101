import turtle
from os import write

import pandas

# Initialize the game screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# Create a turtle for writing state names on the map
to_write = turtle.Turtle()
to_write.penup()
to_write.hideturtle()

# Set the background image of the US states map
turtle.shape(image)

# Load state data from CSV file
data = pandas.read_csv("50_states.csv")

# Extract states list and their coordinates from the dataframe
data_states = data.state.to_list()
data_xs = data.x.to_list()
data_ys = data.y.to_list()

# Initialize game variables
correct_guesses = []
len_correct_guesses = 0

# Main game loop
game_is_on = True
while game_is_on:
    # Prompt user for state name input and display current score
    answer_state = screen.textinput(title=f"{len_correct_guesses} /50 States Correct",
                                    prompt="What's another state's name?").title()

    # Check if the guessed state is in the list of states
    if answer_state in data_states:
        # Get the index of the correct state to find its coordinates
        state_index = data_states.index(answer_state)
        x = data_xs[state_index]
        y = data_ys[state_index]

        # Move turtle to state coordinates and write the state name
        to_write.goto(x, y)
        to_write.write(answer_state)

        # Add to correct guesses list and update score counter
        correct_guesses.append(answer_state)
        len_correct_guesses += 1

    # End game when all 50 states are guessed correctly
    if len(correct_guesses) == len(data_states):
        game_is_on = False

# Keep the screen open until user clicks
screen.exitonclick()