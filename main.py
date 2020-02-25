import pygame
import sys

DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720

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
    pygame.font.Font(None, 200).render_to(screen, (100, 100), 'aooooooooo', (100, 100, 100))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()