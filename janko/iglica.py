import pygame as pg
from random import randint
import math as m

pg.init()
NASUMICNO = (randint(0, 255), randint(0, 255), randint(0, 255))
blue = (0, 0, 255)
white = (0, 255, 0)
clock = pg.time.Clock()
kidara = pg.image.load("kidara.png")
smrad = pg.image.load("anti_vodista.png")
cigan = pg.image.load("cigan.png")
metak = pg.image.load("bullet.png")

fps = 60


class Bullet:
    def __init__(self, x, y, vel, damage):
        self.x = x
        self.y = y
        self.vel = vel
        self.damage = damage

    def smaraj(self):
        window.blit(metak, (self.x + 8, self.y + 4))


class Player:
    def __init__(self, x, y, hp, max_hp, cooldown):
        self.x = x
        self.y = y
        self.hitbox = (self.x + 10, self.y)
        self.hp = hp
        self.max_hp = max_hp
        self.cooldown = cooldown * fps
        self.cooldown2 = cooldown * fps

    def smaraj(self):
        window.blit(kidara, (self.x + 10, self.y + 10))

    def right(self):
        self.x += 7

    def left(self):
        self.x -= 7

    def up(self):
        self.y -= 7

    def down(self):
        self.y += 7

    def bullet_colided(self, bullet):
        if (
            abs(bullet.x - self.x) <= 100
            and abs(bullet.y - self.y) <= 100
            and self.cooldown <= 0
        ):
            self.hp -= 10
            self.cooldown = self.cooldown2


class Enemy:
    def __init__(self, x, y, vrsta):
        self.x = x
        self.y = y
        self.type = vrsta

    def smaraj(self):
        if self.type == "runner":
            window.blit(smrad, (self.x + 10, self.y + 10))
        elif self.type == "gunner":
            window.blit(cigan, (self.x + 10, self.y + 10))

    def run(self, player):
        if self.type == "runner":
            if (abs(player.x - self.x) <= 200 or abs(player.y - self.y) <= 200) and (
                abs(player.x - self.x) >= 40 or abs(player.y - self.y) >= 40
            ):
                if player.x < self.x:
                    self.x -= 7
                else:
                    self.x += 7
                if player.y <= self.y:
                    self.y -= 7
                else:
                    self.y += 7
        elif self.type == "gunner":
            if (abs(player.x - self.x) <= 600 or abs(player.y - self.y) <= 600) and (
                abs(player.x - self.x) >= 200 or abs(player.y - self.y) >= 200
            ):
                if player.x < self.x:
                    self.x -= 5
                else:
                    self.x += 5
                if player.y <= self.y:
                    self.y -= 5
                else:
                    self.y += 5
        else:
            print("Not defined")

    def gledaj(self, player, slika):  # NE RADI
        mrzonja = m.sqrt(player.x * player.x + player.y + player.y)
        smaranje = m.sin((1 / player.x) / (1 / mrzonja)) + 50
        slika = pg.transform.rotate(slika, smaranje)
        print(smaranje)


iglac = Player(500, 500, 100, 100, 3)
smarac = Enemy(100, 100, "runner")
milan = Enemy(100, 700, "gunner")
stvar = Bullet(100, 300, 2, 10)


width, height = 1080, 800
window = pg.display.set_mode((width, height))

pg.display.set_caption("iglica")

running = True
while running:
    window.fill(white)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    iglac.smaraj()
    smarac.smaraj()
    milan.smaraj()
    smarac.run(iglac)
    milan.run(iglac)
    stvar.smaraj()
    iglac.bullet_colided(stvar)
    # milan.gledaj(iglac, cigan)
    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
        iglac.right()
    if keys[pg.K_a]:
        iglac.left()
    if keys[pg.K_w]:
        iglac.up()
    if keys[pg.K_s]:
        iglac.down()
    iglac.cooldown -= 1
    print(iglac.hp, iglac.cooldown)
    clock.tick(fps)
    pg.display.update()
