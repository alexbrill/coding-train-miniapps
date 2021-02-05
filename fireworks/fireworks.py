import pygame as pg
from sys import exit
from random import randint, random

SIZE = W, H = 800, 600
GREY = (59, 59, 59)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

quan_of_part = 100
chance = 0.07


class coord:
    def __init__(self, x, y):
        self.set(x, y)

    def set(self, x, y):
        self.x = x
        self.y = y

    def add(self, another):
        self.x = self.x + another.x
        self.y = self.y + another.y

    def mult(self, num):
        self.x = self.x * num
        self.y = self.y * num

    def getRound2DVector(self):
        return round(self.x), round(self.y)


gravity = coord(0, 0.5)


class Particle:
    def __init__(self, x, y, one=True):
        self.coord = coord(x, y)
        self.acc = coord(0, 0)
        self.exist = True
        self.van = 1
        self.one = one

        if self.one:
            self.r = 3
            self.vel = coord(0, randint(-25, -9))
        else:
            self.r = 1
            self.vel = coord(random() * randint(-6, 6),
                             random() * randint(-6, 8))

    def applyForce(self, force):
        self.acc.add(force)

    def draw(self, screen, color):
        if not self.one:
            for i in range(len(color)):
                color[i] = round(color[i] * self.van)
            self.van = self.van - 0.00065

        pg.draw.circle(screen, color,
                       self.coord.getRound2DVector(), self.r)

    def update(self):
        self.applyForce(gravity)
        self.vel.add(self.acc)
        self.coord.add(self.vel)
        self.acc.mult(0)

        if self.coord.y > H:
            self.exist = False


class Firework:
    def __init__(self, x, y):
        self.particles = []
        self.particles.append(Particle(x, y))
        self.exploded = False
        self.ended = False
        self.color = [randint(50, 255),
                      randint(50, 255), randint(50, 255)]

    def update(self):
        for particle in self.particles:
            particle.update()
            if not self.exploded and particle.vel.y > 0:
                self.exploded = True
                self.particles.remove(particle)
                for i in range(quan_of_part):
                    self.particles.append(Particle(particle.coord.x,
                                                   particle.coord.y, False))

            if not particle.exist:
                self.particles.remove(particle)

        if self.exploded and len(self.particles) == 0:
            self.ended = True

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen, self.color)


def run():
    pg.init()
    pg.display.set_caption = "FIREWORKS"
    screen = pg.display.set_mode(SIZE)
    clock = pg.time.Clock()

    fireworks = []

    while 1:
        clock.tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        if random() < chance:
            fireworks.append(Firework(randint(0, W), H))

        for firework in fireworks:
            firework.update()

            if firework.ended:
                fireworks.remove(firework)

        screen.fill(BLACK)
        for firework in fireworks:
            firework.draw(screen)

        pg.display.update()


if __name__ == "__main__":
    run()