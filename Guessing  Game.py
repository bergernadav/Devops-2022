import random


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    number = input("whats is your guess between 1 to " + difficulty + ":")
    return int(number)


def compare_results(secret_number, user_guess):
    return secret_number == user_guess


def play_memory_game():
    difficulty_input = input("What is the wanted difficulty? ")
    secret_number = generate_number(difficulty_input)
    user_guess = get_guess_from_user(difficulty_input)
    print(compare_results(secret_number, user_guess))


def check_if_should_play_again():
    user_answer = input('would you like to play again? (y/n):')
    while user_answer != 'n' and user_answer != 'y':
        print('you have entered invalid answer ' + user_answer + ' please enter only (y/n)')
        user_answer = input('would you like to play again? (y/n):')

    if user_answer == 'y':
        return True

    print('thank you for playing with us')
    return False


def play():
    should_play = True  # at least 1 game of guessing
    while should_play:
        play_memory_game()
        should_play = check_if_should_play_again()


play()
