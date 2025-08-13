import random


def validate_input(user_guess):
    try:
        int(user_guess)
        return True
    except:
        return False
        

def is_in_boundaries(number ,low_band, up_band):
    number = int(number)
    if number > up_band or number < low_band:
        print('-- Your guess number is not in range\n')
        return False
    
    return True


def score_calculator(score, minus):
    score -= minus
    return max(score, 0)


def base_game():
    while True:
        low_num = input('Enter the lower limit of the number: ')
        if not validate_input(low_num):
            continue
        low_num = int(low_num)
        break
    
    while True:
        high_num = input('Enter the upper limit of the number: ')
        if not validate_input(high_num):
            continue
        high_num = int(high_num)
        break
    
    
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
 
        
def main():
    while True:
        base_game()
        print('')
        play_again = input('do you want to play again? [y/n]: ')
        if play_again == 'y' or play_again == 'Y':
            continue
        break


if __name__ == '__main__':
    main()
    
 