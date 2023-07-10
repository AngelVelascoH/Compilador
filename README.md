<a name="br1"></a> 

INSTITUTO POLITÉCNICO NACIONAL

ESCUELA SUPERIOR DE CÓMPUTO

2022-2

Proyecto Final

Compilador de PYTHON a C++

COMPILADORES

DOCENTE:

Sánchez Brito Miguel

AUTOR:

Velasco Huerta Angel Eduardo

GRUPO: 3CV13

CIUDAD DE MÉXICO, ENERO 2023



<a name="br2"></a> 

Compilador de Python a C++

Compiladores

Este proyecto, corresponde a la culminación de la materia de compiladores, la cuál,

es de gran importancia para nuestra ya avanzada formación de ingenieros en

sistemas, ya que solemos usarlos practicamente para cualquier trabajo que

realicemos, ya que son un concepto fundamental de las computadoras.

¿Qúe es un compilador?

Un compilador es uno de los pilares de la programación y de cómo entender la

comunicación entre un lenguaje de alto nivel y una máquina. Al poder conocer el

funcionamiento de este paso intermedio nos permitirá desarrollar y programar de

una forma más precisa los lenguajes de alto nivel.

Tradicionalmente los compiladores generaban código máquina de inferior calidad

que el que podían escribir programadores humanos, pero actualmente los

compiladores proporcionan hoy en día un código máquina de alta calidad

pequeño y rápido, haciendo poco atractiva la programación en ensamblador,

programación que en asignaturas como está ya simplemente se menciona por

conocerla pero no se realiza un estudio para aprender este tipo de programación.

Los programadores de ensamblador siguen teniendo ventaja en cuanto a que

disponen de un mayor conocimiento global del programa que les permite realizar

determinadas optimizaciones del código que resultan muy difíciles para los

compiladores.

Un intérprete lee un programa fuente ejecutable, escrito en un lenguaje de

programación de alto nivel, así como datos para este programa, y ejecuta el

programa contra los datos para producir algunos resultados. Un ejemplo es el



<a name="br3"></a> 

intérprete de shell de Unix, que ejecuta comandos del sistema operativo de forma

interactiva.

Hay que tener en cuenta que tanto los intérpretes como los compiladores (como

cualquier otro programa) están escritos en un lenguaje de programación de alto

nivel (que puede ser diferente del idioma que aceptan) y se traducen en código

máquina.

Por ejemplo, un intérprete de Java puede escribirse completamente en C o incluso

en Java. El programa fuente del intérprete es independiente de la máquina ya que

no genera código de máquina.

Un intérprete generalmente es más lento que un compilador porque procesa e

interpreta cada enunciado de un programa tantas veces como el número de

evaluaciones de esta aꢀrmación. Por ejemplo, cuando se interpreta un bucle for, las

aꢀrmaciones dentro del cuerpo for-loop se analizarán y evaluarán en cada paso del

bucle. Algunos lenguajes, como Java y Lisp, vienen con un intérprete y un

compilador. Los programas fuente de Java (clases Java con extensión .java) son

traducidos por el compilador javac en archivos de códigos de bytes (con extensión

.class).

El intérprete de Java, llamado Java Virtual Machine (JVM), en realidad puede

interpretar códigos de bytes directamente o puede compilarlos internamente en

código máquina y luego ejecutar ese código.

Los compiladores son procesos complejos debido a que tienen varias fases por las

que un programa fuente debe de pasar antes de convertirse en un programa

ejecutable, los pasos son los siguiente



<a name="br4"></a> 

¿Es nuestro proyecto un compilador?

Claro que lo es, ya entendida la diferencia entre un compilador y un interprete,

sabemos que el interprete solo busca la ejecución del código sin importar el

lenguaje que tengamos, así, python es un lenguaje que utiliza un interprete, pero el

objetivo ꢀnal de nuestro software, es poder realizar una traducción de lenguajes,

que si analizamos un poco, nos daremos cuenta que es un compilador, solamente

que aquí no usaremos lenguaje máquina, ya que además de ser muy tedioso,

existen cientos de compiladores que ya hacen eso, lo interesante es aplicar el

conocimiento adquirido del funcionamiento de un compilador, y aplicarlo para

lograr nuestro objetivo.

¿Cómo se compone un compilador?

Un compilador, se compone de lo siguiente:

**Analizador léxico:**

El analizador léxico o lexicográꢀco (Scanner en inglés) es la primera etapa del

proceso de compilación, el cual se encarga de dividir el programa en Tokens, los

cuales, según una tabla de símbolos deꢀnida por el mismo lenguaje.

De esta forma cada token del programa es clasiꢀcado según su signiꢀcado para ser

procesados en la segunda etapa del proceso de compilación.

**Analizador sintáctico:**

El analizador sintáctico (Parse en inglés), es la segunda fase del proceso de

compilación y tiene como ꢀnalidad la generación de un [Árbol](http://www.oscarblancarteblog.com/2014/08/22/estructura-de-datos-arboles/)[ ](http://www.oscarblancarteblog.com/2014/08/22/estructura-de-datos-arboles/)sintáctico, el cual no

es más que una estructura de datos compleja que permite representar de una

forma más simple al programa fuente.



<a name="br5"></a> 

Los compiladores modernos utilizan estructuras de objetos para representa a un

programa, de esta forma existe una clase especíꢀca para representa cada posible

token de nuestra tabla de símbolos.

**Analizador semántico:**

El analizador semántico es el último paso antes de empezar a compilar realmente el

código, prepara el programa para ser compilado. El analizador semántico parte del

árbol sintáctico abstracto y tiene la ꢀnalidad de validar los puntos más ꢀnos del

programa, como por ejemplo, validar compatibilidad en tipos de datos, que la

variable utilizada en una instrucción este previamente declara o que estén dentro

del contexto, si implementamos una interface que todos los métodos estén

deꢀnidos, etc.

El analizador semántico es el que analiza que todo el programa tenga un

signiꢀcado exacto y que este no pueda fallar en tiempo de ejecución,

Si bien, podemos seguir puntualmente la elaboración teórica de un compilador,

durante el curso, también aprendimos que podemos utilizar nuestra creatividad

combinada con una buena logica para programar, y obtener un resultado similar

utilizando expresiones regulares.

Expresiones Regulares

En [cómputo](https://es.wikipedia.org/wiki/Ciencia_computacional_te%C3%B3rica)[ ](https://es.wikipedia.org/wiki/Ciencia_computacional_te%C3%B3rica)[teórico](https://es.wikipedia.org/wiki/Ciencia_computacional_te%C3%B3rica)[ ](https://es.wikipedia.org/wiki/Ciencia_computacional_te%C3%B3rica)y teoría de [lenguajes](https://es.wikipedia.org/wiki/Lenguaje_formal)[ ](https://es.wikipedia.org/wiki/Lenguaje_formal)[formales](https://es.wikipedia.org/wiki/Lenguaje_formal), una expresión regular, o

expresión racional, también son conocidas como regex o regexp, por su

contracción de las palabras inglesas regular expression, es una secuencia de

[caracteres](https://es.wikipedia.org/wiki/Car%C3%A1cter_\(tipo_de_dato\))[ ](https://es.wikipedia.org/wiki/Car%C3%A1cter_\(tipo_de_dato\))que conforma un patrón de búsqueda. Se utilizan principalmente para

la [búsqueda](https://es.wikipedia.org/wiki/B%C3%BAsqueda_de_patrones)[ ](https://es.wikipedia.org/wiki/B%C3%BAsqueda_de_patrones)[de](https://es.wikipedia.org/wiki/B%C3%BAsqueda_de_patrones)[ ](https://es.wikipedia.org/wiki/B%C3%BAsqueda_de_patrones)[patrones](https://es.wikipedia.org/wiki/B%C3%BAsqueda_de_patrones)[ ](https://es.wikipedia.org/wiki/B%C3%BAsqueda_de_patrones)de cadenas de caracteres u operaciones de sustituciones.

Las expresiones regulares son patrones utilizados para encontrar una determinada

combinación de caracteres dentro de una [cadena](https://es.wikipedia.org/wiki/Cadena_de_texto)[ ](https://es.wikipedia.org/wiki/Cadena_de_texto)[de](https://es.wikipedia.org/wiki/Cadena_de_texto)[ ](https://es.wikipedia.org/wiki/Cadena_de_texto)[texto](https://es.wikipedia.org/wiki/Cadena_de_texto). Las expresiones



<a name="br6"></a> 

regulares proporcionan una manera muy ꢁexible de buscar o reconocer cadenas de

texto.

La mayoría de las formalizaciones proporcionan los siguientes constructores: una

expresión regular es una forma de representar los [lenguajes](https://es.wikipedia.org/wiki/Lenguaje_regular)[ ](https://es.wikipedia.org/wiki/Lenguaje_regular)[regulares](https://es.wikipedia.org/wiki/Lenguaje_regular)[ ](https://es.wikipedia.org/wiki/Lenguaje_regular)(ꢀnitos o

inꢀnitos) y se construye utilizando [caracteres](https://es.wikipedia.org/wiki/Tipograf%C3%ADa)[ ](https://es.wikipedia.org/wiki/Tipograf%C3%ADa)del [alfabeto](https://es.wikipedia.org/wiki/Alfabeto)[ ](https://es.wikipedia.org/wiki/Alfabeto)sobre el cual se deꢀne el

[lenguaje](https://es.wikipedia.org/wiki/Lenguaje).

Sin embargo, en el presente trabajo, se optó por seguir la teoría estricta de la

creación de un compilador, pues el trabajo a realizar no es trivial, y el seguir

correctamente los pasos sería una manera mas organizada y limpia de trabajar (en

mi opinion)

Resultados

El proyecto está conformado por 4 programas que permiten la compilación:

Empecemos por el lexer.py:



<a name="br7"></a> 

El programa de lexer, crea una clase Lexer, cuyo objetivo es retornan los tokens que

componen el programa que se le pasa en formato txt, para esto, crearemos

métodos que nos permitan desplazarnos caracter por caracter, con el objetivo de

seguir reglas establecidas para obtener:

palabras reservadas

tokens

simbolos ({}[].:;+-\*/)

y a la vez, eliminar comentarios e identiꢀcar identaciones:

from ast import keyword

import enum

import sys

from queue import LifoQueue

stack = LifoQueue()

stack.put(0)

class Lexer:

def \_\_init\_\_(self, inp):

self.source = inp + '\n'

self.curChar = ''

self.curPos = - 1

self.nextChar()

self.line\_counter = 0

def nextChar(self):

self.curPos += 1

*if* self.curPos >= len(self.source):

self.curChar = '\0'

*else*:



<a name="br8"></a> 

self.curChar = self.source[self.curPos]

def peek(self):

*if* self.curPos + 1 >= len(self.source):

*return* '\0'

*return* self.source[self.curPos+1]

def abort(self,message):

sys.exit("Lexing error. " + message)

def skipWhitespace(self):

*while* self.curChar == ' ':

self.nextChar()

def skipComment(self):

*if* self.curChar == '#':

*while* self.curChar != '\n':

self.nextChar()

Para poder correctamente identiꢀcar la identación, utilizamos una pila, al igual

que el mismo interprete de python usa, ahí, compararemos con el ultimo indice

que tengamos, para ver si existe o no un espacio o varios, y así llevar orden de los

mismos, también identiꢀcar dedentaciones, y lineas nuevas, pues es fundamental

para los ciclos y funciones la correcta determinación de los mismos.

def indentationchecker(self,count):

original\_value = stack.get()

*if* count > original\_value:

stack.put(original\_value)



<a name="br9"></a> 

stack.put(count)

*return* 1

*elif* count < original\_value:

indent\_anterior = stack.get()

*if* count != indent\_anterior:

*raise* Exception("Problema de indentación,

verificar que las indentaciones correspondan")

*else*:

stack.put(count)

*return* 2

*elif* count == original\_value:

stack.put(original\_value)

*return* 3

*else*: *return* 4

def dedentationchecker(self,count):

original\_value = stack.get()

*if* count < original\_value:

indent\_anterior = stack.get()

*if* count != indent\_anterior:

*raise* Exception("Problema de indentación,

verificar que las indentaciones correspondan")

*else*:

stack.put(indent\_anterior)

stack.put(count)

*return* 1

*else*:

stack.put(count)

*return* 2



<a name="br10"></a> 

def indentation\_validator(self,count):

original\_value = stack.get()

*if* count != original\_value:

*raise* Exception("Problema de indentación,

verificar que las indentaciones correspondan")

*else*:

*return*

Finalmente, el lexer, utiliza sus métodos par analizar caracter por caracter, y

agruparlos en caso de que sea necesario, así identiꢀcando los tokens y creando un

objeto token que retrornaremos para el parser, a continuación solo se muestran

algunos casos de la gran cantidad de tokens posibles, los cuales fueron

implementados, (ver código fuente)

**def getToken(self):**

**self.skipWhitespace()**

**self.skipComment()**

**token = None**

***if* self.curChar == "+":**

**token = Token(self.curChar, TokenType.PLUS)**

***elif* self.curChar == '-':**

**token = Token(self.curChar, TokenType.MINUS)**

***elif* self.curChar == '\*':**

**token = Token(self.curChar, TokenType.ASTERISK)**

***elif* self.curChar == '/':**

**token = Token(self.curChar, TokenType.SLASH)**

***elif* self.curChar == '>':**



<a name="br11"></a> 

***if* self.peek() == '=':**

**lastChar = self.curChar**

**self.nextChar()**

**token = Token(lastChar + self.curChar,**

**TokenType.GTEQ)**

***else*:**

**token = Token(self.curChar, TokenType.GT)**

***elif* self.curChar == '<':**

***if* self.peek() == '=':**

**lastChar = self.curChar**

**self.nextChar()**

**token = Token(lastChar + self.curChar,**

**TokenType.LTEQ)**

***else*:**

**token = Token(self.curChar, TokenType.LT)**

Parser

El parser, utiliza los tokens recibidos, y va haciendo match (emparejando) los

tokens con las reglas de la gramática de python, las cuales pueden ser obtenidas de

la siguiente página:

https://inst.eecs.berkeley.edu/~cs164/sp18/python-gram

mar.html

A continuación se muestran algunas de las implementaciones de las reglas de

python, para así, obtener código intermedio que nos permitira traducir

correctamente a c++



<a name="br12"></a> 

*elif* self.checkToken(TokenType.APPEND):

print("SENTENCIA APPEND")

self.nextToken()

self.match(TokenType.PAREN\_OP)

self.expression()

self.match(TokenType.PAREN\_CL)

*elif* self.checkToken(TokenType.INPUT):

print("SENTENCIA INPUT")

self.nextToken()

self.match(TokenType.PAREN\_OP)

self.match(TokenType.STRING)

self.match(TokenType.PAREN\_CL)

*elif* self.checkToken(TokenType.INT):

print("SENTENCIA INT")

self.nextToken()

self.match(TokenType.PAREN\_OP)

self.expression()

self.match(TokenType.PAREN\_CL)

*elif* self.checkToken(TokenType.FOR):

print("SENTENCIA FOR")

self.nextToken()

self.match(TokenType.IDENT)

self.match(TokenType.IN)

*if* self.checkToken(TokenType.RANGE):

self.nextToken()



<a name="br13"></a> 

self.match(TokenType.PAREN\_OP)

self.expression()

self.match(TokenType.COMMA)

self.expression()

self.match(TokenType.PAREN\_CL)

self.match(TokenType.COL)

self.match(TokenType.INDENTATION)

self.statement(main\_check)

*while* self.checkToken(TokenType.NEWLINE):

self.nextToken()

self.statement(main\_check)

self.match(TokenType.DEDENTATION)

*else*:

self.match(TokenType.IDENT)

self.match(TokenType.COL)

self.match(TokenType.INDENTATION)

self.statement(main\_check)

self.match(TokenType.DEDENTATION)

print("FIN SENTENCIA FOR")

Emmiter:

El emisor, solo son funciones que nos permitiran agregar ese codigo a nuestro

programa ꢀnal:



<a name="br14"></a> 

class Emmiter:

def \_\_init\_\_(self,fullpath):

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

*with* open(self.fullpath, 'w') *as* outputfile:

outputfile.write(self.header + '\n' + self.code)

Una vez contamos con el emisor, fusionaremos el emisor con el parser, creando los

dos analizadores restantes, sintactico y semantico, así, podremos crear el código

necesario para c++

El resultado de unirlos sería algo como esto, solo se muestra el de una función,

pero debería aplicar a todas.



<a name="br15"></a> 

*if* self.checkToken(TokenType.PRINT):

print("SENTENCIA PRINT")

self.nextToken()

self.match(TokenType.PAREN\_OP)

*if* self.checkToken(TokenType.STRING):

*if* main\_check == 1:

self.emmiter.headerLine(f"cout<<\"{self.curToken.text}\"<<endl;

")

*else*:

self.emmiter.emmitLine(f"cout<<\"{self.curToken.text}\"<<endl;"

)

self.match(TokenType.STRING)

*else*:

args = []

args = self.argumentos(args)

args = '<< \" \"<< '.join(args)

*if* main\_check == 1:

self.emmiter.headerLine(f"cout<<{args}<<endl;")

*else*:

self.emmiter.emmitLine(f"cout<<{args}<<endl;")

self.match(TokenType.PAREN\_CL)

Aquí ya creamos código c++ mientras encontremos que la sintaxis corresponde a

ciertos casos traducibles, como la sentencia print —> cout<<



<a name="br16"></a> 

Finalmente, el main, programa que solo uniꢀcara estos analizadores para crear

nuestro compilador:

from lexer import \*

from parse import \*

import io

def main():

print("Compilador PYTHON ------> C++")

print("\n")

f = io.open('proyectoFinal.txt',mode='r',encoding="utf-8")

inp = '\n' + f.read()

lexer = Lexer(inp)

token = lexer.getToken()

*while* token.kind != TokenType.EOF:

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



<a name="br17"></a> 

Ejecución

**Identiꢀca los tokens del programa**

**Analiza los tokens y los parsea (analizadores sintacticos y semanticos) y**

**crea código intermedio**

**Crea el código en c++**



<a name="br18"></a> 



<a name="br19"></a> 

Conclusión

**Ventajas:**

● Crea código seguro y limpio, al no tener todo el lenguaje de python

implementado, se logró crear las expresiones y transformaciones de la

manera más precisa posible

● Mantiene variables y funciones con el mismo nombre

● Identiꢀca errores si existen previamente

**Desventajas:**

● No contiene todo el lenguaje de python, por lo que está limitado a traducir

todos los programas que se puedan crear, sino solo los que contienen los

métodos y opciones disponibles en el software actual (aunque este se puede

mejorar gradualmente de manera sencilla, pues solo es cuestión de agregar

los casos correspondientes)

● No es preciso con los tipos, pues python es un lenguaje contextualizado, y

requiere más para determinar que tipo de valores puede adquirir una

función o una variable

La creación de un compilador fue todo un reto, a nivel lógico y teórico, lo cual será

de gran ayuda para el desarrollo a futuro de programas o software que requieran

hacer analisis tan profundos a nivel lógico, además, aprendí mucho más acerca de

los dos lenguajes implicados, pues si quieres realizar una compilación, primero

debes entender bien como funcionan ambos lenguajes, para así aplicar las reglas y

su funcionamiento interno al compilador, como por ejemplo fue el caso de las

identaciones, o los tipos abstractos en C++, en conclusion, me pareció un

proyecto muy interesante y desaꢀante que me ayudará mucho en mi crecimiento

como programador e ingeniero.



<a name="br20"></a> 

