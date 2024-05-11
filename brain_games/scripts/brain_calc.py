from brain_games import cli
import random


plus_op = '+'
minus_op = '-'
multy_op = '*'
max_correct = 3

ops = (plus_op, minus_op, multy_op)

def main():
    name = cli.greeting() #приветствие

    print('What is the result of the expression?') #правила игры

    corrects = 0
    while corrects < 3:
        random_num1 = random.randint(1, 100)
        random_num2 = random.randint(1, 100)
        operation = random.choice(ops)

        if operation == '+':
            correct_answer = random_num1 + random_num2
        elif operation == '-':
            correct_answer = random_num1 - random_num2
        elif operation == '*':
            correct_answer = random_num1 * random_num2

        print(f'Question: {random_num1} {operation} {random_num2}')
        answer = int(input('Your answer: '))

        if cli.check_answer(answer, correct_answer, name) == True:
            corrects += 1
        else:
            break

        if corrects == 3:
            print(f'Congratulations, {name}')
    
if __name__ == "__main__":
    main()