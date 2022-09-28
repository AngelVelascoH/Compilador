from lexer import *


def main():
    inp = """
    def impresion(mensaje,informacion):
    print("el resultado de esta suma es :" + 23.4)
    """
    lexer = Lexer(inp)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


main()

