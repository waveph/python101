import math
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



while True:
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

    decision = input('Do you want to play a game of Blackjck? Type \'y\' or \'n\': ')

    if decision == 'n':
        break

    if decision == 'y':

        u_card = random.choice(cards)
        user_cards.append(u_card)

        u_card = random.choice(cards)
        user_cards.append(u_card)
        user_score = sum(user_cards)

        c_card = random.choice(cards)
        computer_cards.append(c_card)

        c_card = random.choice(cards)
        computer_cards.append(c_card)
        computer_score = sum(computer_cards)

        print(f'    Your cards: {user_cards}, current score: {user_score}')
        print(f'    Computer\'s first card: [{computer_cards[0]}]')
        if user_score == 21:
            print('You win')
            break
        elif computer_score == 21:
            # print(f'    Your cards: {user_cards}, current score: {user_score}')
            print(f'    Computer\'s first card: [{computer_cards}], computer score: {computer_score}')
            print('computer wins')
            break

        decision_2 = input('do you want another card pls? Type \'y\' or \'n\': ')
        while decision_2 == 'y':

            u_card = random.choice(cards)
            user_cards.append(u_card)
            user_score = sum(user_cards)

            if user_score > 21:
                print(f'    Your cards: {user_cards}, current score: {user_score}')
                print(f'    Computer\'s card: {computer_cards}, computer score: {computer_score}')
                print('you lose')
                break
            elif user_score < 21 or computer_score < 21 and user_score > computer_score and decision_2 == 'n':
                print(f'    Your cards: {user_cards}, current score: {user_score}')
                print(f'    Computer\'s card: {computer_cards}, computer score: {computer_score}')
                print('you win')
                break
            elif user_score < 21 or computer_score < 21 and user_score < computer_score:
                print('computer wins')

        decision_2 = input('do you want another card pls-2? Type \'y\' or \'n\': ')
        if decision_2 == 'n':
            break

