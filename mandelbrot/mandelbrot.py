import pygame
from sys import exit

SIZE = W, H = (600, 400)
WHITE = (255, 255, 255)
GREY = (59, 59, 59)
BLACK = (0, 0, 0)


class Mandelbrot_Set:
    def draw(self, surface):
        maxIt = 100

        for j in range(H):
            for i in range(W):
                a = (lambda x: x * 3.2 / W - 2.2)(i)
                b = (lambda x: x * 3.2 / H - 1.6)(j)

                ca = a
                cb = b

                n = 0
                while n < maxIt:
                    aa = a * a - b * b
                    bb = 2 * a * b
                    a = aa + ca
                    b = bb + cb

                    if abs(a + b) > 4:
                        break

                    n = n + 1

                br = (lambda x: round(x * 255 / 100))(n)
                if n == maxIt:
                    br = 0

                surface.fill((br, 0, br), (i, j, 1, 1))


def run():
    pygame.init()
    pygame.display.set_caption("MANDELBROT SET")
    surface = pygame.display.set_mode(SIZE)
    surface.set_alpha(100)

    m_set = Mandelbrot_Set()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    m_set.draw(surface)

        pygame.display.update()


if __name__ == "__main__":
    run()