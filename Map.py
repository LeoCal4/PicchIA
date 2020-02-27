import pygame
from utils import *


class Map:
    def __init__(self):
        self.border = [
            pygame.Rect(0, 0, WINDOW_WIDTH, 5),
            pygame.Rect(WINDOW_WIDTH-5, 0, 5, WINDOW_HEIGHT),
            pygame.Rect(0, 0, 5, WINDOW_HEIGHT),
            pygame.Rect(0, WINDOW_HEIGHT-5, WINDOW_WIDTH, 5),

            pygame.Rect(500, 500, 100, 100)
        ]


class Wall(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface(rect.size)
        self.image.fill(WHITE)
        self.rect = rect
