import pandas

# Read NATO phonetic alphabet data from CSV file into a DataFrame
alpha_dictionary = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alpha = pandas.DataFrame(alpha_dictionary)

# Create a dictionary comprehension to map letters to their phonetic codes
# Format: {'A': 'Alfa', 'B': 'Bravo', ...}
new_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}

# Get user input and convert to uppercase for consistent matching
user_input = input("Please enter your word: ").upper()

# Convert the input word into a list of individual characters
user_input_list = list(user_input)

# Use list comprehension to convert each letter to its NATO phonetic code
# Only includes letters that exist in the NATO alphabet dictionary
list_output = [new_dict[letter] for letter in user_input_list if letter in new_dict]

# Display the resulting list of phonetic code words
print(list_output)

