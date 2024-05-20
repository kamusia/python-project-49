import prompt  # type: ignore


def greeting():  # приветствие
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    return name

# def welcome_user1():
#    name = ''
#    while name == '':
#        print('May I have your name? ', end='')
#        name = input()
#        print(f"Hello, {name}")


def get_answer(question):
    print("Question: ", question)
    answer = prompt.string("Your answer: ")
    return answer


def check_answer(answer, correct_answer, name):  # проверка ответа
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was"
              f"'{correct_answer}'.\nLet's try again, {name}!")
        return False
