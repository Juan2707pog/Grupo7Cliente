# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Segunda práctica
# ===========================================================

#   APELLIDOS, NOMBRE: Villar Mendez, Carlos Manuel
#   DNI: 3021661C

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

# Clase general figura
class Figura():
    # input para preguntar los datos necesarios para los calculos
    altura = int(input('\nIngresar altura triangulo:'))
    base = int(input('Ingresar base triangulo:'))
    lado1 = int(input('\nIngresar primer lado del triangulo:'))
    lado2 = int(input('Ingresar segundo lado del triangulo:'))
    lado3 = int(input('Ingresar tercer lado del triangulo:'))
    alturaR = int(input('\nIngresar altura rectangulo:'))
    baseR = int(input('Ingresar base rectangulo:'))
    radio = int(input('\nIngresa el radio del circulo: '))


    def __init__(self, altura, base, lado1, lado2, lado3, alturaR, baseR,radio):

        self.altura = altura
        self.base = base
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.radio = radio

        self.alturaR = alturaR
        self.baseR = baseR

    def areaFigura(self):
        Triangulo.areaFigura(Triangulo)
        Rectangulo.areaFigura(Rectangulo)
        Circulo.areaFigura(Circulo)

    def perimetroFigura(self):
        Triangulo.perimetroFigura(Triangulo)
        Rectangulo.perimetroFigura(Rectangulo)
        Circulo.perimetroFigura(Circulo)

    def diametroFigura(self):
       Circulo.diametroFigura(Circulo)

# Clase triangulo donde se forma tanto el area como el perimetro
class Triangulo(Figura):


    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # Calculo el area y perimetro con sus formulas
    def areaFigura(self):
        print('\n****************Resultados****************')
        print('------------------Área------------------')
        print('Area triangulo: ', self.base * self.altura / 2)

    def perimetroFigura(self):
        print('\n------------------Perímetro------------------')
        print('Perimetro triangulo: ',self.lado1 + self.lado2 + self.lado3)

# Clase rectangulo donde se forma tanto el area como el perimetro
class Rectangulo(Figura):
    def __init__(self, alturaR, baseR):

        self.alturaR = alturaR
        self.baseR = baseR
    # Calculo el area y perimetro con sus formulas
    def areaFigura(self):
        print('Area Rectangulo: ', self.baseR * self.alturaR)

    def perimetroFigura(self):
        print('Perimetro Rectangulo: ', 2 * self.baseR + 2 * self.alturaR)

# Clase circulo donde se forma tanto el area como el perimetro y el diametro
class Circulo(Figura):
    def __init__(self, radio):

        self.radio = radio

    # Calculo el area, perimetro y diametro con sus formulas
    def areaFigura(self):
        print('Area Circulo: ', 2*math.pi*self.radio**2)
    
    def perimetroFigura(self):
        print('Perimetro Circulo: ', 2*math.pi*self.radio)

    def diametroFigura(self):
        print('\n------------------Diámetro------------------')
        print('Diametro Circulo: ', 2*self.radio)


Figura.areaFigura(Figura)
Figura.perimetroFigura(Figura)
Figura.diametroFigura(Figura)