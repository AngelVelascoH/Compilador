from lexer import *
from parse import *
import io



def main():
    print("Compilador PYTHON ----> C++")

    f = io.open('test.txt',mode='r',encoding="utf-8")
    inp = '\n' + f.read()
    lexer = Lexer(inp)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()
    print("FIN DEL ANALIZADOR LÉXICO")
    print("<-------------------------->")

    parser = Parser(lexer)

    parser.file()
    print("FIN DEL PARSING")
    print("<-------------------------->")


main()

