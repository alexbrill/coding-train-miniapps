import pygame
from pygame import *
from sys import exit
from random import randint as rand
from math import sqrt, pi

NAME = "AGAR.IO"
SIZE = W, H = (800, 600)
FPS = 30
GREY = (59, 59, 59)
WHITE = (255, 255, 255)
QUAN = 120


def dist(x0, y0, x1, y1):
    return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)


class Blob:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.c = (rand(0, 255), rand(0, 255), rand(0, 255))

    def respawn(self):
        self.x = rand(-W, 2 * W)
        self.y = rand(-H, 2 * H)

    def eats(self, blob):
        d = dist(self.x, self.y, blob.x, blob.y)

        if d <= self.r + blob.r:
            S = self.r ** 2 * pi + blob.r ** 2 * pi
            self.r = sqrt(S / pi)
            # self.r = self.r + blob.r
            return True
        else:
            return False

    def move_to(self, coord):
        self.x = self.x + (coord[0] - W / 2) / W * 10
        self.y = self.y + (coord[1] - H / 2) / H * 10

    def draw(self, screen, offset_x=0, offset_y=0):
        draw.circle(screen, self.c, \
                    (round(self.x - offset_x), round(self.y - offset_y)), round(self.r))


def run():
    pygame.init()
    display.set_caption(NAME)
    screen = display.set_mode(SIZE)
    clock = time.Clock()

    blob = Blob(W / 2, H / 2, 15)

    blobs = []

    for i in range(QUAN):
        blobs.append(Blob(rand(-W, 2 * W), rand(-H, 2 * H), 5))

    while 1:
        clock.tick(FPS)

        for e in event.get():
            if e.type == QUIT:
                quit()
                exit()

        m_coord = mouse.get_pos()
        blob.move_to(m_coord)

        screen.fill(GREY)

        i = len(blobs) - 1
        while i >= 0:
            if blob.eats(blobs[i]):
                blobs.remove(blobs[i])
            else:
                blobs[i].draw(screen, blob.x - W / 2, blob.y - H / 2)
            i = i - 1

        for i in range(len(blobs)):
            if blob.eats(blobs[i]):
                blobs[i].respawn()
                # blobs.remove(blobs[i])
            blobs[i].draw(screen, blob.x - W / 2, blob.y - H / 2)

        blob.draw(screen, blob.x - W / 2, blob.y - H / 2)
        draw.rect(screen, WHITE, (-W - blob.x + W / 2, -H - blob.y + H / 2, \
                                  3 * W, 3 * H), 1)

        display.update()


if __name__ == "__main__":
    run()