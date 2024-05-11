import prompt # type: ignore


def greeting():
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


if __name__ == '__main__':
    greeting()
