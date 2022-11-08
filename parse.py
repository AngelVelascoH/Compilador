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
    def statement(self):
        #Checar el primer token para ver el tipo de sentencia.
        #print
        if self.checkToken(TokenType.PRINT):
            print("SENTENCIA PRINT")
            self.nextToken()

            if self.checkToken(TokenType.PAREN_OP):
                self.nextToken()

                if self.checkToken(TokenType.STRING):
                    self.nextToken()
                    if self.checkToken(TokenType.PAREN_CL):
                        self.nextToken()
                else:
                    self.expression()
                    if self.checkToken(TokenType.PAREN_CL):
                        self.nextToken()
                    
                
        elif self.checkToken(TokenType.IF):
            print("SENTENCIA IF")
            self.nextToken()
            self.comparison()

            self.match(TokenType.COL)
            self.match(TokenType.INDENTATION)
            self.nl()


            while not self.checkToken(TokenType.DEDENTATION):
                self.statement()
            self.match(TokenType.DEDENTATION)
        else:
            self.abort(f"Invalid statement at {self.curToken.text} ({self.curToken.kind.name})")
        self.nl()     

    def nl(self):
        print("SALTO DE LINEA")
        if self.checkToken(TokenType.DEDENTATION):
         while self.checkToken(TokenType.DEDENTATION):
            self.nextToken()   
        if self.checkToken(TokenType.NEWLINE):
            while self.checkToken(TokenType.NEWLINE):
                self.nextToken()
                
                
