import pygame
from math import atan2, sqrt, pi
PROJ_SPEED = 3
SHOOT_RATE = 30
WHITE = (255, 255, 255)


class Projectile:
    def __init__(self):
        self.image = pygame.surface.Surface((10, 10))
        pygame.draw.circle(self.image, (255, 255, 255), (5, 5), 5)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    WIDTH = 40
    HEIGTH = 40
    MOVE_SPEED = 2

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.surface.Surface((self.WIDTH, self.HEIGTH))
        self.image = pygame.image.load('pg.png')
        self.original_image = self.image
        self.rect = self.image.get_rect()

        self.hp = 100
        self.weapons = list()
        self.move_dir_x = 0
        self.move_dir_y = 0

        self.i = 0
        self.enable = True

        self.projectiles = []

    def update(self):
        keys = pygame.key.get_pressed()
        self.move_dir_x = keys[pygame.K_d] - keys[pygame.K_a]
        self.move_dir_y = keys[pygame.K_s] - keys[pygame.K_w]
        self.move()
        self.rotate()
        if keys[pygame.K_SPACE] and self.enable:
            print('shoot')
            self.shoot()
            self.enable = False
        self.i += 1
        if self.i % SHOOT_RATE == 0:
            self.enable = True

        screen = pygame.display.get_surface()
        for proj in self.projectiles:
            screen.blit(proj.image, (proj.rect.x, proj.rect.y))

            proj.rect.x += PROJ_SPEED

            if not screen.get_rect().colliderect(proj.rect):
                self.projectiles.remove(proj)

    def move(self):
        self.rect.x += self.MOVE_SPEED * self.move_dir_x
        self.rect.y += self.MOVE_SPEED * self.move_dir_y

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
        shooting_angle = (180 / pi) * -atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(shooting_angle))
        self.rect = self.image.get_rect(center=self.rect.center)

    def shoot(self):
        proj = Projectile()
        proj.rect.right = self.rect.right
        proj.rect.centery = self.rect.centery
        self.projectiles.append(proj)
