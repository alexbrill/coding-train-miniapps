import pygame, sys, random, math

SIZE = w, h = (600, 600)
GREY = (59, 59, 59)
MAGENTA = (220, 12, 220)
YELLOW = (220, 220, 12)
CYAN = (12, 220, 220)
rows = 30
columns = 30
cw = round(w / rows)
ch = round(h / columns)


def index(i, j):
    if i < 0 or j < 0 or i >= columns or j >= rows:
        return None
    return i + j * columns


def removeWalls(cur, next_one):
    x = cur.i - next_one.i
    y = cur.j - next_one.j

    if x == 1:
        cur.bord[3] = False
        next_one.bord[1] = False
    elif x == -1:
        cur.bord[1] = False
        next_one.bord[3] = False
    if y == 1:
        cur.bord[0] = False
        next_one.bord[2] = False
    elif y == -1:
        cur.bord[2] = False
        next_one.bord[0] = False


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.bord = [True, True, True, True]  # Top Right Bottom Left
        self.visited = False

    def draw(self, screen):
        x = self.i * cw
        y = self.j * ch

        if self.visited:
            pygame.draw.rect(screen, YELLOW, (x, y, cw, ch))
        if self.bord[0]:
            pygame.draw.line(screen, MAGENTA, (x, y), (x + cw, y))
        if self.bord[1]:
            pygame.draw.line(screen, MAGENTA, (x + cw, y), (x + cw, y + ch))
        if self.bord[2]:
            pygame.draw.line(screen, MAGENTA, (x, y + ch), (x + cw, y + ch))
        if self.bord[3]:
            pygame.draw.line(screen, MAGENTA, (x, y), (x, y + ch))

    def highLight(self, screen):
        x = self.i * cw
        y = self.j * ch
        pygame.draw.rect(screen, CYAN, (x, y, cw, ch))

    def getNeighbor(self, grid):
        neighbors = []

        topI = index(self.i, self.j - 1)
        rightI = index(self.i + 1, self.j)
        bottomI = index(self.i, self.j + 1)
        leftI = index(self.i - 1, self.j)

        if ((topI is not None) and (not grid[topI].visited)):
            neighbors.append(grid[topI])
        if ((rightI is not None) and (not grid[rightI].visited)):
            neighbors.append(grid[rightI])
        if ((bottomI is not None) and (not grid[bottomI].visited)):
            neighbors.append(grid[bottomI])
        if ((leftI is not None) and (not grid[leftI].visited)):
            neighbors.append(grid[leftI])

        if len(neighbors) > 0:
            return neighbors[random.randint(0, len(neighbors) - 1)]
        else:
            return None


def run():
    pygame.init()
    pygame.display.set_caption("MAZE GENERATOR")
    screen = pygame.display.set_mode(SIZE)

    grid = []
    stack = []

    for j in range(rows):
        for i in range(columns):
            grid.append(Cell(i, j))

    cur = grid[0]

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        cur.visited = True
        next_one = cur.getNeighbor(grid)

        if next_one is not None:
            stack.append(cur)
            removeWalls(cur, next_one)
            cur = next_one
        elif len(stack) > 0:
            cur = stack.pop()

        screen.fill(GREY)

        for i in range(columns * rows):
            grid[i].draw(screen)

        cur.highLight(screen)

        pygame.display.update()


if __name__ == "__main__":
    run()