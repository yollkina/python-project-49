from brain_games.core.engine import start_game
from brain_games.core.utils import get_random_number


def is_even(number):
    answer = number % 2
    return "no" if answer else "yes"


def get_even_game_question_and_answer():
    number = get_random_number()
    answer = is_even(number)
    return number, answer


def start_even_game():
    even_game_instruction = ('Answer "yes" if the number is even, '
                             'otherwise answer "no".')
    start_game(even_game_instruction, get_even_game_question_and_answer)