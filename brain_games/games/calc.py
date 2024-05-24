import random


rules = 'What is the result of the expression?'
plus_op = '+'
minus_op = '-'
multy_op = '*'
ops = [plus_op, minus_op, multy_op]


def run_game():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    operation = random.choice(ops)

    if operation == '+':
        correct = str(random_num1 + random_num2)
    elif operation == '-':
        correct = str(random_num1 - random_num2)
    elif operation == '*':
        correct = str(random_num1 * random_num2)

    question = f'{random_num1} {operation} {random_num2}'

    return question, correct
