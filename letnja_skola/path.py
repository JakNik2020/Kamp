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
x_num = 235
y_num = 90
def path():
    pg.draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(0,150),(200,150))
    pg.draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(200,150),(200,300))
    pg.draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(200,300),(100,300))
    pg.draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(100,300),(100,400))
    pg.draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(100,400),(350,400))
    pg.draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(350,400),(350,150))
    pg.draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(350,150),(500,150))
def move_circle():
    pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(0,150),RADIUS)
    
    #pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(200,150),(200,300))
    #pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(200,300),(100,300))
    #pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(100,300),(100,400))
    #pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(100,400),(350,400))
    #pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(350,400),(350,150))
    #pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(350,150),(500,150))


screen = pg.display.set_mode((WIDTH,HEIGHT))


screen.fill((255,255,255))
block_x = WIDTH // 2
block_y = 0

while True:
    path()

    pg.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(0,150),RADIUS)
    #if y_num <= 50:
    #    x_num = x_num - 10
    #if x_num <= 250 and y_num <= 100:
    #    x_num = x_num - 10
    #if x_num <= 200 and y_num <= 100:
    #    for i in range(100):
    #        y_num = y_num + 1
    
    pg.display.update()
    pg.time.delay(50)