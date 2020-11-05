# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Primera entrega
# ===========================================================

# GRUPO: 7
# INTEGRANTE 1:
#   APELLIDOS, NOMBRE: MartÃ­nez LÃ³pez, Juan Jesus
#   DNI: 30280475D
# INTEGRANTE 2:
#   APELLIDOS, NOMBRE: Reina Montes, Jose Antonio
#   DNI: 30263968Q
# INTEGRANTE 3:
#   APELLIDOS, NOMBRE: Villar MÃ©ndez, Carlos Manuel
#   DNI: 30216661C

# Escribir el cÃ³digo Python de las funciones que se piden en el
# espacio que se indica en cada ejercicio.

# IMPORTANTE: NO CAMBIAR EL NOMBRE NI A ESTE ARCHIVO NI A LAS FUNCIONES QUE SE
# PIDEN (aquellas funciones con un nombre distinto al que se pide en el
# ejercicio NO se corregirÃ¡n).

# ESTE ENTREGABLE SUPONEN 3 PUNTOS DE LA NOTA DEL TRIMESTRE PARA TODO EL GRUPO

# *****************************************************************************
# HONESTIDAD ACADÃ‰MICA Y COPIAS: la realizaciÃ³n de estos ejercicios es un
# trabajo grupal, por lo que deben completarse por cada grupo de estudiantes.
# La discusiÃ³n y el intercambio de informaciÃ³n de carÃ¡cter general con los
# compaÃ±eros se permite (e incluso se recomienda), pero NO AL NIVEL DE CÃ“DIGO.
# Igualmente el remitir cÃ³digo de terceros, obtenido a travÃ©s de la red o
# cualquier otro medio, se considerarÃ¡ plagio.

# Cualquier plagio o comparticiÃ³n de cÃ³digo que se detecte significarÃ¡
# automÃ¡ticamente la calificaciÃ³n de CERO EN LA ASIGNATURA para TODOS los
# alumnos involucrados. Â¡Aseguraros!
# *****************************************************************************

# -----------------------------------------------------------------------------
# EJERCICIO 1)

# Supongamos que tenemos una cadena de caracteres con una frase, en la que
# pueden aparecer dÃ­gitos (entre 0 y 9), que hacen el papel de "comodines" que
# han de ser sustituidos por palabras concretas. Por ejemplo, si tenemos la
# siguiente frase:

# "1 me dijo que 0 vendrÃ­a con 2"

# podemos pensar que 0, 1 y 2 hacen el papel de sÃ­mbolos que pueden ser
# sustituidos por palabras concretas. Por ejemplo, sustituyendo 0 por Miguel,
# 1 por Juan y 2 por Pedro, tendrÃ­amos la frase:

# "Juan me dijo que Miguel vendrÃ­a con Pedro"

# Para expresar las sustituciones a realizar, lo haremos mediante una
# secuencia p0:p1:p2:... de palabras separadas por el carÃ¡cter ":", en la que
# la palabra de la posiciÃ³n i-Ã©sima es la que hay que usar para sustituir al dÃ­gito i
#
# Por ejemplo, la sustituciÃ³n del ejemplo anterior la expresarÃ­amos por
# Miguel:Juan:Pedro
# (es decir, 0 por Miguel, 1 por Juan y 2 por Pedro).

# Supongamos que tenemos listadas en un fichero de texto una serie de
# sustituciones en el formato descrito, una por cada lÃ­nea del fichero.

# Se pide definir una funciÃ³n sustituye_patrones(frase,fichero) que
# recibiendo como entrada una frase y un fichero en el que estÃ¡n listadas una
# serie de sustituciones (una por lÃ­nea), escribe por pantalla las frases que
# se obtienen al aplicar cada sustituciÃ³n del fichero a la frase.

# Por ejemplo, si tenemos un fichero sustituciones.txt con las siguientes
# lÃ­neas:

# Miguel:Juan:Pedro
# Luis:Antonio:Maria
# Marcos:Eva
# Ivan:Jesus:Antonio:Luis
# Rafael:Francisco:Jose

# entonces, el comportamiento de la funciÃ³n debe ser el siguiente:

# >>> sustituye_patrones("1 me dijo que 0 vendrÃ­a con 2","sustituciones.txt")
# Juan me dijo que Miguel vendrÃ­a con Pedro
# Antonio me dijo que Luis vendrÃ­a con Maria
# Eva me dijo que Marcos vendrÃ­a con 2
# Jesus me dijo que Ivan vendrÃ­a con Antonio
# Francisco me dijo que Rafael vendrÃ­a con Jose

# >>> sustituye_patrones("Los hijos de 1 son 2 y 0","sustituciones.txt")
# Los hijos de Juan son Pedro y Miguel
# Los hijos de Antonio son Maria y Luis
# Los hijos de Eva son 2 y Marcos
# Los hijos de Jesus son Antonio y Ivan
# Los hijos de Francisco son Jose y Rafael

def sustituye_patrones(frase, fichero):
    document = open (fichero, 'a')  #abre el archivo
    tests = [line.rstrip('\n').split(':') for line in document] #el rstrip devuelve una nueva cadena con los espacios en blanco eliminados
        
        for test in tests:  #edita el texto
            text = frase
            for idx in range (len(test)):   #introduzca un índice
                text = text.replace(str(idx), test[idx]) #como queremos q aparezca que reemplace el texto como arrays con separtaciones, comas...

            print(text)      #imprime
    
        
sustituye_patrones("1 me dijo que 0 vendría con 2","sustituciones.txt") 

# NÃ³tese que:
# - Supondremos que en la frase de entrada las palabras se separan mediante un
#   Ãºnico espacio, y que los Ãºnicos nÃºmeros que aparecen son dÃ­gitos de 0 a 9.
# - No todas las sustituciones indican sustituciÃ³n para todos los dÃ­gitos que
#   aparezcan en la frase. Por ejemplo, la tercera lÃ­nea del ejemplo, no
#   indica sustituciÃ³n para 2, y en ese caso se deja sin sustituir.
# - Asimismo, puede que la sustituciÃ³n indique sustituciÃ³n para mÃ¡s dÃ­gitos de
#   los que aparece en la frase.

# INDICACIÃ“N: pueden ser Ãºtiles los mÃ©todos split y join de la clase string.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# EJERCICIO 2)

# Supongamos que la ETSII ha comprado un nuevo ordenador que vamos a utilizar
# como servidor para las prÃ¡cticas de la asignatura, y que necesitamos dar de
# alta a los alumnos como usuarios de ese servidor. Para ello, hemos de
# generar automÃ¡ticamente un nombre de usuario para cada alumno, en base a su
# nombre y apellidos.

# En este ejercicio se pide una funciÃ³n imprime_usuarios(fichero), que
# recibiendo como entrada un fichero con los datos de cada usuario, imprime
# por pantalla un listado de los mismos en orden alfabÃ©tico de apellidos,
# junto con el nombre de usuario automÃ¡ticamente generado.

# Por ejemplo, aplicando la funciÃ³n imprime_usuarios al fichero nombres.txt
# que se proporciona, debe de mostrase el siguiente resultado:

# >>> imprime_usuarios("nombres.txt")
#
# DNI      Apellidos                      Nombre          Usuario
# -------- ------------------------------ --------------- --------
# 67834547 Abad Garcia                    Maria Jose      mjabagar
# 87452221 Fernandez Lopera               Maria           mferlop1
# 76865412 Fernandez Lopez                Mario           mferlop
# 36638712 Gomariz Gonzaga                Amador          agomgon1
# 12987534 Gomez Gonzalez                 Alicia          agomgon
# 21783647 Gonzalez Echevarri             Antonia Maria   amgonech
# 87654321 Luna Espejo                    Emilio          elunesp
# 78988851 Mencheta Ruiz                  Javier Liborio  jlmenrui2
# 88734412 Mencheta Ruiz                  Jose Luis       jlmenrui1
# 22426553 Menendez Ruiz                  Juan            jmenrui
# 23823472 Mensaque Ruibarros             Juan Luis       jlmenrui
# 63555789 Muela Garcia                   Lidia           lmuegar
# 73535787 Navas Suarez                   Rocio           rnavsua
# 73163633 Perez Posada                   Manuel Jose     mjperpos
# 73263638 Poza Ramirez                   Isabel          ipozram
# 73276362 Rodicio Martinez               Antonio Manuel  amrodmar1
# 12326523 Rodriguez Marquez              Antonio Manuel  amrodmar
# 34551211 Sanchez Sanchez                Fermin Jose     fjsansan
# 78363677 Sanchez Santaella              Enrique Manuel  emsansan
# 21334456 Torres Chacon                  Eduardo         etorcha


# El fichero de entrada es una secuencia de lÃ­neas de la forma:
# DNI:Nombre1:Nombre2:Apellido1:Apellido2
# o bien (si el alumno no tuviera nombre compuesto):
# DNI:Nombre::Apellido1:Apellido2

# Como se muestra en el ejemplo anterior, el nombre de usuario de cada alumno
# se ha de generar mediante la siguiente regla: inicial del primer nombre,
# inicial segundo nombre (si tuviera), las tres primeras letras del primer
# apellido y las tres primeras letras del segundo apellido, todo en
# minÃºsculas. Si con esta regla hay varios alumnos a los que les corresponde
# el mismo nombre de usuario, se distinguen mediante sucesivos Ã­ndices
# numÃ©ricos que se aÃ±aden al final.

# NÃ³tese que si una lÃ­nea del fichero no tiene el formato indicado, se ha de
# ignorar.

# INDICACIONES:
# - Pueden ser Ãºtiles los mÃ©todos split y lower de la clase string
# - Al leer cada lÃ­nea del fichero de entrada, el Ãºltimo carÃ¡cter serÃ¡ el
#   salto de lÃ­nea "\n". Si tenemos una cadena l que tiene ese carÃ¡cter de fin
#   de lÃ­nea, entonces l[:-1] es la misma lÃ­nea pero sin ese carÃ¡cter.
# - Para ordenar las lÃ­neas por orden alfabÃ©tico, puede ser util el mÃ©todo de
#   sort de la clase listas, y usar el parametro "key=...".
# - Las lÃ­neas de salida del ejemplo han sido impresas con la siguiente cadena
#   de formateo:  "{0:>8} {1:<30} {2:<15} {3}"
# ----------------------------------------------------------------------------------

ficheros = "nombres.txt"
import re


def is_user_line(list):
    if len(list) == 5 and len(list[0]) == 8:
        return True

    else:
        return False


def set_name(nombre1, nombre2):
    if len(nombre2) > 0:
        return nombre1 + ' ' + nombre2

    else:
        return nombre1


def set_usernames(users):
    usernames = []

    for user in users:

        nombres = user['nombre'].split(' ')

        apellidos = user['apellidos'].split(' ')

        if len(nombres) == 2:
            username = nombres[0][0] + nombres[1][0] + apellidos[0][0:3] + apellidos[1][0:3]

        else:
            username = nombres[0][0] + apellidos[0][0:3] + apellidos[1][0:3]

        while username.lower() in usernames:
            numbers = re.findall(r'[0-9]+', username)

            if len(numbers) > 0:
                new_number_name = int(numbers[len(numbers) - 1]) + 1

                username = username.replace(numbers[len(numbers) - 1], str(new_number_name))

            else:
                username = username + str(1)

        usernames.append(username.lower())

        user['usuario'] = username.lower()


def imprime_usuarios(file):
    users = []
    f = open(file, 'r')

    for line in f:
        items = line.split(':')

        if is_user_line(items):
            new_user = {
                'dni': items[0],
                'apellidos': items[3] + ' ' + items[4].replace('\n', ''),
                'nombre': set_name(items[1], items[2]),
                'usuario': ''
            }

            users.append(new_user)

    set_usernames(users)

    print('DNI      Apellidos                      Nombre          Usuario')
    print('-------- ------------------------------ --------------- --------')

    for user in users:
        print(f"{user['dni']:>8} {user['apellidos']:<30} {user['nombre']:<15} {user['usuario']}")

    f.close()


imprime_usuarios(ficheros)
#############
              ###mensaje = "hola.txt"
#with open (mensaje,"r") as f:
 #   mensaje = f.read()
  #  espacio = [i for i in mensaje.split(":")]
   # espacio = "  ".join(espacio)
    #espacio = espacio.split("\n")
    #for x in espacio:
     #       print(x)
              #
              #
              ##

# -----------------------------------------------------------------------------
# EJERCICIO 3) EL DECODIFICADOR

# Se tiene que realizar un juego con las siguientes instrucciones:

# 1. El programa decidirÃ¡ 3 dÃ­gitos no repetidos. Ej: 123
# 2. El jugador deberÃ¡ indicar 3 dÃ­gitos mediante la consola.
# 3. El programa nos devolverÃ¡ una pista de las siguientes:
#
#     Â¡Casi!: El jugador acertÃ³ los tres nÃºmeros, pero en el orden incorrecto.
#     Cerca: El jugador acertÃ³ un nÃºmero en la posiciÃ³n correcta.
#     Nada: El jugador no acertÃ³ el resto de casos.
#
# 4. BasÃ¡ndonos en estas pruebas, el jugador tendrÃ¡ que conseguir hacer que
#    coincidan los 3 dÃ­gitos en la misma posiciÃ³n, el programa responderÃ¡ y
#    terminarÃ¡ con:
#                    Â¡Enhorabuena, ahora eres un hacker!

# Por ejemplo, si intentamos jugar con la mÃ¡quina y esta tiene almacenado el
# nÃºmero 479, esto serÃ­a un ejemplo de una partida:

# >>> juego_decodificador()
# Â¡Bienvenido al decodificador!
# Â¿CuÃ¡l es tÃº apuesta?: 459
# Cerca, Â¡sigue asÃ­!
# Â¿CuÃ¡l es tÃº apuesta? 345
# Nada, intÃ©ntalo de nuevo.
# Â¿CuÃ¡l es tÃº apuesta? 947
# Â¡Casi!, reordÃ©nalos.
# Â¿CuÃ¡l es tÃº apuesta? 479
# Â¡Enhorabuena, ahora eres un hacker!
# >>>

# Es importante que el programa termine en esa sentencia.

# Notas:
# Hay que tener en cuenta la divisiÃ³n de las tareas para completar este tiempo
# de tareas que podrÃ­an tener una complejidad elevada. Â¡Divide y vencerÃ¡s!
#
# Hay algunas instrucciones que pueden ser de utilidad para desarrollar este
# sencillo juego:

import random


digitos = ('0','1','2','3','4','5','6','7','8','9') #para que el codigo que toque solo tenga de rango del 0 al 9. Tambien se puede hacer con un list(range(10))


codigo = '' #con esto hacemos que toque un codigo

for i in range(3): #para que tenga un rango de solo 3 digitos.
    candidato = random.choice(digitos)
                                            
    while candidato in codigo:  # para que no toque digitos no repetidos
        candidato = random.choice(digitos)
    codigo = codigo + candidato


print('\n------------------------------¡Bienvenido al decodificador!------------------------------\n')
              
propuesta = input("¿Cual es tú apuesta?: ") #este input es para que nosotros pongamos el codigo


intentos = 1
while propuesta != codigo: #para ayudar un poco con los aciertos y coincidencias
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0


    for i in range(3):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1

    if coincidencias == 3:
        print(" ¡Casi!, acertaste los 3 numeros, pero tienes que ordenarlos.")
    elif coincidencias == 2:
        print(" ¡Cerca!, tienes ", coincidencias ,"coincidencias y", aciertos ,"en la posicion correcta, dentro de poco seras hacker")
    elif coincidencias == 1:
        print(" ¡Cerca!, tienes ", coincidencias ,"coincidencias y", aciertos ,"en la posicion correcta, dentro de poco seras hacker")
    elif coincidencias == 0:
        print(" ¡Nada!, tienes ", coincidencias ,"coincidencias y", aciertos ,"en la posicion correcta hazlo de nuevo")
    propuesta = input("\n¿Cual es tú apuesta?: ")

print ("¡Enhorabuena, ahora eres un hacker! ")
