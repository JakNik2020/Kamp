import pygame as pg
from random import *


def grid(x1, y1):
    for i in range(50):
        for i in range(100):
            pg.draw.rect(window, blue, ((x1, y1), (x1 + 20, y1 + 20)), 1)
            x1 += 20
        y1 = y1 + 20


pg.init()
blue = (0, 0, 255)
white = (255, 255, 255)
width, height = 800, 600
window = pg.display.set_mode((width, height))
x1 = 0
x2 = 0
y1 = 0
y2 = 800
x = 20
running = True
window.fill(white)
circles = []
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = event.pos
            if len(circles) <= 5:
                circles = []
                pos = 0
            else:
                circles.append(pos)
    Nasu = (randint(0, 255), randint(0, 255), randint(0, 255))
    Nasumicnoo = randint(0, 255)
    jej = (randint(0, 800), randint(0, 600))
    # for pos in circles:
    #    pg.draw.circle(window, Nasu, pos, 10)
    iscrtaj = random.sample(circles, 5)
    """for i in range(1):
        for i in range(100):
            pg.draw.circle(window, blue, (400, 300), x, 1)
            x += 20
        y1 = y1 + 20"""
    # grid(x1, x2, y1, y2)

    pg.display.update()
