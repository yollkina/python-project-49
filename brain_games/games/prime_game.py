from brain_games.core.engine import start_game
from brain_games.core.utils import get_random_number


def is_prime(number):
    number_square_root = int(number ** 0.5)
    for div in range(2, number_square_root + 1):
        if number % div == 0:
            return 'no'
    return 'yes'


def get_prime_game_question_and_answer():
    number = get_random_number()
    answer = is_prime(number)
    return number, answer


def start_prime_game():
    prime_game_instruction = ('Answer "yes" if given number is prime. '
                              'Otherwise answer "no".')
    start_game(prime_game_instruction, get_prime_game_question_and_answer)