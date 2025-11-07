# Import necessary modules for the game's art and data.
from art import logo, vs
# Note: game_data is imported but the data is defined directly in this file for this version.
import random

# --- Game Data ---
# A list of dictionaries, where each dictionary represents an entity with a social media presence.
# This data is used to populate the comparison options for the player.
data = [
  {
    'name': "Instagram",
    'follower_count': 346,
    'description': "Social media platform",
    'country': "United States",
  },
  {
    'name': "Cristiano Ronaldo",
    'follower_count': 215,
    'description': "Footballer",
    'country': "Portugal",
  },
  {
    'name': "Ariana Grande",
    'follower_count': 183,
    'description': "Musician and actress",
    'country': "United States",
  },
  {
    'name': "Dwayne Johnson",
    'follower_count': 181,
    'description': "Actor and professional wrestler",
    'country': "United States",
  },
  {
    'name': "Selena Gomez",
    'follower_count': 174,
    'description': "Musician and actress",
    'country': "United States",
  },
  {
    'name': "Kylie Jenner",
    'follower_count': 172,
    'description': "Reality TV personality and businesswoman and Self-Made Billionaire",
    'country': "United States",
  },
  {
    'name': "Kim Kardashian",
    'follower_count': 167,
    'description': "Reality TV personality and businesswoman",
    'country': "United States",
  },
  {
    'name': "Lionel Messi",
    'follower_count': 149,
    'description': "Footballer",
    'country': "Argentina",
  },
  {
    'name': "Beyoncé",
    'follower_count': 145,
    'description': "Musician",
    'country': "United States",
  },
  {
    'name': "Neymar",
    'follower_count': 138,
    'description': "Footballer",
    'country': "Brasil",
  },
  {
    'name': "National Geographic",
    'follower_count': 135,
    'description': "Magazine",
    'country': "United States",
  },
  {
    'name': "Justin Bieber",
    'follower_count': 133,
    'description': "Musician",
    'country': "Canada",
  },
  {
    'name': "Taylor Swift",
    'follower_count': 131,
    'description': "Musician",
    'country': "United States",
  },
  {
    'name': "Kendall Jenner",
    'follower_count': 127,
    'description': "Reality TV personality and Model",
    'country': "United States",
  },
  {
    'name': "Jennifer Lopez",
    'follower_count': 119,
    'description': "Musician and actress",
    'country': "United States",
  },
  {
    'name': "Nicki Minaj",
    'follower_count': 113,
    'description': "Musician",
    'country': "Trinidad and Tobago",
  },
  {
    'name': "Nike",
    'follower_count': 109,
    'description': "Sportswear multinational",
    'country': "United States",
  },
  {
    'name': "Khloé Kardashian",
    'follower_count': 108,
    'description': "Reality TV personality and businesswoman",
    'country': "United States",
  },
  {
    'name': "Miley Cyrus",
    'follower_count': 107,
    'description': "Musician and actress",
    'country': "United States",
  },
  {
    'name': "Katy Perry",
    'follower_count': 94,
    'description': "Musician",
    'country': "United States",
  },
  {
    'name': "Kourtney Kardashian",
    'follower_count': 90,
    'description': "Reality TV personality",
    'country': "United States",
  },
  {
    'name': "Kevin Hart",
    'follower_count': 89,
    'description': "Comedian and actor",
    'country': "United States",
  },
  {
    'name': "Ellen DeGeneres",
    'follower_count': 87,
    'description': "Comedian",
    'country': "United States",
  },
  {
    'name': "Real Madrid CF",
    'follower_count': 86,
    'description': "Football club",
    'country': "Spain",
  },
  {
    'name': "FC Barcelona",
    'follower_count': 85,
    'description': "Football club",
    'country': "Spain",
  },
  {
    'name': "Rihanna",
    'follower_count': 81,
    'description': "Musician and businesswoman",
    'country': "Barbados",
  },
  {
    'name': "Demi Lovato",
    'follower_count': 80,
    'description': "Musician and actress",
    'country': "United States",
  },
  {
    'name': "Victoria's Secret",
    'follower_count': 69,
    'description': "Lingerie brand",
    'country': "United States",
  },
  {
    'name': "Zendaya",
    'follower_count': 68,
    'description': "Actress and musician",
    'country': "United States",
  },
  {
    'name': "Shakira",
    'follower_count': 66,
    'description': "Musician",
    'country': "Colombia",
  },
  {
    'name': "Drake",
    'follower_count': 65,
    'description': "Musician",
    'country': "Canada",
  },
  {
    'name': "Chris Brown",
    'follower_count': 64,
    'description': "Musician",
    'country': "United States",
  },
  {
    'name': "LeBron James",
    'follower_count': 63,
    'description': "Basketball player",
    'country': "United States",
  },
  {
    'name': "Vin Diesel",
    'follower_count': 62,
    'description': "Actor",
    'country': "United States",
  },
  {
    'name': "Cardi B",
    'follower_count': 67,
    'description': "Musician",
    'country': "United States",
  },
  {
    'name': "David Beckham",
    'follower_count': 82,
    'description': "Footballer",
    'country': "United Kingdom",
  },
  {
    'name': "Billie Eilish",
    'follower_count': 61,
    'description': "Musician",
    'country': "United States",
  },
  {
    'name': "Justin Timberlake",
    'follower_count': 59,
    'description': "Musician and actor",
    'country': "United States",
  },
  {
    'name': "UEFA Champions League",
    'follower_count': 58,
    'description': "Club football competition",
    'country': "Europe",
  },
  {
    'name': "NASA",
    'follower_count': 56,
    'description': "Space agency",
    'country': "United States",
  },
  {
    'name': "Emma Watson",
    'follower_count': 56,
    'description': "Actress",
    'country': "United Kingdom",
  },
  {
    'name': "Shawn Mendes",
    'follower_count': 57,
    'description': "Musician",
    'country': "Canada",
  },
  {
    'name': "Virat Kohli",
    'follower_count': 55,
    'description': "Cricketer",
    'country': "India",
  },
  {
    'name': "Gigi Hadid",
    'follower_count': 54,
    'description': "Model",
    'country': "United States",
  },
  {
    'name': "Priyanka Chopra Jonas",
    'follower_count': 53,
    'description': "Actress and musician",
    'country': "India",
  },
  {
    'name': "9GAG",
    'follower_count': 52,
    'description': "Social media platform",
    'country': "China",
  },
  {
    'name': "Ronaldinho",
    'follower_count': 51,
    'description': "Footballer",
    'country': "Brasil",
  },
  {
    'name': "Maluma",
    'follower_count': 50,
    'description': "Musician",
    'country': "Colombia",
  },
  {
    'name': "Camila Cabello",
    'follower_count': 49,
    'description': "Musician",
    'country': "Cuba",
  },
  {
    'name': "NBA",
    'follower_count': 47,
    'description': "Club Basketball Competition",
    'country': "United States",
  },
]

# --- Game Logic ---

# Initialize the player's score at the start of the game.
score = 0

# The main game loop. It runs for a maximum number of rounds based on the data length.
# Using len(data) - 1 ensures there are enough unique pairs for the entire game.
for i in range(0,len(data)-1):

  # Randomly select two different items from the data list for comparison.
  # random.sample is perfect for this as it picks unique items.
  item_a, item_b = random.sample(data, 2)

  # --- Display the Round ---
  # Clear the screen and display the game's UI for the current round.
  print(logo)
  print(f'Your current score is: {score}')
  print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}.")
  print(vs)
  print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}.")

  # --- Get User Input ---
  # Prompt the user to make a choice between item A and item B.
  decision = input("Who has more followers? Type 'A' or 'B': ").lower()

  # --- Input Validation ---
  # Ensure the user enters a valid choice ('a' or 'b').
  # The loop will continue to prompt until a valid input is received.
  while decision != 'a' and decision != 'b':
      decision = input("Please enter the right choice again 'a' or 'b': ").lower()

  # --- Compare and Determine Result ---
  # Check if the user's choice matches the entity with the higher follower count.
  # This single condition covers both possibilities (choosing A or choosing B).
  if ((decision == 'a' and item_a['follower_count'] > item_b['follower_count']) or
      (decision == 'b' and item_b['follower_count'] > item_a['follower_count'])):
    # If the user is correct, increment their score and the game continues.
    print("That's right!")
    score += 1
  else:
    # If the user is wrong, print a message and exit the game loop immediately.
    print("That's wrong!")
    break

# --- Game Over ---
# Once the loop ends (either by a wrong answer or finishing all rounds), display the final score.
print(f'Your final score is: {score}')