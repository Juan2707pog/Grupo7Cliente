# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Segunda práctica
# ===========================================================

#   APELLIDOS, NOMBRE: Reina Montes, José Antonio
#   DNI: 30263968Q

# Práctica 2: Programación orientada a objetos
# =================================

# En esta práctica veremos algunos ejercicios de Python, con una
# orientación a objetos.

# -----------
# EJERCICIO 1
# -----------
#
# Escribir una clase general llamada "Figura" con los atributos de
# cualquier figura geométrica. Posteriormente se pide implementar las
# clases "Círculo", "Cuadrado" y "Triángulo" con sus correspondientes
# atributos y funciones.

# En este ejercicio os tendréis que enfrentar con la herencia entre clases,
# colocando toda la información general en la clase "Figura" y 
# posteriormente sobreescribir esos métodos con los diferentes
# comportamientos de cada figura.

# Por ejemplo:
#
# La clase "Cuadrado" tendrá una función area donde se devolverá el 
# area de un cuadrado.
#
# Nota: Son necesarios los siguientes datos, perímetro, area, diámetro.


import math

class Figura():

    base = int(input('Cuánto es la base del triangulo:'))
    altura = int(input('Cuánto es la altura del triangulo:'))       #Pregunta los datos necesarios para los calculos
    lado1 = int(input('Cuánto es el primer lado del triangulo:'))
    lado2 = int(input('Cuánto es el segundo lado del triangulo:'))
    lado3 = int(input('Cuánto es el  tercer lado del triangulo:'))
    baseR = int(input('Cuánto es la base del rectangulo:')) 
    alturaR = int(input('Cuánto es la altura del rectangulo:'))
    radio = int(input('Cuánto es el radio del circulo: '))


    def __init__(self, base, altura, lado1, lado2, lado3, baseR, alturaR, radio):

        self.base = base
        self.altura = altura            
        self.lado1 = lado1
        self.lado2 = lado2                  #Referenciamos las clases
        self.lado3 = lado3
        
        self.baseR = baseR
        self.alturaR = alturaR

        self.radio = radio
        

    def areaFigura(self):
        Triangulo.areaFigura(Triangulo)
        Rectangulo.areaFigura(Rectangulo)               #Representamos als instacias con esas palabras
        Circulo.areaFigura(Circulo)

    def perimetroFigura(self):
        Triangulo.perimetroFigura(Triangulo)
        Rectangulo.perimetroFigura(Rectangulo)
        Circulo.perimetroFigura(Circulo)

    def diametroFigura(self):
       Circulo.diametroFigura(Circulo)


class Triangulo(Figura):            #El triángulo


    def __init__(self, base, altura, lado1, lado2, lado3):

        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetroFigura(self):
        print('Perimetro del Triangulo: ',self.lado1 + self.lado2 + self.lado3)     #Este el perímetro

    def areaFigura(self):
        print('Area del Triangulo: ', self.base * self.altura / 2)          #La operación que calcula el área






class Rectangulo(Figura):                           #El rectángulo
    def __init__(self, alturaR, baseR):

        self.alturaR = alturaR                  
        self.baseR = baseR

    def areaFigura(self):
        print('Area del Rectangulo: ', self.baseR * self.alturaR)       #lo mismo las operaciónes que se nos piden

    def perimetroFigura(self):
        print('Perimetro del Rectangulo: ', 2 * self.baseR + 2 * self.alturaR)



class Circulo(Figura):
    def __init__(self, radio):              

        self.radio = radio                                  #El circulo con la diferencia que este se pide el radio

    def diametroFigura(self):
        print('Diametro del Circulo: ', 2*self.radio)           #Con el radio ya se calcula directamente el diámetro

    def areaFigura(self):
        print('Area del Circulo: ', 2*math.pi*self.radio**2)
    
    def perimetroFigura(self):
        print('Perimetro del Circulo: ', 2*math.pi*self.radio)

   


Figura.areaFigura(Figura)
Figura.perimetroFigura(Figura)
Figura.diametroFigura(Figura)