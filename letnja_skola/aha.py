import pygame as pg
pg.init()

WIDTH = 500
HEIGHT = 500
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
MOVEX = 10
MOVEY = 0
RADIUS = 100


screen = pg.display.set_mode((WIDTH,HEIGHT))

loptica_x = WIDTH // 2
loptica_y = 0

while True: 
    if loptica_x == WIDTH and loptica_y == 0:
        MOVEX = 0
        MOVEY = 10
    elif loptica_x == WIDTH and loptica_y == HEIGHT:
        MOVEX = -10
        MOVEY = 0
    elif loptica_x ==0 and loptica_y == HEIGHT:
        MOVEX = 0
        MOVEY = -10
    elif loptica_x == 0 and loptica_y == 0:
        MOVEX = 10
        MOVEY = 0

    loptica_x += MOVEX
    loptica_y += MOVEY

    
    screen.fill((0,0,0))
    pg.draw.circle(screen, WHITE, (loptica_x, loptica_y), RADIUS)
    pg.display.update()

    pg.time.delay(50)