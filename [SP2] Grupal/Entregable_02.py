# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Segunda práctica
# ===========================================================

# GRUPO: 7
# INTEGRANTE 1:
#   APELLIDOS, NOMBRE: Martínez López, Juan Jesus
#   DNI: 30280475D
# INTEGRANTE 2:
#   APELLIDOS, NOMBRE: Reina Montes, Jose Antonio
#   DNI: 30263968Q
# INTEGRANTE 3:
#   APELLIDOS, NOMBRE: Villar Méndez, Carlos Manuel
#   DNI: 30216661C

# Para esta práctica, se pondrá en uso los conocimientos adquiridos sobre la OOP
# con la creación de un juego de cartas. Este juego de cartas es de dos jugadores
# y es llamado "War" y será un juego de tú contra la máquina. Si no sabes en qué
# consiste el juego "War", aquí te dejo una serie de reglas:
#
# # La baraja se divide en partes iguales, y cada jugador recibe 26 cartas, 
# repartidas una a la vez, boca abajo. Cualquiera puede negociar primero. Cada 
# jugador coloca su pila de cartas boca abajo, enfrente de él.
#
# El juego:
#
# Cada jugador muestra una carta al mismo tiempo y el jugador con la carta más alta
# toma ambas cartas y las coloca, boca abajo, en la parte inferior de su pila.
#
# Si las cartas son del mismo rango, es Guerra. Cada jugador muestra tres cartas boca arriba
# hacia abajo y una carta boca arriba. El jugador con las cartas más altas toma ambas pilas
# (seis cartas). Si las cartas descubiertas vuelven a tener el mismo rango, cada jugador coloca
# otra carta boca abajo y otra carta boca arriba. El jugador con el
# tarjeta superior toma las 10 tarjetas, y así sucesivamente.
#
# Hay algunas variaciones más sobre esto, pero lo mantendremos simple por ahora.
# Ignora las guerras "dobles"
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random

# Estas son dos variables muy útiles para la creación de las cartas.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self,suite=SUITE,ranks=RANKS,deck=[],hdeck1=[],hdeck2=[]):
        self.suite = suite
        self.ranks = ranks
        self.deck = deck
        self.hdeck1= hdeck1
        self.hdeck2= hdeck2

    def create(self):
        for i in range(len(self.suite)):
            for n in range(len(self.ranks)):
                self.deck.append(self.ranks[n]+self.suite[i])
        random.shuffle(self.deck)
        print('\nSe ha barajado el mazo')

    def split_deck(self):
        self.hdeck1=self.deck[0:26]
        self.hdeck2=self.deck[26:52]
        print('El mazo se a dividido en 2')

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,p1=[],p2=[]):
        self.p1 = p1
        self.p2 = p2

    def play(self,p1_deck,p2_deck):
        war=False
        self.p1 = p1_deck.pop()
        self.p2 = p2_deck.pop()
        print('')

    def war(self,war_stack,p1_deck,p2_deck):
        war_stack.append(self.p1)
        war_stack.append(self.p2)
        for i in range(2):
            war_stack.append(p1_deck.pop())
            war_stack.append(p2_deck.pop())
        print('\nAmbos jugadores han cogido 2 cartas')
        return war_stack

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,deck,stack):
        self.deck = deck
        self.stack = stack


######################
#### GAME PLAY #######
######################

# Usa los conocimientos adquiridos junto con algo de lógica para jugar un juego de "War"!

# Recordad de nuevo el "Divide y Vencerás", primero debéis analizar las diferentes
# variales que van a afectaros, los posibles objetos que vayáis a necesitar,
# cuál es la interacción entre esos objetos y el cómo sería el gameplay como orquestador

# Pongo el input para que se mas visual el juego.
input('\n¡Bienvenido a la GUERRA Ricardo!, presiona enter para empezar :) ')

# Defino mi mazo como Deck.
mydeck=Deck()

# Creo el mazo aleatorio.
mydeck.create()

#Divido el mazo en 2 partes
mydeck.split_deck()
print()

# Le asigno a cada jugador una mitad del mazo aleatorio
player_1=Player(mydeck.hdeck1,[])
player_2=Player(mydeck.hdeck2,[])

# El juego esta ON
game_on= True

# Mientras que todavia el juego esta ON, se juega una mano.
# Al final se verifican la cantidad de cartas.
while game_on:
    input('\nPresiona enter para Jugar una mano ')
    print('-------------------------------------------')
    
    # Se inicializa el stack de guerra y se define la mano.
    war_stack=[]
    hand=Hand()
    
    # Se juega una mano
    hand.play(player_1.deck,player_2.deck)
    print('El Jugador 1 ha jugado: ',hand.p1)
    print('El jugador 2 ha jugado: ',hand.p2)

    # Si hay igualdad en el valor de las cartas, hay Guerra.
    if RANKS.index(hand.p1[:-1]) == RANKS.index(hand.p2[:-1]): 
        war = True
        while war :
            print('\nLas cartas tienen el mismo valor!')
            print('GUERRA!')

            if len(player_1.deck) == len(player_2.deck) >= 3:
                hand.war(war_stack,player_1.deck,player_2.deck)
            elif 1 < len(player_1.deck) == len(player_2.deck) < 3 :
                war_stack.append(hand.p1.pop())
                war_stack.append(hand.p2.pop())
                print('\nNo hay suficientes cartas para jugar una guerra normal')
                print('Se descartara solo una carta')
                war_stack.append(p1_deck.pop())
                war_stack.append(p2_deck.pop())
            elif len(player_1.deck) == len(player_2.deck) == 1 :
                print('\nNo hay suficientes cartas para jugar una guerra normal!')
                print('Solo les queda 1 carta a cada uno!')
                print('No se descartan cartas, se juega solo la siguiente')
                war_stack.append(hand.p1)
                war_stack.append(hand.p2)

            input('\nPresiona enter para Jugar ')
            print('-------------------------------------------')
            hand.play(player_1.deck,player_2.deck)
            print('El Jugador 1 ha jugado: ',hand.p1)
            print('El Jugador 2 ha jugado: ',hand.p2)

            if RANKS.index(hand.p1[:-1]) == RANKS.index(hand.p2[:-1]):
                print('Las cartas tienen el mismo valor de nuevo!')
                print('OMG')
                print('GUERRA!')
                input('Presiona enter para Jugar')
                print('-------------------------------------------')
            else:
                war= False

            if len(player_1.deck) == len(player_2.deck) == 0 and  war:
                print('Ya no se puede jugar por falta de cartas!')
                print('Se descarta el stack de ',len(war_stack),' cartas')
                break

    # Si no existe guerra verifico quien gano la mano
    if RANKS.index(hand.p1[:-1]) > RANKS.index(hand.p2[:-1]):
        print('\nGANO JUGADOR 1')
        player_1.stack.extend(war_stack)
        player_1.stack.append(hand.p1)
        player_1.stack.append(hand.p2)
    elif RANKS.index(hand.p1[:-1]) < RANKS.index(hand.p2[:-1]):
        print('\nGANO JUGADOR 2')
        player_2.stack.extend(war_stack)
        player_2.stack.append(hand.p1)
        player_2.stack.append(hand.p2)

    if len(player_1.deck) == len(player_2.deck) == 0:
        game_on=False
        print('\nSE HAN TERMINADO LAS CARTAS!')
        print('EL JUEGO HA TERMINADO')
        print('-------------------------------------------')

#Finalizo el juego
input('Presiona enter para contabilizar las cartas y saber el ganador')
print('\nEl GANADOR ES:')

if len(player_1.stack) > len(player_2.stack):
    print('JUGADOR 1 con ',len(player_1.stack),' cartas')
    print('El jugador 2 tenia ',len(player_2.stack),' cartas :(\n')
elif len(player_1.stack) < len(player_2.stack):
    print('JUGADOR 2 con ',len(player_2.stack),' cartas')
    print('El jugador 1 tenia ',len(player_1.stack),' cartas :(\n')
else:
    print('\n¡AMBOS JUGADORES TIENEN IGUAL CANTIDAD DE CARTAS!')
    print('¡ES UN EMPATE!\n')