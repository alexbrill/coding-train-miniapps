import pygame, sys, math

SIZE = W, H = (960, 600)
GREY = (59, 59, 59)
MAGENTA = (220, 12, 220)
CYAN = (25, 255, 255)
GREEN = (12, 250, 34)

r1 = 200
r2 = 200
m1 = 10
m2 = 10
a1 = math.pi / 2
a2 = math.pi / 5
a1_v = 0
a2_v = 0
g = 2
prX = -1
prY = -1


class D_Pendulum:
    def __init__(self):
        self.x0 = W / 2
        self.y0 = 70

    def update(self, screen, fig):
        global a1, a2, a1_v, a2_v, prX, prY

        x1 = round(r1 * math.sin(a1) + self.x0)
        y1 = round(r1 * math.cos(a1) + self.y0)
        x2 = round(r2 * math.sin(a2) + x1)
        y2 = round(r2 * math.cos(a2) + y1)

        num1 = -g * (2 * m1 + m2) * math.sin(a1)
        num2 = -m2 * g * math.sin(a1 - 2 * a2)
        num3 = -2 * math.sin(a1 - a2) * m2
        num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * math.cos(a1 - a2)
        num5 = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))

        a1_a = (num1 + num2 + num3 * num4) / num5

        num1 = 2 * math.sin(a1 - a2)
        num2 = a1_v * a1_v * r1 * (m1 + m2)
        num3 = g * (m1 + m2) * math.cos(a1)
        num4 = a2_v * a2_v * r2 * m2 * math.cos(a1 - a2)
        num5 = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))

        a2_a = (num1 * (num2 + num3 + num4)) / num5

        a1_v = a1_v + a1_a
        a2_v = a2_v + a2_a
        a1 = a1 + a1_v
        a2 = a2 + a2_v

        a1_v = a1_v * 0.999
        a2_v = a2_v * 0.999

        pygame.draw.line(screen, MAGENTA, (self.x0, self.y0), (x1, y1))
        pygame.draw.circle(screen, MAGENTA, (x1, y1), m1)
        pygame.draw.line(screen, MAGENTA, (x1, y1), (x2, y2))
        pygame.draw.circle(screen, MAGENTA, (x2, y2), m2)

        if prX != -1:
            pygame.draw.line(fig, CYAN, (x2, y2), (prX, prY), 2)
        pygame.draw.circle(fig, GREEN, (x2, y2), 1)

        prX = x2
        prY = y2


def run():
    pygame.init()
    pygame.display.set_caption("DOUBLE PENDULUM")
    screen = pygame.display.set_mode(SIZE)
    fig = pygame.Surface(SIZE)

    A = D_Pendulum()
    clock = pygame.time.Clock()

    while 1:
        clock.tick(35)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

        screen.fill(GREY)

        A.update(screen, fig)
        fig.set_alpha(100)
        screen.blit(fig, (0, 0))

        pygame.display.update()


if __name__ == "__main__":
    run()