import pygame, sys, random

SIZE = W, H = (400, 400)
GREY = (59, 59, 59)
WHITE = (255, 255, 255)
ORANGE = (255, 104, 0)
tiles = 40
side = round(W / tiles)
speed = 1


class Food:
    def __init__(self):
        self.i = random.randint(0, tiles - 1)
        self.j = random.randint(0, tiles - 1)
        self.r = round(side / 2)

    def draw(self, screen):
        x = round(self.i * side + side / 2)
        y = round(self.j * side + side / 2)
        pygame.draw.circle(screen, ORANGE, (x, y), self.r)

    def respawn(self):
        self.i = random.randint(0, tiles - 1)
        self.j = random.randint(0, tiles - 1)


class Snake:
    def __init__(self):
        i = random.randint(0, tiles - 1)
        j = random.randint(0, tiles - 1)
        self.body = []
        self.body.append([i, j])
        self.dir = [False, False, False, True]  # Top Left Bottom Right
        self.alive = True

    def eat(self, food):
        tile = self.body[0]

        for i in range(1, len(self.body)):
            anoth = self.body[i]
            if tile[0] == anoth[0] and tile[1] == anoth[1]:
                self.alive = False

        if tile[0] == food.i and tile[1] == food.j:
            food.respawn()
            self.body.append([tile[0], tile[1]])

    def move(self):
        i = len(self.body) - 1
        while i > 0:
            self.body[i] = self.body[i - 1].copy()
            i = i - 1

        tile = self.body[0]
        if self.dir[0]:
            tile[1] = tile[1] - speed
            if tile[1] < 0: tile[1] = H / side
        elif self.dir[1]:
            tile[0] = tile[0] - speed
            if tile[0] < 0: tile[0] = H / side
        elif self.dir[2]:
            tile[1] = tile[1] + speed
            if tile[1] >= H / side: tile[1] = 0
        elif self.dir[3]:
            tile[0] = tile[0] + speed
            if tile[0] >= W / side: tile[0] = 0

    def setDir(self, direct):
        for i in range(len(self.dir)):
            if (self.dir[i]): curDir = i
        if abs(direct - curDir) % 2 != 0:
            self.dir[curDir] = False
            self.dir[direct] = True

    def draw(self, screen):
        for tile in self.body:
            x = tile[0] * side
            y = tile[1] * side
            pygame.draw.rect(screen, WHITE, (x, y, side, side))


def run():
    pygame.init()
    pygame.display.set_caption("SNAKE")
    screen = pygame.display.set_mode(SIZE)

    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()

    while 1:
        clock.tick(24)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.setDir(0)
                elif event.key == pygame.K_LEFT:
                    snake.setDir(1)
                elif event.key == pygame.K_DOWN:
                    snake.setDir(2)
                elif event.key == pygame.K_RIGHT:
                    snake.setDir(3)

        if snake.alive:
            snake.move()
            snake.eat(food)

        screen.fill(GREY)

        snake.draw(screen)
        food.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    run()