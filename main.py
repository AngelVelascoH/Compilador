from lexer import *


def main():
    f = open('proyectoFInal.txt')
    inp = f.read()
    lexer = Lexer(inp)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


main()

