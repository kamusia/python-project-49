import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game():
    num = random.randint(1, 25)

    if num % 2 == 1:
        correct = 'no'
    elif num % 2 == 0:
        correct = 'yes'

    question = f'{num}'

    return question, correct
