from sys import argv

from lexical import Lexical


def main():
    lexical = Lexical(argv[1])

    result = lexical.get_token()

    while result is not None:
        print(result)
        result = lexical.get_token()

    print('\n\n')


if __name__ == '__main__':
    main()
