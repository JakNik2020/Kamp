import pygame as pg
from random import randint
pg.init()

WIDTH = 500
HEIGHT = 500
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
RADIUS = 10

MOVEX = 0
MOVEY = 10
RADIUS = 10

loptica_x = WIDTH // 2
loptica_y = 430

g = 0.1



screen = pg.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))


while True:
    
    rect = [loptica_x, loptica_y, 30, 50]
    screen.fill((255,255,255))
    pg.draw.rect(screen,RED,rect)

    if loptica_y > (HEIGHT-50):
        MOVEY *= -0.98
        loptica_y = 450

    if loptica_y < 0 :
        MOVEY = 0
    
    
    MOVEY = MOVEY + g
    loptica_y += MOVEY
    loptica_x += MOVEX

    tasteri = pg.key.get_pressed()

    if tasteri[pg.K_a]:
        loptica_x -= 3
        print("a")

    if tasteri[pg.K_d]:
        loptica_x += 3
        print("d")

    if tasteri[pg.K_SPACE]:
        loptica_y -= 3
        print("jump")
    if tasteri[pg.K_s]:
        loptica_y += 3
        print("down")

    pg.display.update()
    pg.event.pump()
    pg.time.delay(10)