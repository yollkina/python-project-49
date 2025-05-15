from brain_games.core.engine import start_game
from brain_games.core.utils import get_random_number


def get_gcd(number1, number2):
    if number1 < number2:
        number1, number2 = number2, number1

    while number2 != 0:
        number1, number2 = number2, number1 % number2
    
    return str(number1)


def get_gcd_game_question_and_answer():
    number1, number2 = get_random_number(), get_random_number()
    numbers = f'{number1} {number2}'
    answer = get_gcd(number1, number2)
    return numbers, answer


def start_gcd_game():
    gcd_game_instruction = 'Find the greatest common divisor of given numbers.'
    start_game(gcd_game_instruction, get_gcd_game_question_and_answer)