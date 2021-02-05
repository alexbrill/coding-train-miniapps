import pygame
from pygame import *
from sys import exit
from math import sin, cos, pi, sqrt
from random import randint as rand
from random import random

# ___WINDOW___
SIZE = W, H = (800, 600)
NAME = "ASTEROIDS"
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (51, 51, 51)

# ____SHIP_____
DUMPING = 0.97
S_THICK = 3
S_RAD = 20

# __ASTEROIDS__
A_AMOUNT = 10
A_THICK = 1

# ____LAZER____
L_SPEED = 8
L_RAD = 1


def dist(x0, y0, x1=0, y1=0):
    return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)


DIAG = dist(W, H)


def rotate(x, y, a, off_x=0, off_y=0):
    rx = x * cos(a) - y * sin(a) + off_x
    ry = x * sin(a) + y * cos(a) + off_y
    return [rx, ry]


class Lazer():
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.alive = True
        self.r = L_RAD
        vect = rotate(0, -1, angle)
        self.vx = vect[0]
        self.vy = vect[1]

    def isAlive(self):
        if self.x > W or self.x < 0 or self.y > H or self.y < 0:
            self.alive = False

    def hits(self, targ):
        d = dist(self.x, self.y, targ.x, targ.y)
        if d <= self.r + targ.r:
            return True

    def update(self):
        self.x = self.x + self.vx * L_SPEED
        self.y = self.y + self.vy * L_SPEED
        self.isAlive()

    def render(self, screen):
        draw.circle(screen, WHITE, \
                    (round(self.x), round(self.y)), self.r)


class Asteroid():
    def __init__(self, x=-1, y=-1):
        self.x = rand(0, W)
        self.y = rand(0, H)
        self.r = rand(7, 26)
        self.vx = random() * 2 - 1
        self.vy = random() * 2 - 1
        self.total = rand(3, 14)
        self.offset = []
        for n in range(self.total):
            self.offset.append(rand(-5, 5))

        if x != -1 and y != -1:
            self.x = x
            self.y = y

    def edges(self):
        if self.x > W + self.r:
            self.x = -self.r
        elif self.x < -self.r:
            self.x = W + self.r
        if self.y > H + self.r:
            self.y = -self.r
        elif self.y < -self.r:
            self.y = H + self.r

    def render(self, screen):
        fig = []
        for n in range(self.total):
            angle = n / self.total * (2 * pi)
            fig.append(rotate(0, -self.r, angle, \
                              self.x + self.offset[n], self.y + self.offset[n]))
        draw.polygon(screen, WHITE, fig, A_THICK)

    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.edges()


class Ship:
    def __init__(self):
        self.x = W / 2
        self.y = H / 2
        self.r = S_RAD
        self.heading = 0
        self.vx = 0
        self.vy = 0

    def edges(self):
        if self.x > W + self.r:
            self.x = -self.r
        elif self.x < -self.r:
            self.x = W + self.r
        if self.y > H + self.r:
            self.y = -self.r
        elif self.y < -self.r:
            self.y = H + self.r

    def boost(self):
        force = rotate(0, -1, self.heading)
        self.vx = self.vx + force[0]
        self.vy = self.vy + force[1]

    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.vx = self.vx * DUMPING
        self.vy = self.vy * DUMPING
        self.edges()

    def render(self, screen):
        point1 = rotate(-self.r, self.r, self.heading, self.x, self.y)
        point2 = rotate(self.r, self.r, self.heading, self.x, self.y)
        point3 = rotate(0, -self.r, self.heading, self.x, self.y)
        draw.polygon(screen, WHITE, (point1, point2, point3), S_THICK)

    def turn(self, angle):
        self.heading = self.heading + angle


def run():
    pygame.init()
    display.set_caption(NAME)
    screen = display.set_mode(SIZE)
    clock = time.Clock()

    ship = Ship()
    asteroids = []
    lazers = []

    for n in range(A_AMOUNT):
        asteroids.append(Asteroid())

    while 1:
        clock.tick(FPS)

        for e in event.get():
            if e.type == QUIT:
                quit()
                exit()

        pressed1, pressed2, pressed3 = mouse.get_pressed()
        if pressed1:
            ship.turn(-0.1)
        if pressed3:
            ship.turn(0.1)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            ship.boost()
        if key_pressed[pygame.K_SPACE]:
            lazers.append(Lazer(ship.x, ship.y, ship.heading))

        ship.update()
        screen.fill(BLACK)

        for ast in asteroids:
            ast.update()
            ast.render(screen)

        for laz in lazers:
            if laz.alive:
                laz.update()
                for i in range(len(asteroids) - 1, -1, -1):
                    if laz.hits(asteroids[i]):
                        lazers.remove(laz)
                        asteroids.remove(asteroids[i])
                        asteroids.append(Asteroid(laz.x, laz.y))
                        asteroids.append(Asteroid(ast.x, ast.y))

                laz.render(screen)
            else:
                lazers.remove(laz)

        ship.render(screen)

        display.update()


if __name__ == "__main__":
    run()
