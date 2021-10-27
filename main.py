"""
Conway's Game of Life using pygame
"""

import copy
import examples
import logging
import random
# Package installation
import subprocess
import sys

# Logging setup
with open("main.log", "w+") as fp: pass
logging.basicConfig(filename="main.log", level=logging.INFO)


def install(package: str) -> None:
    """
    Uses pip to install the specified package.

    :param package: name of package to install as a string
    :return: None
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    import pygame
except ImportError:
    install("pygame")
finally:
    import pygame

# Colors
BLACK = (0, 0, 0)
GRAY = (176, 176, 176)
WHITE = (250, 250, 250)

# pygame
WRAP = True    # flag for wrapping
SQUARE = 10
GRID_WIDTH = 100
GRID_HEIGHT = 100
WIDTH = GRID_WIDTH * SQUARE
HEIGHT = GRID_HEIGHT * SQUARE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30
pygame.display.set_caption("Conway's Game of Life")


def main():
    """
    Main execution function.

    :return: None
    """

    # Initialize grid
    # grid: list[list[int]] = [[random.randint(0, 1) for i in range(GRID_WIDTH)] for j in range(GRID_HEIGHT)]
    grid = examples.get_example("stones", GRID_WIDTH, GRID_HEIGHT)

    background = pygame.Surface(SCREEN.get_size()).convert()
    background.fill((0, 0, 0))

    SCREEN.blit(background, (0, 0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                x, y = SQUARE * j, SQUARE * i
                sq = pygame.Rect(x, y, SQUARE, SQUARE)
                pygame.draw.rect(SCREEN, WHITE if cell else BLACK, sq, 0)

        grid = step(grid)

        pygame.display.flip()
        # pygame.time.Clock().tick(FPS)


def step(grid: list[list[int]]) -> list[list[int]]:
    """
    Steps the grid forward 1 generation based on the GoL rules. Modifies the grid in place.

    :param grid: the grid to modify
    :return: None
    """

    grid_out: list[list[int]] = copy.deepcopy(grid)

    grid_width: int = len(grid[0])
    grid_height: int = len(grid)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            n_neighbors: int = 0
            for m in (-1, 0, 1):
                for n in (-1, 0, 1):
                    if m == 0 and n == 0: continue
                    n_y = y + m
                    n_x = x + n
                    if WRAP:
                        if n_x >= grid_width: n_x -= grid_width
                        if n_y >= grid_height: n_y -= grid_height
                        n_neighbors += grid[n_y][n_x]
                    elif 0 <= n_x < grid_width and 0 <= n_y < grid_height:
                        n_neighbors += grid[n_y][n_x]

            # Only check for the cases where we need to flip the state
            if (cell and n_neighbors not in (2, 3)) or (not cell and n_neighbors == 3):
                grid_out[y][x] = 1 - cell

    return grid_out


if __name__ == '__main__':
    main()
