import random


rules = 'answer "yes" if the number is even, otherwise answer "no".'

def run_game():
    num = random.randint(1, 25)

    if num % 2 == 1:
        correct = 'yes'
    elif num % 2 == 0:
        correct = 'no'
    
    question = f'{num}'

    return question, correct