import random


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    stop = int(num**0.5)
    for i in range(2, stop + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def run_game():
    num = random.randint(1, 100)
    correct = is_prime(num)
    question = num
    return question, correct
