import pygame
import sys

def main():
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

if __name__ == "__main__":
    main()