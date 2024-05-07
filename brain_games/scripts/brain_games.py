#!/usr/bin/env python3
import brain_even
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    cli.main()
    brain_even.main()


if __name__ == '__main__':
    main()
