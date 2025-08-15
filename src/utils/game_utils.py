
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


def get_boundaries():
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
    
    return (low_num, high_num)