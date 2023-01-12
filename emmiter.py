class Emmiter:
    def __init__(self,fullpath):
        self.fullpath = fullpath
        self.header = ""
        self.code = ""

    def emmit(self,code):
        self.code += code
    
    def emmitLine(self,code):
        self.code += code + '\n'

    def headerLine(self,code):
        self.header += code + '\n'

    def writeFile(self):
        with open(self.fullpath, 'w') as outputfile:
            outputfile.write(self.header + '\n' + self.code)
