import random
import numpy as np
#Función que crea el tablero inicial
#def tablero_inicial():
    #board = []
    #for i in range(0, 8):
        #line = []
        #for j in range(0, 8):
            #line.append(0)
        #board.append(line)
    #return board

# Arreglo para almacenar el número total de items, donde items[0] son la cantidad de jugadores, 
# items[1] la cantidad de césped, items[2] la cantidad de flores e items[3] la cantidad de manzanas

items = [2, 14, 5, 2]

tablero_inicial = np.array([  [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0]])

def tablero():
    cesped = flores = manzanas = 0
    jugador1 = jugador2 = True
    
    while jugador1:
        x = random.randint(0,7)
        y = random.randint(0,7)
        if tablero_inicial[x][y] == 0:
            tablero_inicial[x][y] = 1
            jugador1 = False
    while jugador2:
        x = random.randint(0,7)
        y = random.randint(0,7)
        if tablero_inicial[x][y] == 0:
            tablero_inicial[x][y] = 2
            jugador2 = False
    while cesped < items[1]:
        x = random.randint(0,7)
        y = random.randint(0,7)
        if tablero_inicial[x][y] == 0:
            tablero_inicial[x][y] = 3
            cesped += 1
    while flores < items[2]:
        x = random.randint(0,7)
        y = random.randint(0,7)
        if tablero_inicial[x][y] == 0:
            tablero_inicial[x][y] = 4
            flores += 1
    while manzanas < items[3]:
        x = random.randint(0,7)
        y = random.randint(0,7)
        if tablero_inicial[x][y] == 0:
            tablero_inicial[x][y] = 5
            manzanas += 1
    return tablero_inicial    
