import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    import pygame
except ImportError:
    install("pygame")
finally:
    import pygame

WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.update()


if __name__ == '__main__':
    main()
