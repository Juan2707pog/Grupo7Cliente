# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Primera prÃ¡ctica
# ===========================================================

#   APELLIDOS, NOMBRE: José Antonio Reina Montes
#   DNI: 30263968Q

import math

# PrÃ¡ctica 1: IntroducciÃ³n a Python
# =================================

# En esta prÃ¡ctica veremos algunos ejercicios de Python, para ir
# familiarizÃ¡ndonos con el lenguaje.

# -----------
# EJERCICIO 1
# -----------
#
# Escribir una funcion cuadrados(l) que recibiendo una secuencia l de nÃºmeros,
# devuelve la lista de los cuadrados de esos nÃºmeros, en el mismo orden.

# Por ejemplo:
#
# >>> cuadrados([4,1,5.2,3,8])
# [16, 1, 27.040000000000003, 9, 64]

# Hacer dos versiones: una usando un bucle explÃ­cito, y la otra mediante
# definiciÃ³n de listas por comprensiÃ³n.
# ---------------------------------------------------------------------------

def cuadrados1(l):
    x = [ x*x for x in l ]
#return a
#print(cuadrados1([5,6,3,2,1,7]))

def cuadrados2(l):
    x = []
    for i in l:
        x.append(i*i)
    return x

# -----------
# EJERCICIO 2
# -----------
# Definir una funcion vocales_consonantes(s), que reciba una cadena de
# caracteres s (de letras mayÃºsculas) y escribe por pantalla, una a una, si
# sus letras son vocales o  consonantes.
# Ejemplo:
# >>> vocales_consonantes("INTELIGENCIA")
# I es vocal
# N es consonante
# T es consonante
# E es vocal
# L es consonante
# I es vocal
# G es consonante
# E es vocal
# N es consonante
# C es consonante
# I es vocal
# A es vocal
# ---------------------------------------------------------------------------

def vocales_consonantes(s):
    vocales = "AEIOUaeiou"
    for i in s:
        if vocales.find(i)== -1:
            print('{0} es consonante'.format(i))
        else:
            print('{0} es vocal'.format(i))
#print(vocales_consonantes("holaaa"))


# -----------
# EJERCICIO 3
# -----------

# Usando como tÃ©cnica principal la definiciÃ³n de secuancias por comprensiÃ³n,
# definir las siguientes funciones:

# a) Dada una lista de nÃºmeros naturales, la suma de los cuadrados de los
#    nÃºmeros pares de la lista.

# Ejemplo:
# >>> suma_cuadrados([9,4,2,6,8,1])
# 120

def suma_cuadrados(l):
    x = 0
    for i in l:
        if i % 2 == 0:
            x += i*i        
    return x


# b) Dada una lista de nÃºmeros l=[a(1),...,a(n)], calcular el sumatorio de i=1
#    hasta n de i*a(i).

# Ejemplo:

# >>> suma_fÃ³rmula([2,4,6,8,10])
# 110

def suma_formula(l):
    x = len(l)
    y = 0
    l1 = [(i+1)*l[i] for i in range(x)]
    for k in l1:
        y+=k
    return y


# c) Dados dos listas numÃ©ricas de la misma longitud, representado dos puntos
#    n-dimensionales, calcular la distancia euclÃ­dea entre ellos.

# Ejemplo:

# >>> distancia([3,1,2],[1,2,1])
# 2.449489742783178

def distancia(l0,l1):
    return math.sqrt(sum([(x-y)**2 for x,y in zip(l0,l1)])) #al tener el mismo tamaño unimos los datos en el zip

# d) Dada una lista y una funcion de un argumento, devolver la lista de los
#    resultados de aplicar la funcion a cada elelmento de la lista.

# Ejemplo:

# >>> map_mio(abs,[-2,-3,-4,-1])
# [2, 3, 4, 1]

def map_mio(f,l):
    l1 = [ f(x) for x in l]
    return l1

# e) Dada un par de listas (de la misma longitud) y una funcion de dos
#    argumentos, devolver la lista de los resultados de aplicar la funcion a
#    cada par de elementos que ocupan la misma posiciÃ³n en las listas de
#    entrada.

# Ejemplo:
# >>> map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9])
# [6, 4, 10, 13]

def map2_mio(f,l0,l1):
    if(len(l0) == len(l1)):
        return [f(x,y) for x,y in zip(l0,l1)]
    else:
        return 'No tiene el mismo tamaño'


# f) Dada una lista de nÃºmeros, contar el nÃºmero de elementos que sean mÃºltiplos
#    de tres y distintos de cero.

# Ejemplo:

# >>> m3_no_nulos([4,0,6,7,0,9,18])
# 3

def m3_no_nulos(l):
    x = len(l)
    l1 = [ 1 for i in range(x) if (l[i] % 3 == 0 and l[i] != 0)]
    return sum(l1)
#return l1.len()


# f) Dadas dos listas de la misma longitud, contar el nÃºmero de posiciones en
#    las que coinciden los elementos de ambas listas.

# Ejemplo:

# >>> cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# 3

def cuenta_coincidentes(l0,l1):
    x = len(l0)
    y = sum([1 for i in range(x) if l0[i] == l1[i]])
    return y    

# g) Dadas dos listas de la misma longitud, devolver un diccionario que tiene
# como claves las posiciones  en las que coinciden los elementos de ambas
# listas, y como valor de esas claves, el elemento coincidente.

# Ejemplos:

# >>> dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# {1: 2, 3: 8, 4: 9}
# >>> dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6])
# {1: 8, 2: 1, 3: 2, 4: 1}

def dic_posiciones_coincidentes(l0,l1):
    if (len(l0) == len(l1)):
        return {x:l0[x] for x in range(len(l0)) if l0[x] == l1[x]}
    else:
        return 'El tamaño de las listas no es el mismo'


# -----------
# EJERCICIO 4
# -----------
# Un nÃºmero es perfecto si es la suma de todos sus divisores (excepto Ã©l
# mismo). Definir una funciÃ³n filtra_perfectos(n,m,p) que imprime por pantalla
# todos los nÃºmeros perfectos entre n y m que cumplen la condiciÃ³n p. Se pide
# tambiÃ©n que se indiquen los divisores de cada nÃºmero perfecto que se
# imprima.

# Ejemplo:

# >>> filtra_perfectos(3,500, lambda x: True)
# El 6 es perfecto y sus divisores son [1, 2, 3]
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# El 496 es perfecto y sus divisores son [1, 2, 4, 8, 16, 31, 62, 124, 248]

# >>> filtra_perfectos(3,500, lambda x: (x%7==0))
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# ------------------------------------------------------------------------

def divisores(x):
    div = [ i for i in range(1,x) if x%i == 0]
    return div

def filtra_perfectos(a,b,f):
    l1 = [x for x in range(a,b) if f(x)== True and sum(divisores(x)) == x]
    for i in l1:
        print("El {0} es perfecto y sus divisores son {1}".format(i,divisores(i)))
    


##    for x in range(a,b+1):
##        if sum(multiplos(x)) == x:
##            if f(x):
##                print ( "El " , x , " es perfecto y sus divisores son " , multiplos(x))
# -----------
# EJERCICIO 5
# -----------
#
# Supongamos que recibimos un diccionario cuyas claves son cadenas de
# caracteres de longitud uno y los valores asociados son nÃºmeros enteros
# entre 0 y 50.
# Definir una funcion histograma_horizontal(d), que recibiendo un diccionario
# de ese tipo, escribe un histograma de barras horizontales asociado,
# como se ilustra en el siguiente ejemplo:

# >>> d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_horizontal(d1)
# a: *****
# b: **********
# c: ************
# d: ***********
# e: ***************
# f: ********************
# g: ***************
# h: *********
# i: *******
# j: **
#
# Nota: imprimir las barras, de arriba a abajo, en el orden que determina la
#         funciÃ³n "sorted" sobre las claves
# ---------------------------------------------------------------------------

d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}

def histograma_horizontal(d1):
    for x,y in sorted(d1.items()):
        if(y >= 0 and y <= 50):
            print( x , ": ", y * '*')
        else:
            print('Esta fuera del rango')

##    for x,y in sorted(d1.items()):
##        print( x , ": ", y * '*')

# -----------
# EJERCICIO 6
# -----------
# Con la misma entrada que el ejercicio anterior, definir una funcion
# histograma_vertical(d) que imprime el mismo histograma pero con las barras
# en vertical.

# Ejemplo:

# >>> d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_vertical(d2)
#           *
#           *
#           *
#           *
#           *
#         * * *
#         * * *
#         * * *
#       * * * *
#       * * * *
#       * * * *
#     * * * * * *
#     * * * * * *
#   * * * * * * * *
#   * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# a b c d e f g h i j

# Nota: imprimir las barras, de izquierda a derecha, en el orden que determina la
#         funciÃ³n "sorted" sobre las claves
# ---------------------------------------------------------------------------

d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}

#Buscamos el mÃ¡ximo de todos para saber por cual empezar.

def histograma_vertical(d2):
    
    max_num = max(d2.values())
    items = sorted(d2.items())
    
    for x in range (max_num+1):
        print(*(
            '*'
            if max_num - x < v
            else
            ' '
            for k, v in items
        ))
    print(*d2.keys())
