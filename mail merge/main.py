# Define the placeholder string that will be replaced with actual names
PLACEHOLDER = "[name]"

# Read the list of names from the input file
# Each line in the file becomes an element in the names list
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read the template letter that contains the placeholder
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    # Iterate through each name in the list
    for name in names:
        # Remove any leading/trailing whitespace or newline characters
        stripped_name = name.strip()

        # Replace the placeholder with the current name to create personalized content
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Create a new file for each personalized letter in the output directory
        # File naming convention: letter_for_[name].docx
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", "w") as completed_letter:
            # Write the personalized content to the new file
            completed_letter.write(new_letter)