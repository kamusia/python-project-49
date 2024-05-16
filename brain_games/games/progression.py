import random


rules = 'What number is missing in the progression?'

def run_game():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    stop =  step*10 + start

    progression = [str(x) for x in range(start, stop, step)]

    skip = random.randint(0, 9)
    correct = progression[skip]

    progression[skip] = '..'
    question = progression

    return question, correct