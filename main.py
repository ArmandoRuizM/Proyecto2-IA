import numpy as np
#Variable global para almacenar y tratar el ambiente del juego
environment=np.array([[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0]])

#Variables globales para llevar el conteo del puntaje de los jugadores, blanco=cpu y negro=humano
blackHorseScore=0
whiteHorseScore=0