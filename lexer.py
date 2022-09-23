import enum


class Lexer:
    def __init__(self, inp):
        self.source = inp + '\n'
        self.curChar = ''
        self.curPos = - 1
        self.nextChar()

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
        pass
    def skipWhitespace(self):
        pass
    def skipComment(self):
        pass
    def getToken(self):
        if self.curChar == '+':
            pass
        if self.curChar == '-':
            pass
        if self.curChar == '*':
            pass
        if self.curChar == '/':
            pass
        if self.curChar == '\n':
            pass
        if self.curChar == '\0':
            pass
        else:
            pass
        self.nextChar()


class Token:
    def __init__(self,tokenText,tokenKind):
        self.text = tokenText
        self.kind = tokenKind

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
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
