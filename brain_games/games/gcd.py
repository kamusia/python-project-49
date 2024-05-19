import random


rules = 'Find the greatest common divisor of given numbers.'


def run_game():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    question = f'{a} {b}'

    if a == b:
        correct = str(a)

    if a < b:
        a, b = b, a

    remainder = a % b
    while remainder != 0:
        remainder = a % b
        a, b = b, remainder
        correct = str(a)

    return question, correct
