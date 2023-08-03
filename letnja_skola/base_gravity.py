import pygame as pg

screen = pg.display.set_mode((500,500))
RADIUS = 20

x = 500/2
y = 500 - RADIUS
speed = -10

while True:
    screen.fill("white")
    pg.draw.circle(screen,"red",(x,y),RADIUS)

    y += speed
    speed += 0.05

    pg.display.update()
    pg.time.delay(50)