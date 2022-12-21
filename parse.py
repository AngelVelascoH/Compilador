from lib2to3.pgen2 import token
import sys
from lexer import *

# Parser object keeps track of current token and checks if the code matches the grammar.
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
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
        self.nextToken()
    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    def abort(self, message):
        sys.exit("Error. " + message)

    #reglas de la gramatica de Python
    def file(self):
        print("PROGRAMA")
        if self.checkToken(TokenType.INDENTATION):
            self.abort("Indentacion no esperada")
        #saltar los saltos de linea no necesarios.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
        #analizar todas las sentencias en el programa.
        while not self.checkToken(TokenType.EOF):
            self.statement()
        print("FIN PROGRAMA")
    def statement(self):
        #Checar el primer token para ver el tipo de sentencia.
        #print
        
        if self.checkToken(TokenType.PRINT):
            print("SENTENCIA PRINT")
            self.nextToken()
            self.match(TokenType.PAREN_OP)
            if self.checkToken(TokenType.STRING):
                self.match(TokenType.STRING)
            else:
                self.argumentos()
            self.match(TokenType.PAREN_CL)

        elif self.checkToken(TokenType.DEF):
            print("FUNCION+++")
            self.nextToken()
            self.match(TokenType.IDENT)
            self.match(TokenType.PAREN_OP)
            self.argumentos()
            self.match(TokenType.PAREN_CL)
            self.match(TokenType.COL)
            self.match(TokenType.INDENTATION)
            self.statement()
            while self.checkToken(TokenType.NEWLINE):
                self.nextToken()
                self.statement()
            if self.checkToken(TokenType.RETURN):
                self.returnStatement()
            else:
                self.match(TokenType.DEDENTATION)
            print("FIN FUNCION---")

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
                self.statement()
                while self.checkToken(TokenType.NEWLINE):
                    self.nextToken()
                    self.statement()
                self.match(TokenType.DEDENTATION)
            else:
                self.match(TokenType.IDENT)
                self.match(TokenType.COL)
                self.match(TokenType.INDENTATION)
                self.statement()
                self.match(TokenType.DEDENTATION)
            print("FIN SENTENCIA FOR")



        elif self.checkToken(TokenType.IDENT):
            if self.checkPeek(TokenType.EQ):
                print("ASIGNACION")
                self.nextToken()
                self.match(TokenType.EQ)
                if self.checkToken(TokenType.IDENT):
                    if self.checkPeek(TokenType.PAREN_OP):
                        self.statement()
                    else:
                        self.expression()
                else:
                    self.expression()
            elif self.checkPeek(TokenType.PAREN_OP):
                print("LLAMADA FUNCION")
                self.nextToken()
                self.match(TokenType.PAREN_OP)
                self.argumentos()
                self.match(TokenType.PAREN_CL)
            else:
                print("METODO")
                self.nextToken()
                self.match(TokenType.DOT)
                self.statement()
                
        elif self.checkToken(TokenType.NEWLINE):
            if self.checkPeek(TokenType.EOF):
                print("---FIN DEL MAIN---")
                self.nextToken()
            else:
                print("---INICIO DEL MAIN---")
                self.nextToken()
                self.statement()
                while self.checkToken(TokenType.NEWLINE):
                    if self.checkToken(TokenType.EOF):
                        print("___Main___")
                        break
                    self.nextToken()
                    self.statement()



            
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
        self.expression()
        self.match(TokenType.DEDENTATION)
    def argumentos(self):
        print("ARGUMENTOS")
        if self.checkToken(TokenType.IDENT) or self.checkToken(TokenType.STRING) or self.checkToken(TokenType.NUMBER):
            self.nextToken()
            while self.checkToken(TokenType.COMMA):
                self.nextToken()
                if self.checkToken(TokenType.IDENT) or self.checkPeek(TokenType.STRING) or self.checkPeek(TokenType.NUMBER):
                    self.nextToken()
        if self.checkToken(TokenType.INT):
            self.expression()

                    
    def expression(self):
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
            self.term()
            # Can have 0 or more +/- and expressions.
            while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
                self.nextToken()
                self.term()
                
    def term(self):
        print("TERM")

        self.unary()
        # Can have 0 or more *// and expressions.
        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH):
            self.nextToken()
            self.unary()


    # unary ::= ["+" | "-"] primary
    def unary(self):
        print("UNARY")

        # Optional unary +/-
        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()        
        self.primary()
    def primary(self):
        print("PRIMARY (" + self.curToken.text + ")")

        if self.checkToken(TokenType.NUMBER): 
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
            self.nextToken()
            if self.checkToken(TokenType.BRACKET_OP):
                print("INDICE DE LISTA")
                self.nextToken()
                self.expression()
                self.match(TokenType.BRACKET_CL)
        elif self.checkToken(TokenType.BRACKET_OP):
            self.nextToken()
            self.expression()
            self.match(TokenType.BRACKET_CL)
        elif self.checkToken(TokenType.BRACKET_CL):
            pass
        else:
            # Error!
            self.abort("Unexpected token at " + self.curToken.text)
