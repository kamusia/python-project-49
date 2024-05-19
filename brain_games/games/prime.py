import random


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    num = random.randint(1, 100)

    question = num

    stop = int(num**0.5)
    correct = 'yes'
    for i in range(2, stop + 1):
        if num % i == 0:
            correct = 'no'

    return question, correct
