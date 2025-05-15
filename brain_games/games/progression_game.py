from random import randint

from brain_games.core.engine import start_game
from brain_games.core.utils import get_random_number
    

def get_progression_game_question_and_answer():
    first_term = get_random_number()
    step = randint(1, 10)
    terms_count = randint(5, 15)
    last_term = first_term + (terms_count - 1) * step
    progression = [str(num) for num in range(first_term, last_term + 1, step)]
    missing_term_index = randint(0, terms_count - 1)
    answer = progression[missing_term_index]
    progression[missing_term_index] = '..'
    return ' '.join(progression), answer


def start_progression_game():
    progr_game_instruction = 'What number is missing in the progression?'
    start_game(progr_game_instruction, get_progression_game_question_and_answer)