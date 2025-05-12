from random import randint

from brain_games.cli import welcome_user


def get_random_number():
    random_number = randint(1, 65536)
    return random_number


def is_even(number):
    answer = number % 2
    return "no" if answer else "yes"


def start_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    rounds = 3
    for _ in range(rounds):
        random_number = get_random_number()
        player_answer = input(f'Question: {random_number}\nYour answer: ')
        correct_answer = is_even(random_number)
        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
    else:
        print(f"Congratulations, {name}!")