import random


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    stop = int(num**0.5)
    for i in range(2, stop + 1):
        if num % i == 0:
            return False
    return True


def run_game():
    num = random.randint(1, 100)
    correct = 'yes' if is_prime(num) else 'no'
    question = num
    return question, correct
