import random
import brain_games


def main():
    brain_games.main()
    print('answer "yes" if the number is even, otherwise answer "no".')
    corrects = 0
    while corrects < 3:

        num = random.randint(1, 25)

        if num % 2 == 1:
            correct = 'yes'
        elif num % 2 == 0:
            correct = 'no'

        print(f'Question: {num}')
        answer = input('Your answer: ')

        if answer == correct:
            corrects += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.\nLet's try again, Bill!")
            break
        if corrects == 3:
            print('Congratulations, {name}')


if __name__ == '__main__':
    main()
