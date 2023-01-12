from lib2to3.pgen2 import token
import sys
from lexer import *
from emmiter import *

# Parser object keeps track of current token and checks if the code matches the grammar.
class Parser:
    def __init__(self, lexer,emmiter):
        self.lexer = lexer
        self.emmiter = emmiter
        
        self.symbols = set()
        self.functionsDeclared = set()
        self.functionsCalled = set()

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()
    # Return true if the current token matches.
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Return true if the next token matches.
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort(f"Expected {kind.name}, got {self.curToken.kind}")
        else:
            text = self.curToken.text
            self.nextToken()
            return text
    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    def abort(self, message):
        sys.exit("Error. " + message)

    #reglas de la gramatica de Python
    def file(self):
        print("Inicio Programa++++++")
        #boilerplate de C++ en el momento en el que iniciamos el parsing del archivo
        self.emmiter.headerLine("#include<iostream>")
        self.emmiter.headerLine("#include<stdio.h>")
        self.emmiter.headerLine("#include<string>")
        self.emmiter.headerLine("#include<vector>")
        self.emmiter.headerLine("#include<variant>")
        self.emmiter.headerLine("using namespace std;")
        self.emmiter.headerLine("using std::vector;")
        self.emmiter.headerLine("using std::variant;")
        self.emmiter.headerLine("\n")
        self.emmiter.emmitLine("int main()")
        self.emmiter.emmitLine("{")

        if self.checkToken(TokenType.INDENTATION):
            self.abort("Indentacion no esperada")
        #saltar los saltos de linea no necesarios.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
        #analizar todas las sentencias en el programa.
        while not self.checkToken(TokenType.EOF):
            self.statement()
        
        self.emmiter.emmitLine("return 0;")
        self.emmiter.emmitLine("}")

        for funcion in self.functionsCalled:
            if funcion not in self.functionsDeclared:
                self.abort(f"llamada a {funcion} no valida, la funcion no está declarada.")
        print("Fin del programa------")
    def statement(self,main_check = 0):
        #Checar el primer token para ver el tipo de sentencia.
        #print
        
        if self.checkToken(TokenType.PRINT):
            print("SENTENCIA PRINT")
            self.nextToken()
            self.match(TokenType.PAREN_OP)
            if self.checkToken(TokenType.STRING):
                if main_check == 1:
                    self.emmiter.headerLine(f"cout<<\"{self.curToken.text}\"<<endl;")
                else:
                    self.emmiter.emmitLine(f"cout<<\"{self.curToken.text}\"<<endl;")
                    self.match(TokenType.STRING)
            else:
                args = []
                args = self.argumentos(args)
                args = '<< \" \"<< '.join(args)
                if main_check == 1:
                    self.emmiter.headerLine(f"cout<<{args}<<endl;")
                else:
                    self.emmiter.emmitLine(f"cout<<{args}<<endl;")
            self.match(TokenType.PAREN_CL)

        elif self.checkToken(TokenType.DEF):
            args = []
            print("FUNCION+++")
            self.nextToken()
            function_identifier = self.match(TokenType.IDENT)
            self.functionsDeclared.add(function_identifier)
            self.match(TokenType.PAREN_OP)
            args = self.argumentos(args)
            args2 = []
            for element in args:
                element = f"variant<float,string> {element}"
                args2.append(element)
            args = args2
            args = ', '.join(args)
            self.match(TokenType.PAREN_CL)
            self.match(TokenType.COL)
            self.match(TokenType.INDENTATION)
            self.statement(1)
            while self.checkToken(TokenType.NEWLINE):
                self.nextToken()
                self.statement(1)
            if self.checkToken(TokenType.RETURN):
                self.emmiter.headerLine(f"float {function_identifier}({args}){{")
                return_variable = self.returnStatement()
                self.emmiter.headerLine(f"return {return_variable};")
            else:
                self.match(TokenType.DEDENTATION)
            self.emmiter.headerLine("}")
            print("FIN FUNCION---")
            main_check = 0

        elif self.checkToken(TokenType.APPEND):
            print("SENTENCIA APPEND")
            self.nextToken()
            self.match(TokenType.PAREN_OP)
            self.expression()
            self.match(TokenType.PAREN_CL) 

        elif self.checkToken(TokenType.INPUT):
            print("SENTENCIA INPUT")
            self.nextToken()
            self.match(TokenType.PAREN_OP)
            self.match(TokenType.STRING)
            self.match(TokenType.PAREN_CL)
        
        elif self.checkToken(TokenType.INT):    
            print("SENTENCIA INT")
            self.nextToken()
            self.match(TokenType.PAREN_OP)
            self.expression()
            self.match(TokenType.PAREN_CL)
        
        elif self.checkToken(TokenType.FOR):
            print("SENTENCIA FOR")
            self.nextToken()
            self.match(TokenType.IDENT)
            self.match(TokenType.IN)
            if self.checkToken(TokenType.RANGE):
                self.nextToken()
                self.match(TokenType.PAREN_OP)
                self.expression()
                self.match(TokenType.COMMA)
                self.expression()
                self.match(TokenType.PAREN_CL)
                self.match(TokenType.COL)
                self.match(TokenType.INDENTATION)
                self.statement(main_check)
                while self.checkToken(TokenType.NEWLINE):
                    self.nextToken()
                    self.statement(main_check)
                self.match(TokenType.DEDENTATION)
            else:
                self.match(TokenType.IDENT)
                self.match(TokenType.COL)
                self.match(TokenType.INDENTATION)
                self.statement(main_check)
                self.match(TokenType.DEDENTATION)
            print("FIN SENTENCIA FOR")



        elif self.checkToken(TokenType.IDENT):
            if self.checkPeek(TokenType.EQ):
                print("ASIGNACION")
                identifier = self.curToken.text
                self.nextToken()
                self.match(TokenType.EQ)

                #caso de que hable de una asignación variable variable
                if self.checkToken(TokenType.IDENT):
                    if self.checkPeek(TokenType.PAREN_OP):
                        self.statement(main_check)
                    else:
                        tokens = self.expression()
                        print(tokens)
                        tokens = "".join(tokens)
                        if main_check == 1:
                            self.emmiter.headerLine(f"{identifier} = {tokens}")
                        else:
                            self.emmiter.emmitLine(f"{identifier} = {tokens}")
                #caso de que se hable de una asignación de tipo, es decir, crear una variable o lista      
                else:
                    tokens = self.expression()
                    tokens = "".join(tokens)
                    if len(tokens) > 0:
                        if tokens[0] == '[':
                            if main_check == 1:
                                #usamos las propiedades de variant para asegurar un tipo de lista de esos tipos.
                                self.emmiter.headerLine(f"vector<variant<int, float, string>> {identifier};")
                            else:
                                self.emmiter.emmitLine(f"vector<variant<int, float, string>> {identifier};")
                        elif tokens[0][0].isdigit():
                            if main_check == 1:
                                self.emmiter.headerLine(f"float {identifier} = {tokens};")
                            else:
                                self.emmiter.emmitLine(f"float {identifier} = {tokens};")
                       
                        else:
                            if main_check == 1:
                                self.emmiter.headerLine(f"string {identifier} = {tokens};")
                            else:
                                self.emmiter.emmitLine(f"string {identifier} = {tokens};")
                    else:
                        pass
            #caso de llamada a función
            elif self.checkPeek(TokenType.PAREN_OP):
                identifier = self.curToken.text
                if identifier in self.functionsDeclared:
                    args = []
                    print("LLAMADA FUNCION")
                    self.nextToken()
                    self.match(TokenType.PAREN_OP)
                    self.argumentos(args)
                    self.match(TokenType.PAREN_CL)
                else:
                    self.abort(f"Error, {identifier} no está definido.")
            else:
                print("METODO")
                self.nextToken()
                self.match(TokenType.DOT)
                self.statement(main_check)
                
        elif self.checkToken(TokenType.NEWLINE):
            if self.checkPeek(TokenType.EOF):
                print("---FIN DEL MAIN---")
                self.nextToken()
            else:
                print("---INICIO DEL MAIN---")
                self.nextToken()
                self.statement(main_check)
                while self.checkToken(TokenType.NEWLINE):
                    if self.checkToken(TokenType.EOF):
                        print("___Main___")
                        break
                    self.nextToken()
                    self.statement(main_check)



            
        else:
            self.abort(f"Invalid statement at {self.curToken.text} ({self.curToken.kind.name})")
             

    def nl(self):
        print("SALTO DE LINEA")
        if self.checkToken(TokenType.DEDENTATION):
         while self.checkToken(TokenType.DEDENTATION):
            self.nextToken()   
        if self.checkToken(TokenType.NEWLINE):
            while self.checkToken(TokenType.NEWLINE):
                self.nextToken()
    def returnStatement(self):
        print("RETURN")
        self.nextToken()
        variable = self.curToken.text
        self.expression()
        self.match(TokenType.DEDENTATION)
        return variable
    def argumentos(self,args):
        print("ARGUMENTOS")
        if self.checkToken(TokenType.IDENT) or self.checkToken(TokenType.STRING) or self.checkToken(TokenType.NUMBER):
            args.append(self.curToken.text)
            self.nextToken()
            while self.checkToken(TokenType.COMMA):
                self.nextToken()
                if self.checkToken(TokenType.IDENT) or self.checkPeek(TokenType.STRING) or self.checkPeek(TokenType.NUMBER):
                    args.append(self.curToken.text)
                    self.nextToken()
        if self.checkToken(TokenType.INT):
            self.expression()
        return args

                    
    def expression(self):
        tokens = []
        print("EXPRESSION")
        if self.checkToken(TokenType.INPUT):
            print("INPUT")
            self.nextToken()
            self.match(TokenType.PAREN_OP)
            self.match(TokenType.STRING)
            self.match(TokenType.PAREN_CL)
        elif self.checkToken(TokenType.INT):
            print("INT")
            self.nextToken()
            self.match(TokenType.PAREN_OP)
            self.expression()
            self.match(TokenType.PAREN_CL)
        elif self.checkToken(TokenType.LEN):
            print("LEN")
            self.nextToken()
            self.match(TokenType.PAREN_OP)
            self.expression()
            self.match(TokenType.PAREN_CL)
        else:
            self.primary(tokens)
            # Can have 0 or more +/- and expressions.
            while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS) or self.checkToken(TokenType.ASTERISK):
                if self.checkToken(TokenType.PLUS):
                    tokens.append("+")
                elif self.checkToken(TokenType.MINUS):
                    tokens.append("-")
                elif self.checkToken(TokenType.ASTERISK):
                    tokens.append("*")
                self.nextToken()
                tokens = self.primary(tokens)

        return tokens
            
   
    def primary(self,tokens):
        print("PRIMARY (" + self.curToken.text + ")")
        if self.checkToken(TokenType.NUMBER): 
            tokens.append(self.curToken.text)
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
            tokens.append(self.curToken.text)
            self.nextToken()
            if self.checkToken(TokenType.BRACKET_OP):
                print("INDICE DE LISTA")
                tokens.append(self.curToken.text)
                self.nextToken()
                tokens.append(self.curToken.text)
                print(f"INDICE {self.curToken.text}")
                self.nextToken()
                tokens.append(self.curToken.text)
                self.match(TokenType.BRACKET_CL)
        elif self.checkToken(TokenType.BRACKET_OP):
            tokens.append(self.curToken.text)
            self.nextToken()
            tokens.append(self.curToken.text)
            self.match(TokenType.BRACKET_CL)
        elif self.checkToken(TokenType.BRACKET_CL):
            pass
        else:
            # Error!
            self.abort("Unexpected token at " + self.curToken.text)
        return tokens
