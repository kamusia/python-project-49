import random
from brain_games import cli

max_correct = 3

def main():
    name = cli.greeting() #приветствие

    print('answer "yes" if the number is even, otherwise answer "no".') #правила игры
    
    corrects = 0
    while corrects < max_correct:

        num = random.randint(1, 25)

        if num % 2 == 1:
            correct_answer = 'yes'
        elif num % 2 == 0:
            correct_answer = 'no'

        print(f'Question: {num}')
        answer = input('Your answer: ')

        if cli.check_answer(answer, correct_answer, name) == True:
            corrects += 1
        else:
            break

        if corrects == 3:
            print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
