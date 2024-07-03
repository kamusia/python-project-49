import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 1:
        return False
    elif num % 2 == 0:
        return True


def run_game():
    num = random.randint(1, 25)
    correct = 'yes' if is_even(num) else 'no'
    question = f'{num}'

    return question, correct
