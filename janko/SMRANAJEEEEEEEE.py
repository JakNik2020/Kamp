import pygame as pg
from random import *

white = (255, 255, 255)

pg.init()

width, height = 1080, 800
window = pg.display.set_mode((width, height))
runing = True
while runing:
    window.fill(white)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOW:
            pos = event.pos
