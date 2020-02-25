import pygame


class Player(pygame.sprite.Sprite):
    WIDTH = 40
    HEIGTH = 40
    WHITE = (255, 255, 255)
    MOVE_SPEED = 2

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.surface.Surface((self.WIDTH, self.HEIGTH))
        self.image.fill(self.WHITE)
        self.rect = pygame.rect.Rect(0, 0, self.WIDTH, self.HEIGTH)

        self.hp = 100
        self.weapons = list()
        self.move_dir_x = 0
        self.move_dir_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.move_dir_x = keys[pygame.K_d] - keys[pygame.K_a]
        self.move_dir_y = keys[pygame.K_s] - keys[pygame.K_w]
        self.move()

    def move(self):
        self.rect.x += self.MOVE_SPEED * self.move_dir_x
        self.rect.y += self.MOVE_SPEED * self.move_dir_y
