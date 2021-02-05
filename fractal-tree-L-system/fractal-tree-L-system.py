import pygame
from sys import exit
from math import sin, cos, pi

SIZE = W, H = (1000, 600)
GREY = (59, 59, 59)
WHITE = (255, 255, 255)

ANGLE = 25 * pi / 180
SCL = 0.5
LENGTH = 100


def rotate(x, y, a):
    rx = x * cos(a) - y * sin(a)
    ry = x * sin(a) + y * cos(a)
    return [rx, ry]


def rule1(sentence):
    next_one = ""
    for ch in sentence:
        if ch == 'F':
            next_one = next_one + "FF+[+F-F-F]-[-F+F+F]"
        else:
            next_one = next_one + ch
    return next_one


def rule2(sentence):
    next_one = ""
    for ch in sentence:
        if ch == 'X':
            next_one = next_one + "F-[[X]+X]+F[+FX]-X"
        elif ch == 'F':
            next_one = next_one + "FF"
        else:
            next_one = next_one + ch
    return next_one


def draw_tree(screen, sentence, clock, scl, st_angle, st_x, st_y):
    stack = []
    angle = st_angle
    l = 75

    x = st_x
    y = st_y

    # print(sentence)

    for ch in sentence:
        if ch == 'F':
            vect = rotate(0, -l * scl, angle)
            px = x
            py = y
            x = x + vect[0]
            y = y + vect[1]

            pygame.draw.circle(screen, (30, 220, 130),
                               (round(x), round(y)), 1)
            pygame.draw.line(screen, GREY, (px, py), (x, y), 2)

        elif ch == '+':
            angle = angle + ANGLE
        elif ch == '-':
            angle = angle - ANGLE
        elif ch == '[':
            stack.append([x, y, angle])
        elif ch == ']':
            buff = stack.pop()
            x = buff[0]
            y = buff[1]
            angle = buff[2]


def run():
    pygame.init()
    pygame.display.set_caption("L-system")
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    screen.fill(WHITE)
    pygame.display.update()

    sentence1 = "F"
    sentence2 = "X"

    scl = 1

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_SPACE:
                screen.fill(WHITE)
                sentence1 = rule1(sentence1)
                sentence2 = rule2(sentence2)
                draw_tree(screen, sentence1, clock, scl, 0, 700, H)
                draw_tree(screen, sentence2, clock, scl, ANGLE, 50, H)
                scl = scl * SCL

                pygame.display.update()


if __name__ == "__main__":
    run()