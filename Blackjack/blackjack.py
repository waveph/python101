import math
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

decision = ''

u_first_card = 0
u_second_card = 0
u_third_card = 0
user_cards = []
user_score = 0
new_user_score = 0

computer_cards = []
c_first_card = 0
c_second_card = 0
c_third_card = 0
computer_score = 0
new_computer_score = 0


while True:

    decision = input('Do you want to play a game of Blackjck? Type \'y\' or \'n\': ')

    if decision == 'n':
        break

    if decision == 'y':

        u_first_card = random.choice(cards)
        user_cards.append(u_first_card)
        u_second_card = random.choice(cards)
        user_cards.append(u_second_card)

        user_score = u_first_card + u_second_card

        c_first_card = random.choice(cards)
        computer_cards.append(c_first_card)
        c_second_card = random.choice(cards)
        computer_cards.append(c_second_card)
        computer_score = c_first_card + c_second_card

        print(f'    Your cards: {user_cards}, current score: {user_score}')
        print(f'    Computer\'s first card: [{c_first_card}]')
    if user_score > 21 or user_score == 21:
        break
    decision_2 = input("Type 'y' to get another card, type 'n' to pass: ")
    if decision_2 == 'y':
        new_u_element = random.choice(cards)
        user_cards.append(new_u_element)
        user_score = user_score + new_u_element
    if decision_2 == 'n':
        break





