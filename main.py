import pygame
import sys
from Player import Player, Projectile


DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720
BLACK = (0, 0, 0)

def init_font():
    pygame.font.init()
    if not pygame.font.get_init():
        print('Font not initialized, closing')
        sys.exit()

def create_text_surface():
    font = pygame.font.Font(None, 200)
    return font.render('xddddddddddd', True, [100, 100, 100], [200, 200, 200])
    
def main():
    pygame.init()
    size = width, height = DEFAULT_WIDTH, DEFAULT_HEIGHT
    screen = pygame.display.set_mode(size)
    init_font()
    text_surface = create_text_surface()
    screen.blit(text_surface, (0, 0))
    player = Player()
    all_sprites = pygame.sprite.Group([player])
    pygame.font.Font(None, 200).render_to(screen, (100, 100), 'aooooooooo', (100, 100, 100))
    while True:
        screen.fill(BLACK)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()
