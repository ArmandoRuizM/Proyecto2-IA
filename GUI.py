from re import U
import pygame, sys
import numpy as np
from board import board
from pygame.locals import *
from main import possibleMoves, findPlayer, initStatus, movePlayer, createTree, utility
from node import Node
import time
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Hungry horses 1.0')
screen = pygame.display.set_mode((800, 800),0,32)
font = pygame.font.SysFont(None, 100)
apple=pygame.image.load("src/apple.png")
grass=pygame.image.load("src/grass.png")
rose=pygame.image.load("src/rose.png")
player=pygame.image.load("src/player.png")
cpu=pygame.image.load("src/cpu.png")

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def getPossibleMove(posMoves,env):
    playerPos=findPlayer(1,env)
    moves=[]
    if posMoves[0]:
        moves.append([0,[playerPos[0]-1,playerPos[1]-2]])
    if posMoves[1]:
        moves.append([1, [playerPos[0]-2,playerPos[1]-1]])
    if posMoves[2]:
        moves.append([2, [playerPos[0]-1,playerPos[1]+2]])
    if posMoves[3]:
        moves.append([3, [playerPos[0]-2,playerPos[1]+1]])
    if posMoves[4]:
        moves.append([4, [playerPos[0]+1,playerPos[1]+2]])
    if posMoves[5]:
        moves.append([5, [playerPos[0]+2,playerPos[1]+1]])
    if posMoves[6]:
        moves.append([6, [playerPos[0]+1,playerPos[1]-2]])
    if posMoves[7]:
        moves.append([7, [playerPos[0]+2,playerPos[1]-1]])
    return moves


def drawObjects(environment, ancho, alto):
    n=0
    color=0
    for i in range(0, 800, ancho):
        m=0
        for j in range(0, 800, alto):
            if color % 2 == 0:
                if(environment[m][n]==1):
                    screen.blit(player, [i+15, j+15])
                elif (environment[m][n]==2):
                    screen.blit(cpu, [i+15, j+15])
                elif (environment[m][n]==3):
                    screen.blit(grass, [i+15, j+15])
                elif (environment[m][n]==4):
                    screen.blit(rose, [i+15, j+15])
                elif (environment[m][n]==5):
                    screen.blit(apple, [i+15, j+15])
            else:
                if(environment[m][n]==1):
                    screen.blit(player, [i+15, j+15])
                elif (environment[m][n]==2):
                    screen.blit(cpu, [i+15, j+15])
                elif (environment[m][n]==3):
                    screen.blit(grass, [i+15, j+15])
                elif (environment[m][n]==4):
                    screen.blit(rose, [i+15, j+15])
                elif (environment[m][n]==5):
                    screen.blit(apple, [i+15, j+15])
            color += 1
            m=m+1
        color += 1
        n=n+1

def drawPossibleMoves(moves, environment):
    listeners=[]
    for i in range(len(moves)):
        listeners.append([moves[i][0], pygame.Rect(moves[i][1][1]*100, moves[i][1][0]*100, 100, 100)])
        pygame.draw.rect(screen, (255, 255, 102), [moves[i][1][1]*100, moves[i][1][0]*100, 100, 100], 0)
    return listeners

def drawBoard(board, environment, ancho, alto, BLANCO, NEGRO, CAFE, pp1, pcpu):
    color = 0
    n=0
    screen.fill(CAFE)
    p1PossibleMoves=possibleMoves(1,environment)
    moves = getPossibleMove(p1PossibleMoves, environment)
    for i in range(0, 800, ancho):
        m=0
        for j in range(0, 800, alto):
            if color % 2 == 0:
                #board[n].append(pygame.Rect(i, j, ancho, alto))
                pygame.draw.rect(screen, NEGRO, [i, j, ancho, alto], 0)
            else:
                #board[n].append(pygame.Rect(i, j, ancho, alto))
                pygame.draw.rect(screen, BLANCO, [i, j, ancho, alto], 0)
            color += 1
            m=m+1
        color += 1
        n=n+1
    listeners=drawPossibleMoves(moves,environment)
    drawObjects(environment, ancho, alto)
    font = pygame.font.SysFont(None, 40)
    draw_text('Puntos CPU:', font, (255, 255, 255), screen, 80, 840)
    draw_text(str(pcpu), font, (255, 255, 255), screen, 265, 840)
    draw_text('Sus puntos:', font, (255, 255, 255), screen, 530, 840)
    draw_text(str(pp1), font, (255, 255, 255), screen, 710, 840)
    pygame.display.flip()
    return listeners

def isThereAWinner(status):
    objects=0
    for i in range(len(status[0])):
        for j in range(len(status[0][i])):
            if(status[0][i][j]==3):
                objects+=1
            elif(status[0][i][j]==4):
                objects+=1
            elif(status[0][i][j]==5):
                objects+=1
    if objects==0:
        return True
    else:
        return False
    
def whoWins(status):
    winner="CR7"
    if status[1]>status[2]:
        winner="Usted"
    elif status[2]>status[1]:
        winner="CPU"
    else:
        winner="Nadie, fue un empate"
    return winner
    
def game_over(status):
    while True:
        screen.fill((255,255,255))
        draw_text('Game Over', pygame.font.SysFont(None, 110), (0, 0, 0), screen, 200, 150)
        mx, my = pygame.mouse.get_pos()
        draw_text("Terminó la partida, el ganador es: "+ whoWins(status), pygame.font.SysFont(None, 50), (0, 0, 0), screen, 50, 480)
        button_3 = pygame.Rect(350, 610, 100, 60)
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        font = pygame.font.SysFont(None, 40)
        pygame.draw.rect(screen, (255, 255, 255), button_3)
        draw_text('Salir', font, (255, 0, 0), screen, 350, 630)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

def main_menu():
    while True:
        screen.fill((255,255,255))
        draw_text('Hungry horses 1.0', pygame.font.SysFont(None, 110), (0, 0, 0), screen, 90, 150)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(260, 330, 260, 80)
        button_2 = pygame.Rect(280, 480, 200, 80)
        button_3 = pygame.Rect(270, 630, 220, 80)
        if button_1.collidepoint((mx, my)):
            if click:
                game(2)
        if button_2.collidepoint((mx, my)):
            if click:
                game(4)
        if button_3.collidepoint((mx, my)):
            if click:
                game(6)
        font = pygame.font.SysFont(None, 60)
        pygame.draw.rect(screen, (255, 255, 255), button_1)
        draw_text('Principiante', font, (0, 0, 0), screen, 265, 350)
        pygame.draw.rect(screen, (255, 255, 255), button_2)
        draw_text('Amateur', font, (0, 0, 0), screen, 285, 500)
        pygame.draw.rect(screen, (255, 255, 255), button_3)
        draw_text('Avanzado', font, (0, 0, 0), screen, 275, 650)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
 
def game(difficulty):
    diff=difficulty
    running = True
    screen = pygame.display.set_mode((800, 900),0,32)
    NEGRO = (0, 230, 230)
    BLANCO = (179, 255, 255)
    CAFE = (153, 77, 0)
    ancho = int(100)
    alto = int(100)
    tree=createTree(diff, Node(initStatus(), None, 2, 0, "xd", -1))
    gameBoard= [[],
                [],
                [],
                [],
                [],
                [],
                [],
                []]
    status=tree.elements[0].getStatus()
    currentPlayer="CPU"
    while running:
        listeners=drawBoard(gameBoard, status[0], ancho, alto, BLANCO, NEGRO, CAFE, status[1], status[2])
        if currentPlayer=="CPU": ##Juega la CPU
            tree=utility(tree)
            nextMove = tree.elements[0].getOperator()
            status=movePlayer(2, nextMove, status)
            currentPlayer="P1"
        else: ##Juega player1
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    # get a list of all sprites that are under the mouse cursor
                    clicked_listeners = [s for s in listeners if s[1].collidepoint(pos)]
                    # do something with the clicked sprites...
                    for i in range(len(clicked_listeners)):
                        status=movePlayer(1 , clicked_listeners[i][0], status)
                        listeners=drawBoard(gameBoard, status[0], ancho, alto, BLANCO, NEGRO, CAFE, status[1], status[2])
                        tree=createTree(diff, Node(status, None, 2, 0, "xd", -1))
                        currentPlayer="CPU"
        if(isThereAWinner(status)):
            running=False
            game_over(status)
        pygame.display.update()
        mainClock.tick(60)
main_menu()