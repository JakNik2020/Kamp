import pygame as pg
from random import randint
from pygame.locals import *;
import math
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
r = 0
scroll = 0
tajmer = 5000
mashine_gun_time = 20
shotgun_time = 1000

def random_gun(br1,br2,r,š):
    while r == 0:
        numero = randint(br1,br2)
        if numero in holding_guns:
            š = š + 1
        else:
            r = 1
            print(š)
    return numero
def every_second_element(values):
    second_values = []

    for index in range(1, len(values), 2):
        second_values.append(values[index])

    return second_values
            
loptica_x = WIDTH // 2
loptica_y = 250

enemies = []
bullets = []
guns = [0,1,2]
holding_guns = [0]
c = 0
pg.font.init()
my_font=pg.font.SysFont("Cosmic Sans MS",30)

enemy_timer = 3000
d = 0
b = 0.1
e = 0
g = 0.1
points = 500
crate_x = 100
crate_y = 600

enemy_x = 500
enemy_y = 500

screen = pg.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
get_gun = False
running = True
player = pg.image.load("a_guy.png").convert_alpha()

#recnik = {'key' : 'value'}
player_x = loptica_x - 15
player_y = loptica_y - 15

#
while running:
    keys = pg.key.get_pressed()
    pos = pg.mouse.get_pos()
    rect = [loptica_x, loptica_y, 10, 15]
    crate = [crate_x, crate_y, 50, 40]
    screen.fill((255,255,255))
    #pg.draw.circle(screen,RED,(loptica_x,loptica_y),RADIUS)
    if enemy_timer <= 0:
        for i in range(10):
            pg.draw.circle(screen,"Green",(enemy_x-randint(-50,50),enemy_y-randint(-50,50)),RADIUS)
        enemy_timer = 3000
    #pg.draw.rect(screen,"Black",rect)
    pg.draw.rect(screen,"Yellow",crate)
    tasteri = pg.key.get_pressed()
    screen.blit(player,(player_x,player_y))
    if abs(loptica_x-crate_x) + abs(loptica_y-crate_y) < 100:
        if d <= 0 and not get_gun:
            txt_buy = my_font.render("Press E to open costs 1000 points",False,(10,10,10))
            screen.blit(txt_buy,(10,10))
        if tajmer == 0 and get_gun:
            txt_get = my_font.render("Press E to get your gun",False,(10,10,10))
            screen.blit(txt_get,(10,10))
        if tasteri[pg.K_e] and d == 0 and not get_gun and points >= 0:
            a = random_gun(0,2,0,0)
            print(a)
            b = 1
            d = 5000
            tajmer = tajmer + 1000
            e = 1
            print(tajmer)
            get_gun = True
        elif tasteri[pg.K_e] and tajmer == 0 and get_gun:
            holding_guns.append(a)
            print(holding_guns)
            b = 0
            d = d + 1000
            get_gun = False
            tajmer = 5000
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif 0 in holding_guns: 
            if event.type == pg.MOUSEBUTTONDOWN and scroll == 0:
                if event.button == 1:
                    y = rect[1]
                    x = rect[0]
                    bullets.append([x, y])    
                #bullets.append([rect[0], rect[1]])
    if 2 in holding_guns:
            if event.type == pg.MOUSEBUTTONDOWN and scroll == 2:
                if event.button == 1:
                    if shotgun_time <= 0:
                        for i in range(5):
                            bullets.append([rect[0]-randint(-20,20), rect[1]-randint(-20,0)])
                        shotgun_time = 1000

    if 1 in holding_guns:
        if pg.mouse.get_pressed()[0] and scroll == 1:
            print(1)
            if mashine_gun_time <= 0:
                print(2)
                bullets.append([rect[0], rect[1]])
                mashine_gun_time = 100
    
    

    if enemy_x < loptica_x:
        enemy_x+=1
    else:
        enemy_x-=1
    if enemy_y < loptica_y:
        enemy_y+=1
    else:
        enemy_y-=1
        
    mx,my = pg.mouse.get_pos()

    points_str = str(points)

    txt_points = my_font.render(points_str,False,(10,10,10))
    screen.blit(txt_points,(10,30))

    #rotate_x = mx - loptica_x
    #rotate_y = my - loptica_y
    #rotate_xy= math.atan2(rotate_y,rotate_x)
    #pg.transform.rotate(screen,rotate_xy)

    

    temp = []
    for bullet in bullets:
        if bullet[1]<800:
            temp.append(bullet)
    #for i in range(len(guns)):
         #if i == 

    b_angle = my - player_y
    a_angle = mx - player_x
    tgalfa = math.tan(a_angle/b_angle)
    alfa = math.atan(tgalfa) * 180 / math.pi

    angle = alfa
    rotimage = pg.transform.rotate(player,angle)
    rect = rotimage.get_rect(center=(650,350))
    screen.blit(rotimage,rect)


    
    bullets = temp
    for bullet in bullets:
        bullet[1] += 5
        pg.draw.circle(screen,"black",bullet,5)
        if tasteri[pg.K_a]:
            bullet[0] += 5
        if tasteri[pg.K_d]:
            bullet[0] -= 5
        if tasteri[pg.K_a]:
            bullet[1] += 5
        if tasteri[pg.K_a]:
            bullet[1] -= 5
        
    try:
        x_diff = abs(enemy_x-bullet[0])
        y_diff = abs(enemy_y-bullet[1])
        c_diff = math.hypot(x_diff, y_diff)

        if c_diff < 5+RADIUS:
            enemy_y = 100000
            enemy_x = 100000
    except:
        print("JA VOLIM DA SMARAM")

    if tasteri[pg.K_a]:
            #loptica_x -= 3
            crate_x += 5
            enemy_x += 5
            bullet[0] += 5
            print("a")
    if tasteri[pg.K_d]:
            #loptica_x += 3
            crate_x -= 5
            enemy_x -= 5
            bullet[0] -= 5
            print("d")
    if tasteri[pg.K_w]:
            #loptica_y -= 3
            crate_y += 5
            enemy_y += 5
            bullet[1] += 5
            print("jump")
    if tasteri[pg.K_s]:
            #loptica_y += 3
            crate_y -= 5
            enemy_y -= 5
            bullet[1] -= 5
            print("down")
    if tasteri[pg.K_1]:
        scroll = 0
    if tasteri[pg.K_2]:
        scroll = 1
    if tasteri[pg.K_3]:
        scroll = 2
    
    if tajmer > 0 and e == 1:
        tajmer = tajmer - 10
    if d > 0:
        d = d - 10
    if mashine_gun_time > 0:
        mashine_gun_time -= 10
    if shotgun_time > 0:
        shotgun_time -= 10
    if enemy_timer > 0:
        enemy_timer -= 10

    pg.event.pump()
    pg.display.update()
    pg.time.delay(10)

pg.quit()