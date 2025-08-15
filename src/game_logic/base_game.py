import random
from src.utils.game_utils import is_in_boundaries, score_calculator, validate_input, get_boundaries


def base_game():
    
    low_num, high_num = get_boundaries()
    
    randNum = random.randint(low_num,high_num)

    attemps = 0
    score = 100

    while True:
        user_guess = input(f'Guess a number between {low_num} and {high_num}: ')
        print('')

        attemps += 1
            
        if user_guess == 'q':
            print('-- Good Bye --\n')
            break
        
        if not validate_input(user_guess):
            score = score_calculator(score, 7)
            continue
        
        if not is_in_boundaries(user_guess,low_num, high_num):
            score = score_calculator(score, 7)
            continue
        
        user_guess = int(user_guess)
        
        if randNum > user_guess:
            print('-- Your guess is too low\n')
            score = score_calculator(score, 3)
            
        elif randNum < user_guess:
            print('-- your guess is too high\n')
            score = score_calculator(score, 3)
            
        elif randNum == user_guess:
            print('----- CONGRATULATION -----')
            print(f'Your SCORE: {score}')
            print(f'Your ATTEMPS: {attemps}\n')
            break
