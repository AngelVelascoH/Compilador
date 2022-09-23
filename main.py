from lexer import *


def main():
    inp = "var = 123"
    lexer = Lexer(inp)

    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()


main()

