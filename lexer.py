from ast import keyword
import enum
import sys
from queue import LifoQueue
stack = LifoQueue()
stack.put(0)
class Lexer:
    def __init__(self, inp):
        self.source = inp + '\n'
        self.curChar = ''
        self.curPos = - 1
        self.nextChar()
        self.line_counter = 0

    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]

    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

    def abort(self,message):
        sys.exit("Lexing error. " + message)
    def skipWhitespace(self):
        while self.curChar == ' ':
            self.nextChar()
    def skipComment(self):
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()
    def indentationchecker(self,count):
        original_value = stack.get()
        if count > original_value:
            stack.put(original_value)
            stack.put(count)
            return 1
        elif count < original_value:
            indent_anterior = stack.get()
            if count != indent_anterior:
                raise Exception("Problema de indentación, verificar que las indentaciones correspondan")
            else:
                stack.put(count)
                return 2
        elif count == original_value:
            stack.put(original_value)
            return 3
        else: return 4
    def dedentationchecker(self,count):
        original_value = stack.get()
        if count < original_value:
            indent_anterior = stack.get()
            if count != indent_anterior:
                raise Exception("Problema de indentación, verificar que las indentaciones correspondan")
            else:
                stack.put(indent_anterior)
                stack.put(count) 
                return 1
        else:
            stack.put(count)
            return 2
    def indentation_validator(self,count):
        original_value = stack.get()
        if count != original_value:
                raise Exception("Problema de indentación, verificar que las indentaciones correspondan")
        else:
            return


    def getToken(self):
        
        self.skipWhitespace()
        self.skipComment()
        token = None
        if self.curChar == "+":
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '>':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)
        elif self.curChar == '<':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)
        elif self.curChar == '=':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)
        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.abort("Se esperaba un !=, se obtuvo !" + self.peek())
        elif self.curChar == '\"':
            self.nextChar()
            startPos = self.curPos

            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\n':
                    self.abort("String no valida, caracter ilegal")
                self.nextChar()
            tokText = self.source[startPos : self.curPos]
            token =Token(tokText,TokenType.STRING)
        elif self.curChar == '(':
            token = Token(self.curChar,TokenType.PAREN_OP)
        elif self.curChar == ')':
            token = Token(self.curChar,TokenType.PAREN_CL)

        elif self.curChar == '\n':
            self.line_counter += 1
            if self.peek() == ' ': 
                counted_spaces = 0
                self.nextChar()
                startPos = self.curPos
            elif self.peek() == '\t':
                counted_spaces  = 4
                self.nextChar()
                startPos = self.curPos

                while self.peek() == ' ' or self.peek() == '\t':
                    if self.peek() == ' ':
                        counted_spaces += 1
                    else:
                        counted_spaces += 4
                    self.nextChar()
                
                tokText = self.source[startPos: self.curPos]
                indentation_token = self.indentationchecker(counted_spaces)
                if(indentation_token == 1):
                    token = Token(tokText,TokenType.INDENTATION)
                elif(indentation_token == 2):
                    token = Token(tokText,TokenType.DEDENTATION)
                    
                else:
                    token = Token(tokText, TokenType.NEWLINE)
            elif self.peek() == '\t':
                counted_spaces = 0
                self.nextChar()
                startPos = self.curPos

                while self.peek() == ' ' or self.peek() == '\t':
                    if self.peek() == ' ':
                        counted_spaces += 1
                    else:
                        counted_spaces += 4
                    self.nextChar()
                tokText = self.source[startPos: self.curPos]
                indentation_token = self.indentationchecker(counted_spaces)
                if(indentation_token == 1):
                    token = Token(tokText,TokenType.INDENTATION)
                elif(indentation_token == 2):
                    token = Token(tokText,TokenType.DEDENTATION)
                    
                else:
                    token = Token(tokText, TokenType.NEWLINE)
            else:
                counted_spaces = 0
                dedentation_token = self.dedentationchecker(counted_spaces)
                if dedentation_token == 1:
                    token = Token(self.curChar,TokenType.DEDENTATION)
                else:
                    token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == '\0':
            token = Token('', TokenType.EOF)
        elif self.curChar == ':':
            token = Token(self.curChar, TokenType.COL)
        elif self.curChar == '[':
            token = Token(self.curChar, TokenType.BRACKET_OP)
        elif self.curChar == ']':
            token = Token(self.curChar, TokenType.BRACKET_CL)
        elif self.curChar == ',':
            token = Token(self.curChar, TokenType.COMMA)
        elif self.curChar == '.':
            token = Token(self.curChar, TokenType.DOT)

        elif self.curChar.isdigit():
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.':
                self.nextChar()

                if not self.peek().isdigit():
                    self.abort("Caracter ilegal en el número")
                while self.peek().isdigit():
                    self.nextChar()
            tokText = self.source[startPos : self.curPos + 1]
            token = Token(tokText, TokenType.NUMBER)
        elif self.curChar.isalpha():
            startPos = self.curPos
            while self.peek().isalnum():
                self.nextChar()
            tokText = self.source[startPos : self.curPos + 1]
            keyword = Token.checkIfkeyword(tokText)
            if keyword == None:
                token = Token(tokText, TokenType.IDENT)
                
            else: 
                token = Token(tokText, keyword)
        else:
            self.abort("Unknown token: " + self.curChar)
        self.nextChar()
        return token


class Token:
    def __init__(self,tokenText,tokenKind):
        self.text = tokenText
        self.kind = tokenKind
    @staticmethod
    def checkIfkeyword(tokenText):
        for kind in TokenType:
            if kind.name.lower() == tokenText.lower() and kind.value >= 100 and kind.value < 200:
                return kind
        return None

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    INDENTATION = 4
    DEDENTATION = 5
    # Palabras reservadas
    PRINT = 101
    DEF = 102
    FOR = 103
    RETURN = 104
    IN = 105
    RANGE = 106
    LEN = 107
    ENDIF = 108
    INPUT = 109
    INT = 110
    APPEND = 111
    IF = 112
    #simbolos
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
    PAREN_OP = 212
    PAREN_CL = 213
    COL = 214
    BRACKET_OP = 215
    BRACKET_CL = 216
    COMMA = 217
    DOT = 218 
