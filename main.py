import pygame
import sys
from Player import Player, Projectile

DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720
BLACK = (0, 0, 0)
    
def main():
    pygame.init()
    size = width, height = DEFAULT_WIDTH, DEFAULT_HEIGHT
    screen = pygame.display.set_mode(size)
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
