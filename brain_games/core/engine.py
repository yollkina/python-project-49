import prompt

from brain_games.core.constants import ROUNDS_COUNT


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(instruction, get_question_and_answer):
    name = welcome_user()
    print(instruction) 
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_question_and_answer()
        player_answer = input(f'Question: {question}\nYour answer: ')
        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
    else:
        print(f"Congratulations, {name}!")

