from lexer import *
from parse import *
import io



def main():
    print("Compilador PYTHON ------> C++")
    print("\n")
    f = io.open('proyectoFinal.txt',mode='r',encoding="utf-8")
    inp = '\n' + f.read()
    lexer = Lexer(inp)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()
    print("FIN DEL ANALIZADOR LÉXICO")
    print("<-------------------------->")
    lexer = Lexer(inp)
    emmiter = Emmiter('out.cpp')
    parser = Parser(lexer,emmiter)
    parser.file()
    emmiter.writeFile()
    print("FIN DEL PARSING")
    print("<-------------------------->")
    print("COMPILACIÓN COMPLETA")


main()

