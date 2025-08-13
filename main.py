import random

randNum = random.randint(1,100)

attemps = 0
score = 100

while True:
    user_guess = input('Guess a number between 1 and 100: ')
    print('')
    attemps += 1
        
    if user_guess == 'q':
        print('-- Good Bye --')
        print('')
        break
    elif not user_guess.isdigit():
        print('Invalid input. Not a Number')
        print('')
        score -= 7
        continue
    
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1:
        print('Your guess number is not in range')
        print('')
        score -= 7
        continue
    
    if randNum > user_guess:
        print('Your guess is too low')
        print('')
        score -= 3
        
    elif randNum < user_guess:
        print('your guess is too high')
        print('')
        score -= 3
        
    elif randNum == user_guess:
        print('----- CONGRATULATION -----')
        print(f'Your SCORE: {score}')
        print(f'Your ATTEMPS: {attemps}')
        print('')
        break