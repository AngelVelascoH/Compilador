from lexer import *


def main():
    inp = "+- */>>= =\"Hello World\" != =="
    lexer = Lexer(inp)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


main()

