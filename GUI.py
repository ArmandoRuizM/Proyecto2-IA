# pygame.quit()
import pygame, sys
import numpy as np
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Hungry horses 1.0')
screen = pygame.display.set_mode((800, 800),0,32)
 
font = pygame.font.SysFont(None, 100)

apple=pygame.image.load("src/apple.png")
grass=pygame.image.load("src/grass.png")
rose=pygame.image.load("src/rose.png")

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def drawBoard(board, environment, ancho, alto, BLANCO, NEGRO):
    color = 0
    n=0
    for i in range(0, 800, ancho):
        m=0
        for j in range(0, 800, alto):
            print("Valor de n: "+str(n))
            print("Valor de m: "+str(m))
            if color % 2 == 0:
                board[n].append(pygame.Rect(i, j, ancho, alto))
                pygame.draw.rect(screen, NEGRO, [i, j, ancho, alto], 0)
                if(environment[m][n]==1):
                    print("HOLA")
                elif (environment[m][n]==2):
                    print("HOLA")
                elif (environment[m][n]==3):
                    screen.blit(grass, [i+15, j+15])
                elif (environment[m][n]==4):
                    screen.blit(rose, [i+15, j+15])
                elif (environment[m][n]==5):
                    screen.blit(apple, [i+15, j+15])
            else:
                board[n].append(pygame.Rect(i, j, ancho, alto))
                pygame.draw.rect(screen, BLANCO, [i, j, ancho, alto], 0)
                if(environment[m][n]==1):
                    print("HOLA")
                elif (environment[m][n]==2):
                    print("HOLA")
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
    pygame.display.flip()
    return board

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
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                game()
        if button_3.collidepoint((mx, my)):
            if click:
                game()
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
 
def game():
    running = True
    while running:

        screen = pygame.display.set_mode((800, 900),0,32)

        NEGRO = (0, 230, 230)
        BLANCO = (179, 255, 255)
        CAFE = (153, 77, 0)
        reloj = pygame.time.Clock()
        ancho = int(100)
        alto = int(100)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.fill(CAFE)

            env = [[0,0,0,3,0,4,2,3],
                    [0,3,0,4,0,3,0,0],
                    [3,1,0,0,0,0,0,0],
                    [0,3,0,0,5,0,0,4],
                    [3,0,0,0,3,0,3,0],
                    [3,0,0,0,4,0,0,3],
                    [0,4,3,0,0,5,0,0],
                    [0,3,0,0,0,0,3,0]]
    
            board = [[],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    []]
            drawBoard(board, env, ancho, alto, BLANCO, NEGRO)
            reloj.tick(5)


        # screen.fill((0,0,0))
        
        # draw_text('game', font, (255, 255, 255), screen, 20, 20)
        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     if event.type == KEYDOWN:
        #         if event.key == K_ESCAPE:
        #             running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()
