# Compilador
Prototipo del funcionamiento de un compilador, elaborado como proyecto para para el curso de compiladores.

El objetivo del programa, es poder aplicar los fundamentos teóricos detras del funcionamiento de un compilador, para crear un compilador capaz de transformar código básico en python en c++, el proyecto no esta completo al 100%, pues se concluyó el curso con la finalización del analizador semantico y la generación de código intermedio.

Crear un compilador, es una tarea muy extensa además de compleja, especialmente para lenguajes completos como python y c++, es por ello, que el código se realizó para un script específico de python, el objetivo es demostrar fundamentalmente las fases de un compilador, sin la utilización de librerías.

El proyecto está conformado por 4 programas que permiten la compilación

![image](https://github.com/AngelVelascoH/Compilador/assets/86260733/ba29e734-9e61-4c0c-984a-f96820aa0442)

El programa de lexer, crea una clase Lexer, cuyo objetivo es retornan los tokens que
componen el programa que se le pasa en formato txt, para esto, crearemos
métodos que nos permitan desplazarnos caracter por caracter, con el objetivo de
seguir reglas establecidas para obtener:
palabras reservadas
tokens
simbolos ({}[].:;+-*/)
y a la vez, eliminar comentarios e identificar identaciones




