import pygame
from sys import exit
from math import sqrt
from random import random

FPS = 30
SIZE = W, H = (700, 700)
GREY = (51, 51, 51)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (12, 12, 244)
GREEN = (32, 240, 35)
MAGENTA = (230, 12, 240)
cols = 80
rows = 80
c_width = W / cols
c_height = H / rows


def heuristic(a, b):
    d = sqrt((a.i - b.i) ** 2 + (a.j - b.j) ** 2)
    # d = abs(a.i - b.i) + abs(a.j - b.j)
    return d


def index(i, j):
    return j + i * cols


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.wall = random() < 0.4
        if self.wall:
            self.col = GREY
        else:
            self.col = WHITE

    def show(self, screen):
        pygame.draw.circle(screen, self.col, \
                           (round(self.j * c_width + c_width / 2), \
                            round(self.i * c_height + c_height / 2)), 3)

    def addNeighbors(self, grid):
        i = self.i
        j = self.j
        if i - 1 >= 0:
            self.neighbors.append(grid[index(i - 1, j)])
        if i + 1 < cols:
            self.neighbors.append(grid[index(i + 1, j)])
        if j - 1 >= 0:
            self.neighbors.append(grid[index(i, j - 1)])
        if j + 1 < rows:
            self.neighbors.append(grid[index(i, j + 1)])
        if i - 1 >= 0 and j - 1 >= 0:
            self.neighbors.append(grid[index(i - 1, j - 1)])
        if i - 1 >= 0 and j + 1 < rows:
            self.neighbors.append(grid[index(i - 1, j + 1)])
        if i + 1 < cols and j - 1 >= 0:
            self.neighbors.append(grid[index(i + 1, j - 1)])
        if i + 1 < cols and j + 1 < rows:
            self.neighbors.append(grid[index(i + 1, j + 1)])


def run():
    pygame.init()
    pygame.display.set_caption("A*")
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    grid = []
    openSet = []
    closedSet = []
    path = []

    for i in range(rows):
        for j in range(cols):
            grid.append(Cell(i, j))

    for el in grid:
        el.addNeighbors(grid)

    start = grid[0]
    end = grid[len(grid) - 1]

    start.wall = False
    start.col = WHITE
    end.wall = False
    end.col = WHITE

    openSet.append(start)

    while 1:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if len(openSet) > 0:
            winner = 0
            for i in range(len(openSet)):
                if openSet[i].f < openSet[winner].f:
                    winner = i

            curr = openSet[winner]

            if curr == end:
                print("END")
                break

            closedSet.append(curr)
            openSet.remove(curr)

            for n in curr.neighbors:
                newPath = False
                if not n in closedSet and not n.wall:
                    temp = curr.g + 1
                    if n in openSet:
                        if temp < n.g:
                            n.g = temp
                            newPath = True
                    else:
                        n.g = temp
                        newPath = True
                        openSet.append(n)

                    if newPath:
                        n.h = heuristic(n, end)
                        n.f = n.g + n.h
                        n.prev = curr
        else:
            print("NO SOLUTION")
            break

        path.clear()
        temp = curr
        path.append(temp)
        while temp.prev != None:
            path.append(temp.prev)
            temp = temp.prev

        coords = []
        for el in path:
            x = el.j * c_height + c_height / 2
            y = el.i * c_width + c_width / 2
            coords.append([x, y])

        screen.fill(WHITE)
        for cell in grid:
            cell.show(screen)
        for i in range(len(coords) - 1):
            pygame.draw.line(screen, MAGENTA, \
                             coords[i], coords[i + 1], 4)

        pygame.display.update()


if __name__ == "__main__":
    run()