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

bullets = []

g = 0.1



screen = pg.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))

running = True

while running:
    rect = [loptica_x, loptica_y, 30, 50]
    screen.fill((255,255,255))
    pg.draw.rect(screen,RED,rect)

    tasteri = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(10):
                    bullets.append([rect[0], rect[1]])

    if tasteri[pg.K_a]:
        loptica_x -= 3
        print("a")

    if tasteri[pg.K_d]:
        loptica_x += 3
        print("d")

    if tasteri[pg.K_w]:
        loptica_y -= 3
        print("jump")
    if tasteri[pg.K_s]:
        loptica_y += 3
        print("down")
    
    temp = []
    for bullet in bullets:
        if bullet[1]<800:
            temp.append(bullet)
    
    bullets = temp
    for bullet in bullets:
        bullet[1] += 5
        pg.draw.circle(screen,"black",bullet,5)


    pg.event.pump()
    pg.display.update()
    pg.time.delay(10)

pg.quit()