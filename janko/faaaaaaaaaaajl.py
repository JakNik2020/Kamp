import pygame as pg
from random import randint
import math as m

pg.init()
NASUMICNO = (randint(0, 255), randint(0, 255), randint(0, 255))
blue = (0, 0, 255)
zelena = (0, 255, 0)
clock = pg.time.Clock()
igraccc = pg.image.load("player.png")
zunner = pg.image.load("runner.png")
zgunner = pg.image.load("gunner.png")
metak = pg.image.load("bullet.png")
x_mouse = 0
y_mouse = 0
width, height = 1080, 800

fps = 60
font = pg.font.SysFont("comicsansms", 80)


sobe = [
    "pozadine\pozadina.png",
    "pozadine\pozadina2.png",
    "pozadine\pozadina3.png",
    "pozadine\pozadina4.png",
    "pozadine\pozadina5.png",
    "pozadine\pozadina6.png",
    "pozadine\pozadina7.png",
    "pozadine\pozadina8.png",
    "pozadine\pozadina9.png",
    "pozadine\pozadina10.png",
    "pozadine\pozadina11.png",
    "pozadine\pozadina12.png",
    "pozadine\pozadina13.png",
    "pozadine\pozadina14.png",
    "pozadine\pozadina15.png",
    "pozadine\pozadina16.png",
    "pozadine\pozadina17.png",
    "pozadine\pozadina18.png",
    "pozadine\pozadina19.png",
]
# dodaj font i napisi da si izgubio oko 130 linije


class soba:
    def __init__(self, ulaz, izlaz, broj):
        self.ulaz = ulaz
        self.izlaz = izlaz
        self.broj = broj
        self.x_kordinata_vrata = 0
        self.y_kordinata_vrata = 0
        self.x_kordinata_vrata2 = 0
        self.y_kordinata_vrata2 = 0

    def izaberi(self):
        self.vrsta = randint(0, 18)
        self.loading = pg.image.load(sobe[self.vrsta])

    def ulaz_izlaz(self):
        if self.ulaz == 0:
            self.x_kordinata_vrata = height // 2
            self.y_kordinata_vrata = -20

        elif self.ulaz == 1:
            self.x_kordinata_vrata = height // 2
            self.y_kordinata_vrata = height - 54

        elif self.ulaz == 2:
            self.x_kordinata_vrata = 0
            self.y_kordinata_vrata = height // 2

        elif self.ulaz == 3:
            self.x_kordinata_vrata = height
            self.y_kordinata_vrata = width // 2

        if self.izlaz == 0:
            self.x_kordinata_vrata2 = height // 2
            self.y_kordinata_vrata2 = -20

        elif self.izlaz == 1:
            self.x_kordinata_vrata2 = height // 2
            self.y_kordinata_vrata2 = height - 54

        elif self.izlaz == 2:
            self.x_kordinata_vrata2 = 54
            self.y_kordinata_vrata2 = width // 2

        elif self.izlaz == 3:
            self.x_kordinata_vrata2 = height
            self.y_kordinata_vrata2 = width // 2

    def postoji(self):
        window.blit(self.loading, (0, 0))
        self.ulazslik = pg.image.load("pozadine\prolaz(gore-dole).png")
        self.ulazzslik = pg.image.load("pozadine\prolaz(desno-levo).png")

        if self.ulaz == 0 or self.ulaz == 1:
            window.blit(self.ulazslik, (self.x_kordinata_vrata, self.y_kordinata_vrata))

        elif self.ulaz == 2 or self.ulaz == 3:
            window.blit(
                self.ulazzslik, (self.x_kordinata_vrata, self.y_kordinata_vrata)
            )

        if self.izlaz == 0 or self.izlaz == 1:
            window.blit(
                self.ulazslik, (self.x_kordinata_vrata2, self.y_kordinata_vrata2)
            )

        elif self.izlaz == 2 or self.izlaz == 3:
            window.blit(
                self.ulazzslik, (self.x_kordinata_vrata2, self.y_kordinata_vrata2)
            )

    def generate(self):
        self


class Bullet:
    def __init__(self, x, y, vel, damage, cooldown):
        self.x = x
        self.y = y
        self.vel_X = vel[0]
        self.vel_Y = vel[1]
        self.damage = damage
        self.cooldown = cooldown * fps
        self.cooldown2 = cooldown * fps

    def postoji(self):
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
        self.x += self.vel_X / 100

        self.y += self.vel_Y / 100


class Player:
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hitbox = (self.x + 10, self.y)
        self.hp = hp
        self.max_hp = max_hp
        self.bullets = []

    def postoji(self):
        window.blit(igraccc, (self.x - 20, self.y - 20))

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
            bullet.postoji()
            bullet.pomeraj_se(bullet.vel_X, bullet.vel_Y)


class Enemy:
    def __init__(self, x, y, vrsta, hp, max_hp):
        self.x = x
        self.y = y
        self.type = vrsta
        self.zullets = []

    def postoji(self):
        if self.type == "runner":
            window.blit(zunner, (self.x + 10, self.y + 10))
        elif self.type == "gunner":
            window.blit(zgunner, (self.x + 10, self.y + 10))

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
            zullet.postoji()
            zullet.bullet_colided(player)
            zullet.cooldown -= 1
            zullet.pomeraj_se(player.x, player.y)

    def gledaj(self, player, slika):  # NE RADI
        mrzonja = m.sqrt(player.x * player.x + player.y + player.y)
        smaranje = m.sin((1 / player.x) / (1 / mrzonja)) + 50
        slika = pg.transform.rotate(slika, smaranje)
        print(smaranje)


iglac = Player(500, 500, 100, 100)
vojislav = Enemy(100, 100, "runner", 100, 100)
milan = Enemy(100, 700, "gunner", 100, 100)
stvar = Bullet(100, 100, [x_mouse, y_mouse], 10, 1)
sobica = soba(2, 3, 1)

window = pg.display.set_mode((width, height))

pg.display.set_caption("iglica")
sobica.izaberi()


running = True
while running:
    window.fill(zelena)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pg.mouse.get_pos()
            iglac.shoot((x_mouse, y_mouse))

    text_surface = font.render("YOU LOST", True, (0, 0, 0))
    hp = font.render(f"HP{iglac.hp}/{iglac.max_hp}", True, (0, 0, 0))

    if iglac.hp > 0:
        sobica.ulaz_izlaz()
        sobica.postoji()
        iglac.postoji()
        iglac.cltaj(x_mouse, y_mouse)
        stvar.bullet_colided(iglac)
        stvar.pomeraj_se(iglac.x, iglac.y)
        stvar.postoji()
        milan.postoji()
        milan.run(iglac)
        milan.shoot(iglac)
        milan.cltaj(x_mouse, y_mouse, iglac)
        vojislav.run(iglac)
        vojislav.postoji()
        window.blit(hp, (625, 50))
    else:
        window.blit(text_surface, (300, 375))

    # if iglac.x >= height:

    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
        iglac.right()
    if keys[pg.K_a]:
        iglac.left()
    if keys[pg.K_w]:
        iglac.up()
    if keys[pg.K_s]:
        iglac.down()
    stvar.cooldown -= 1
    print(iglac.hp, stvar.cooldown)

    clock.tick(fps)
    pg.display.update()
