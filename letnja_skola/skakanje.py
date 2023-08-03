import pygame as pg
from random import randint
pg.init()
b = 0
WIDTH = 500
HEIGHT = 500
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
MOVEX = 10
MOVEX2 = 10
MOVEY = 10
RADIUS = 10

loptica_x = WIDTH // 2
loptica_y = 470
max_y = 0
max_x = 0
a = 2
screen = pg.display.set_mode((WIDTH,HEIGHT))
event = pg.MOUSEBUTTONUP
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            MOVEY = MOVEY + 0.3
            print("da")
        if event.type == pg.KEYDOWN:
            MOVEY = MOVEY - 0.3
            print("NE")
        
    screen.fill((255,255,255))
    pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(loptica_x,loptica_y),RADIUS)
    pg.display.update()
    if loptica_y >= (HEIGHT-20):
        MOVEY*=-1
    if loptica_y <= max_y:
        MOVEY*=-1
    
    
    MOVEY = MOVEY + a
    loptica_y += MOVEY
    

    pg.time.delay(50)
