import pygame, sys, math

SIZE = W, H = (800, 600)
GREY = (59, 59, 59)
WHITE = (255, 255, 255)
ANGLE = math.pi / 4
SCL1 = 0.75
SCL2 = 0.5


def branch(screen, st, end):
    pygame.draw.line(screen, WHITE, st, end)
    pygame.display.update()

    dist = math.sqrt((end[0] - st[0]) * (end[0] - st[0])
                     + (end[1] - st[1]) * (end[1] - st[1]))

    if dist > 3:
        pX = end[0] - st[0]
        pY = end[1] - st[1]

        nX1 = (pX - pY) * ANGLE * SCL1
        nY1 = (pX + pY) * ANGLE * SCL1

        nX2 = (pX + pY) * ANGLE * SCL2
        nY2 = (-pX + pY) * ANGLE * SCL2

        branch(screen, end, (end[0] + nX1, end[1] + nY1))
        branch(screen, end, (end[0] + nX2, end[1] + nY2))


def run():
    pygame.init()
    pygame.display.set_caption("Fractal Tree")

    screen = pygame.display.set_mode(SIZE)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                branch(screen, (W / 2, 0), (W / 2, H / 4))

        screen.fill(GREY)

        pygame.display.update()


if __name__ == "__main__":
    run()