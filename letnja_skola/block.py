import pygame as pg
from random import randint
pg.init()

WIDTH = 500
HEIGHT = 500
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
MOVEX = 10
MOVEY = 0
RADIUS = 10
RECTW = 40
RECTH = 20

GROUNDH = 150
SW = 40
SH = 40
augh = 235


screen = pg.display.set_mode((WIDTH,HEIGHT))



block_x = WIDTH // 2
block_y = 0

while True:
    screen.fill((255,255,255))
    rect = [[(WIDTH/2-augh)-RECTW/2, (HEIGHT-80)-GROUNDH],(RECTW,RECTH)]
    augh = augh - 1
    pg.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),rect)
    pg.display.update()

    pg.time.delay(50)