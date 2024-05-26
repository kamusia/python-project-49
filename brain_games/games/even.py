import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 1:
        return 'no'
    elif num % 2 == 0:
        return 'yes'


def run_game():
    num = random.randint(1, 25)
    correct = is_even(num)
    question = f'{num}'

    return question, correct
