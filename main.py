from lexer import *
from parse import *


def main():
    print("Compilador PYTHON ----> C++")

    f = open('test.txt')
    inp = f.read()
    lexer = Lexer(inp)
    
    print("FIN DEL ANALIZADOR LÉXICO")
    print("<-------------------------->")

    parser = Parser(lexer)

    parser.file()
    print("FIN DEL PARSING")
    print("<-------------------------->")


main()

