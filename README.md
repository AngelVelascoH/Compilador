
# **Compilador de Python a C++**


Este proyecto, corresponde a la culminación de la materia de compiladores.

Prototipo del funcionamiento de un compilador, elaborado como proyecto para para el curso de compiladores.

El objetivo del programa, es poder aplicar los fundamentos teóricos detras del funcionamiento de un compilador, para crear un compilador capaz de transformar código básico en python en c++, el proyecto no esta completo al 100%, pues se concluyó el curso con la finalización del analizador semantico y la generación de código intermedio.

Crear un compilador, es una tarea muy extensa además de compleja, especialmente para lenguajes completos como python y c++, es por ello, que el código se realizó para un script específico de python, el objetivo es demostrar fundamentalmente las fases de un compilador, sin la utilización de librerías.

El proyecto está conformado por 4 programas que permiten la compilación

##Resultados

El proyecto está conformado por 4 programas que permiten la compilación:
![image](https://github.com/AngelVelascoH/Compilador/assets/86260733/581a168d-5b96-47cb-937c-967b40bb47ca)


## **Lexer**

El programa de lexer, crea una clase Lexer, cuyo objetivo es retornan los tokens que

componen el programa que se le pasa en formato txt, para esto, crearemos

métodos que nos permitan desplazarnos caracter por caracter, con el objetivo de

seguir reglas establecidas para obtener:

palabras reservadas

tokens

simbolos ({}[].:;+-\*/)

y a la vez, eliminar comentarios e identiꢀcar identaciones:


Para poder correctamente identificar la identación, utilizamos una pila, al igual

que el mismo interprete de python usa, ahí, compararemos con el ultimo indice

que tengamos, para ver si existe o no un espacio o varios, y así llevar orden de los

mismos, también identiꢀcar dedentaciones, y lineas nuevas, pues es fundamental

para los ciclos y funciones la correcta determinación de los mismos.


Finalmente, el lexer, utiliza sus métodos par analizar caracter por caracter, y

agruparlos en caso de que sea necesario, así identificando los tokens y creando un

objeto token que retrornaremos para el parser


## **Parser**

El parser, utiliza los tokens recibidos, y va haciendo match (emparejando) los

tokens con las reglas de la gramática de python, las cuales pueden ser obtenidas de

la siguiente página:

https://inst.eecs.berkeley.edu/~cs164/sp18/python-gram

mar.html

A continuación se muestran algunas de las implementaciones de las reglas de

python, para así, obtener código intermedio que nos permitira traducir

correctamente a c++





## **Emmiter**:

El emisor, solo son funciones que nos permitiran agregar ese codigo a nuestro

programa final:




Una vez contamos con el emisor, fusionaremos el emisor con el parser, creando los

dos analizadores restantes, sintactico y semantico, así, podremos crear el código

necesario para c++

El resultado de unirlos sería algo como esto, solo se muestra el de una función,

pero debería aplicar a todas.





## **Ejecución**


![image](https://github.com/AngelVelascoH/Compilador/assets/86260733/7ae9c9aa-c87d-4148-9a33-4f221cc13243)


### **Identifica los tokens del programa**

![image](https://github.com/AngelVelascoH/Compilador/assets/86260733/7b27fc69-9125-4b4d-8486-c10a32e21e53)



### **Analiza los tokens y los parsea (analizadores sintacticos y semanticos) y crea código intermedio**


![image](https://github.com/AngelVelascoH/Compilador/assets/86260733/8f207703-e427-423d-a8cb-99fc8b331559)



### **Crea el código en c++**

![image](https://github.com/AngelVelascoH/Compilador/assets/86260733/b9ecbd92-7a02-44b6-986e-2c928cba247c)




## **Conclusión**


Evidentemente, el muy pequeño compilador realizado en esta práctica, no podrá compilar cualquier código en python, pero fue de gran utilidad para poder comprender el funcionamiento interno de un compilador.






