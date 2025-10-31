import random

with open(r"\Users\abdou\OneDrive\Documents\python101\mail merge\Input\Letters\starting_letter.txt", "r") as letter:
    text = letter.readlines()

with open(r"\Users\abdou\OneDrive\Documents\python101\mail merge\Input\Names\invited_names.txt", "r") as names:
    names = names.readlines()

with open(r"\Users\abdou\OneDrive\Documents\python101\mail merge\Input\Names\invited_names.txt", "a") as names:
    for i in range(0,len(text)):
        letters = text[i].replace("[name]", f"{names}")





#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp