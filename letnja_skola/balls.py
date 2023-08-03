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

loptica_x = WIDTH // 2
loptica_y = 0

screen = pg.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))

while True:
    
    pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(randint(0,WIDTH),randint(0,HEIGHT)),RADIUS)
    pg.display.update()

    pg.time.delay(-1000)