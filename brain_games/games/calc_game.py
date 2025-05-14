from random import choice

from brain_games.engine import start_game
from brain_games.utils import get_random_number


def get_random_math_operator():
    math_operators = ["+", "-", "*"]
    return choice(math_operators)


def calculate_math_expression(first_number, second_number, math_operator):
    match math_operator:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
    return str(result)


def get_calc_game_question_and_answer():
    number1, number2 = get_random_number(), get_random_number()
    math_operator = get_random_math_operator()
    math_expression = f"{number1} {math_operator} {number2}"
    answer = calculate_math_expression(number1, number2, math_operator)
    return math_expression, answer


def start_calc_game():
    calc_game_instruction = 'What is the result of the expression?'
    start_game(calc_game_instruction, get_calc_game_question_and_answer)
    