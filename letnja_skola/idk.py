import pygame as pg

WIDTH = 500
LENGHT = 500
WHITE = (255,255,255)
RED = (255,0,0)

BLUE = (0,0,255)

RECTW = 150
RECTH = 250

SW = 40
SH = 40

GROUNDH = 150



RECTWM= WIDTH/2


rect = [[WIDTH/2-RECTW/2, LENGHT-GROUNDH],(RECTW,RECTH)]

pg.init()
pg.display.set_caption("Petlja letnja škola")


screen = pg.display.set_mode((WIDTH,LENGHT))

while True:
    screen.fill(WHITE)
    rect[0][0]-=SW



    sombrero = [(rect[0][0]-SW,         rect[0][1]),
            (rect[0][0]-SW,         rect[0][1]-SH),
            (rect[0][0],            rect[0][1]-SH),
            (rect[0][0],            rect[0][1]-2*SH),
            (rect[0][0]+RECTW,      rect[0][1]-2*SH),
            (rect[0][0]+RECTW,      rect[0][1]-SH),
            (rect[0][0]+RECTW+SW,   rect[0][1]-SH),
            (rect[0][0]+RECTW+SW,   rect[0][1]),]




    ground = ((0, LENGHT-GROUNDH), (WIDTH,GROUNDH))
    pg.draw.rect(screen,RED,rect)
    pg.draw.rect(screen,BLUE,ground)
    pg.draw.circle(screen, "yellow",((100,100)),80)
    pg.draw.polygon(screen, "Brown" , sombrero)
    pg.display.update()
    pg.time.delay(10000)