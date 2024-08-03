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

SOBA_MIN_X = 60
SOBA_MIN_Y = 50
SOBA_MAX_X = width - 60
SOBA_MAX_Y = height - 69
X_0_KORDINATA_VRATA = width // 2 - 100
Y_0_KORDINATA_VRATA = 0
X_1_KORDINATA_VRATA = width // 2 - 100
Y_1_KORDINATA_VRATA = height - 54
X_2_KORDINATA_VRATA = 0
Y_2_KORDINATA_VRATA = height // 2 - 100
X_3_KORDINATA_VRATA = width - 40
Y_3_KORDINATA_VRATA = height // 2 - 100

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
        self.x_kordinata_sobe = 0
        self.y_kordinata_sobe = 0

    def izaberi(self):
        self.vrsta = randint(0, 18)
        self.loading = pg.image.load(sobe[self.vrsta])

    def ulaz_izlaz(self):
        if self.ulaz == 0:
            self.x_kordinata_vrata = X_0_KORDINATA_VRATA  # 440
            self.y_kordinata_vrata = Y_0_KORDINATA_VRATA  # 0

        elif self.ulaz == 1:
            self.x_kordinata_vrata = X_1_KORDINATA_VRATA  # 440
            self.y_kordinata_vrata = Y_1_KORDINATA_VRATA  # 746

        elif self.ulaz == 2:
            self.x_kordinata_vrata = X_2_KORDINATA_VRATA  # 0
            self.y_kordinata_vrata = Y_2_KORDINATA_VRATA  # 300

        elif self.ulaz == 3:
            self.x_kordinata_vrata = X_3_KORDINATA_VRATA  # 1040
            self.y_kordinata_vrata = Y_3_KORDINATA_VRATA  # 300

        if self.izlaz == 0:
            self.x_kordinata_vrata2 = X_0_KORDINATA_VRATA  # 440
            self.y_kordinata_vrata2 = Y_0_KORDINATA_VRATA  # 0

        elif self.izlaz == 1:
            self.x_kordinata_vrata2 = X_1_KORDINATA_VRATA  # 440
            self.y_kordinata_vrata2 = Y_1_KORDINATA_VRATA  # 746

        elif self.izlaz == 2:
            self.x_kordinata_vrata2 = X_2_KORDINATA_VRATA  # 0
            self.y_kordinata_vrata2 = Y_2_KORDINATA_VRATA  # 300

        elif self.izlaz == 3:
            self.x_kordinata_vrata2 = X_3_KORDINATA_VRATA  # 1040
            self.y_kordinata_vrata2 = Y_3_KORDINATA_VRATA  # 300

    def postoji(self):
        window.blit(self.loading, (self.x_kordinata_sobe, self.y_kordinata_sobe))
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
        if self.izlaz == 0:
            self.izaberi()
            
            print(1)
        self


class Bullet:
    def __init__(self, x, y, vel, damage, no_infinite_pierce):
        self.x = x
        self.y = y
        self.vel_X = vel[0]
        self.vel_Y = vel[1]
        self.damage = damage
        self.no_infinite_pierce = no_infinite_pierce * fps
        self.no_infinite_pierce2 = no_infinite_pierce * fps

    def postoji(self):
        window.blit(metak, (self.x - 8, self.y - 4))

    def bullet_colided(self, player):
        if (
            abs(self.x - player.x) <= 20 and abs(self.y - player.y) <= 20
        ) and self.no_infinite_pierce <= 0:
            player.hp -= self.damage
            self.no_infinite_pierce = self.no_infinite_pierce2

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
        self.speed = 7

    def postoji(self):
        window.blit(igraccc, (self.x - 20, self.y - 20))

    def right(self):
        self.x += self.speed

    def left(self):
        self.x -= self.speed

    def up(self):
        self.y -= self.speed

    def down(self):
        self.y += self.speed

    def shoot(self, mouse_pos):
        vx = mouse_pos[0] - self.x
        vy = mouse_pos[1] - self.y
        b = Bullet(self.x, self.y, (vx, vy), 200, 0.1)
        self.bullets.append(b)

    def cltaj(self, x_mouse, y_mouse, enemy):
        for bullet in self.bullets:
            bullet.postoji()
            bullet.bullet_colided(enemy)
            bullet.no_infinite_pierce -= 1
            bullet.pomeraj_se(bullet.vel_X, bullet.vel_Y)

    def colision(self):
        if self.x > SOBA_MAX_X:  # 1020
            self.x -= self.speed
        elif self.x < SOBA_MIN_X:
            self.x += self.speed
        if self.y > SOBA_MAX_Y:  # 731
            self.y -= self.speed
        elif self.y < SOBA_MIN_Y:
            self.y += self.speed


class Enemy:
    def __init__(self, x, y, vrsta, hp, max_hp):
        self.x = x
        self.y = y
        self.type = vrsta
        self.zullets = []
        self.hp = hp
        self.max_hp = max_hp
        if self.type == "runner":
            self.speed = 7
        elif self.type == "gunner":
            self.speed = 5

    def postoji(self):
        if self.type == "runner":
            window.blit(zunner, (self.x - 15, self.y - 15))
        elif self.type == "gunner":
            window.blit(zgunner, (self.x - 15, self.y - 15))

    def colision(self):
        if self.x > width - 60:  # 1020
            self.x -= self.speed
        elif self.x < SOBA_MIN_X:
            self.x += self.speed
        if self.y > height - 69:  # 700
            self.y -= self.speed
        elif self.y < SOBA_MIN_Y:
            self.y += self.speed

    def run(self, player):
        if self.type == "runner":
            if (abs(player.x - self.x) <= 200 or abs(player.y - self.y) <= 200) and (
                abs(player.x - self.x) >= 40 or abs(player.y - self.y) >= 40
            ):
                if player.x < self.x:
                    self.x -= self.speed
                else:
                    self.x += self.speed
                if player.y <= self.y:
                    self.y -= self.speed
                else:
                    self.y += self.speed
        elif self.type == "gunner":
            if (abs(player.x - self.x) <= 600 or abs(player.y - self.y) <= 600) and (
                abs(player.x - self.x) >= 200 or abs(player.y - self.y) >= 200
            ):
                if player.x < self.x:
                    self.x -= self.speed
                else:
                    self.x += self.speed
                if player.y <= self.y:
                    self.y -= self.speed
                else:
                    self.y += self.speed
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
            zullet.no_infinite_pierce -= 1
            zullet.pomeraj_se(player.x, player.y)

    def gledaj(self, player, slika):  # NE RADI
        mrzonja = m.sqrt(player.x * player.x + player.y + player.y)
        smaranje = m.sin((1 / player.x) / (1 / mrzonja)) + 50
        slika = pg.transform.rotate(slika, smaranje)
        print(smaranje)


iglac = Player(100, 500, 1000, 100)
vojislav = Enemy(100, 100, "runner", 100, 100)
milan = Enemy(100, 700, "gunner", 100, 100)
stvar = Bullet(100, 100, [x_mouse, y_mouse], 10, 1)
sobica = soba(0, 3, 1)

window = pg.display.set_mode((width, height))

pg.display.set_caption("iglica")
sobica.izaberi()
wave_cleared = True

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
        iglac.cltaj(x_mouse, y_mouse, milan)
        iglac.colision()
        stvar.bullet_colided(iglac)
        stvar.pomeraj_se(iglac.x, iglac.y)
        stvar.postoji()
        milan.cltaj(x_mouse, y_mouse, iglac)
        if milan.hp > 0:
            milan.postoji()
            milan.run(iglac)
            milan.shoot(iglac)
            milan.colision()
            print(milan.hp)
        else:
            ("milan je otisao gore")
        vojislav.run(iglac)
        vojislav.postoji()
        vojislav.colision()
        window.blit(hp, (625, 50))
        if wave_cleared == True:
            if (
                iglac.x >= X_0_KORDINATA_VRATA
                and iglac.x <= X_0_KORDINATA_VRATA + 192
                and iglac.y <= SOBA_MIN_X + 50
                and sobica.izlaz == 0
            ):
                iglac.x = X_1_KORDINATA_VRATA + 92
                iglac.y = Y_1_KORDINATA_VRATA
                sobica.izaberi()

            if (
                iglac.x >= X_1_KORDINATA_VRATA
                and iglac.x <= X_1_KORDINATA_VRATA + 192
                and iglac.y >= SOBA_MAX_Y - 50
                and sobica.izlaz == 1
            ):
                iglac.x = X_0_KORDINATA_VRATA + 92
                iglac.y = Y_0_KORDINATA_VRATA + SOBA_MIN_Y + 30
                sobica.izaberi()

            if (
                iglac.y >= Y_2_KORDINATA_VRATA
                and iglac.y <= Y_2_KORDINATA_VRATA + 192
                and iglac.x <= SOBA_MIN_X + 50
                and sobica.izlaz == 2
            ):
                iglac.x = X_3_KORDINATA_VRATA + 92
                iglac.y = Y_3_KORDINATA_VRATA + SOBA_MIN_X + 30
                sobica.izaberi()
            
            if (  # OD OVDE POCINJU BAGOVI
                iglac.y >= Y_3_KORDINATA_VRATA
                and iglac.y <= Y_3_KORDINATA_VRATA + 192
                and iglac.x >= SOBA_MAX_X - 50
                and sobica.izlaz == 3
            ):
                iglac.x = SOBA_MIN_X + 50
                iglac.y = Y_2_KORDINATA_VRATA + 92
                sobica.izaberi()
            
            

    else:
        window.blit(text_surface, (300, 375))

    if iglac.x <= 0:
        sobica.izaberi
        print(1)

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
    stvar.no_infinite_pierce -= 1
    print(iglac.hp, stvar.no_infinite_pierce)

    clock.tick(fps)
    pg.display.update()
