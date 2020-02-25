import pygame
import sys
from Player import Player


def main():
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    BLACK = (0, 0, 0)

    player = Player()
    all_sprites = pygame.sprite.Group([player])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(BLACK)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()


if __name__ == "__main__":
    main()
