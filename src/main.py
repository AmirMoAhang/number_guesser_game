from src.game_logic.base_game import base_game

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