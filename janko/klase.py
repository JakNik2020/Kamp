import pygame as pg
from random import randint
import math as m

pg.init()
NASUMICNO = (randint(0, 255), randint(0, 255), randint(0, 255))
blue = (0, 0, 255)
zelengrad = (0, 255, 0)
clock = pg.time.Clock()
kidara = pg.image.load("kidara.png")
smrad = pg.image.load("anti_vodista.png")
zigan = pg.image.load("cigan.png")
metak = pg.image.load("bullet.png")
x_mouse = 0
y_mouse = 0

fps = 60
# dodaj font i napisi da si izgubio oko 130 linije ,promeni sa igraca na metak cooldown za damage i


class Bullet:
    def __init__(self, x, y, vel, damage, cooldown):
        self.x = x
        self.y = y
        self.vel_X = vel[0]
        self.vel_Y = vel[1]
        self.damage = damage
        self.cooldown = cooldown * fps
        self.cooldown2 = cooldown * fps

    def smaraj(self):
        window.blit(metak, (self.x - 8, self.y - 4))

    def bullet_colided(self, player):
        if (
            abs(self.x - player.x) <= 20 and abs(self.y - player.y) <= 20
        ) and self.cooldown <= 0:
            player.hp -= self.damage
            self.cooldown = self.cooldown2

    def bullet_attacked(self, enemy):
        if (
            abs(self.x - enemy.x) <= 20 and abs(self.y - enemy.y) <= 20
        ) and self.cooldown <= 0:
            enemy.hp -= self.damage
            self.cooldown = self.cooldown2

    def pomeraj_se(self, x_mouse, y_mouse):
        self.x += x_mouse / 100
        self.y += y_mouse / 100


class Player:
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hitbox = (self.x + 10, self.y)
        self.hp = hp
        self.max_hp = max_hp
        self.bullets = []

    def smaraj(self):
        window.blit(kidara, (self.x - 20, self.y - 20))

    def right(self):
        self.x += 7

    def left(self):
        self.x -= 7

    def up(self):
        self.y -= 7

    def down(self):
        self.y += 7

    def shoot(self, mouse_pos):
        vx = mouse_pos[0] - self.x
        vy = mouse_pos[1] - self.y
        b = Bullet(self.x, self.y, (vx, vy), 1, 0.1)
        self.bullets.append(b)

    def cltaj(self, x_mouse, y_mouse):
        for bullet in self.bullets:
            bullet.smaraj()
            bullet.pomeraj_se(bullet.vel_X, bullet.vel_Y)


class Enemy:
    def __init__(self, x, y, vrsta, hp, max_hp):
        self.x = x
        self.y = y
        self.type = vrsta
        self.zullets = []

    def smaraj(self):
        if self.type == "runner":
            window.blit(smrad, (self.x + 10, self.y + 10))
        elif self.type == "gunner":
            window.blit(zigan, (self.x + 10, self.y + 10))

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

    def shoot(self, player):
        vx = player.x - self.x
        vy = player.y - self.y
        c = Bullet(self.x, self.y, (vx, vy), 1, 0.1)
        self.zullets.append(c)

    def cltaj(self, x_mouse, y_mouse, player):
        for zullet in self.zullets:
            zullet.smaraj()
            zullet.bullet_colided(player)
            zullet.cooldown -= 1
            zullet.pomeraj_se(player.x, player.y)

    def gledaj(self, player, slika):  # NE RADI
        mrzonja = m.sqrt(player.x * player.x + player.y + player.y)
        smaranje = m.sin((1 / player.x) / (1 / mrzonja)) + 50
        slika = pg.transform.rotate(slika, smaranje)
        print(smaranje)


iglac = Player(500, 500, 100, 100)
smarac = Enemy(100, 100, "runner", 100, 100)
milan = Enemy(100, 700, "gunner", 100, 100)
stvar = Bullet(100, 100, [x_mouse, y_mouse], 10, 1)


width, height = 1080, 800
window = pg.display.set_mode((width, height))

pg.display.set_caption("iglica")
