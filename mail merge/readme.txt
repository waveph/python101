
This project automatically creates personalized letters for multiple people.

WHAT IT DOES:
- Reads names from a list in Input/Names/invited_names.txt
- Uses a template letter from Input/Letters/starting_letter.txt
- Replaces [name] with each person's actual name
- Saves personalized letters in Output/ReadyToSend/ folder

HOW TO USE:
1. Put your names in Input/Names/invited_names.txt (one name per line)
2. Write your letter template in Input/Letters/starting_letter.txt
   Use [name] where you want the name to appear
3. Run the Python script
4. Find all personalized letters in Output/ReadyToSend/

EXAMPLE:
If invited_names.txt has: John, Jane, Mike
And starting_letter.txt has: "Hello [name], you're invited!"
The program will create:
- letter_for_John.docx with "Hello John, you're invited!"
- letter_for_Jane.docx with "Hello Jane, you're invited!"
- letter_for_Mike.docx with "Hello Mike, you're invited!"

PROJECT DISCLAIMER

This project is for educational purposes only.

- This code is provided "as is" without any warranties
- Intended for learning and personal use only
- Not recommended for production environments without proper testing
- User is responsible for any files generated or modified
- Always backup your original files before running
- Not intended for commercial use without modifications
- May require adjustments for different operating systems
- Use at your own risk

