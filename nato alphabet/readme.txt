 NATO Phonetic Alphabet Converter

Description:
A Python program that converts words into their corresponding NATO phonetic alphabet codes.
The program reads from a CSV database of NATO phonetic codes and translates user input
into phonetic equivalents.

Features:
- Loads NATO phonetic alphabet data from CSV file
- Converts user input to uppercase for consistent processing
- Translates each letter to its corresponding NATO code
- Handles only valid letters present in the NATO alphabet

Requirements:
- Python 3.x
- pandas library

Usage:
1. Run the script
2. Enter any word when prompted
3. Program returns a list of NATO phonetic codes for each letter

Example:
Input: "hello"
Output: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

Files:
- main.py - Main program file
- nato_phonetic_alphabet.csv - Database of NATO codes

This project demonstrates data processing with pandas, dictionary comprehensions,
and list operations in Python.
