import prompt # type: ignore


def main():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")


# def welcome_user1():
#    name = ''
#    while name == '':
#        print('May I have your name? ', end='')
#        name = input()
#        print(f"Hello, {name}")


if __name__ == '__main__':
    main()
