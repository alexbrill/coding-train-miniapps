import pygame, sys, random

SCREEN_SIZE = (WIDTH, HEIGHT) = 600, 400

WHITE = (255, 255, 255)
PURPLE = (148, 0, 211)

DROPS_QUAN = 600


class Drop:

    def __init__(self):
        self.thick = random.randint(1, 2)
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-300, 150)
        self.length = random.randint(2, 10)

        if (self.thick == 1):
            self.speed = random.random() / 4
        else:
            self.speed = random.random()

    def update(self):
        self.y = self.y + self.speed

        if self.y > HEIGHT:
            self.y = random.randint(-20, 50)

    def draw(self, screen):
        pygame.draw.line(screen, PURPLE, [self.x, self.y],
                         [self.x, self.y + self.length], self.thick)


def run():
    pygame.init()
    pygame.display.set_caption("Purple Rain")

    screen = pygame.display.set_mode(SCREEN_SIZE)

    drops = []

    for i in range(DROPS_QUAN):
        drops.append(Drop())

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

        screen.fill(WHITE)

        for i in range(DROPS_QUAN):
            drops[i].update()
            drops[i].draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    run()