import pygame
import weapon
from math import atan2, sqrt, pi, degrees
from utils import *

class Player(pygame.sprite.Sprite):
    WIDTH = 40
    HEIGTH = 40
    MOVE_SPEED = 2

    def __init__(self, walls):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((self.WIDTH, self.HEIGTH))
        # self.image = pygame.image.load('pg.png')
        # self.image = pygame.image.load('sprite_piccolissima.png')
        # self.image = pygame.image.load('sprite_media.png')
        self.image.fill(WHITE)
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.walls = walls
        self.hp = 100
        self.weapons = [weapon.Shotgun(self), weapon.Assault_Rifle(
            self), weapon.Sniper_Rifle(self)]
        self.current_weapon = self.weapons[0]

        self.move_dir_x = 0
        self.move_dir_y = 0

        self.delta_time_shooting = 0
        self.enable_shooting = True
        self.all_projectiles = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        self.move_dir_x = keys[pygame.K_d] - keys[pygame.K_a]
        self.move_dir_y = keys[pygame.K_s] - keys[pygame.K_w]
        self.move()
        #self.rotate()
        self.handle_weapon_change(keys)
        if keys[pygame.K_SPACE] and self.enable_shooting:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.current_weapon.shoot()
            self.enable_shooting = False
        if not self.enable_shooting:
            self.delta_time_shooting += 1
        if self.delta_time_shooting % self.current_weapon.shoot_delay == 0:
            self.enable_shooting = True
            self.delta_time_shooting = 0

        self.all_projectiles.update()
        self.all_projectiles.draw(pygame.display.get_surface())

    def move(self):
        self.rect.x += self.MOVE_SPEED * self.move_dir_x
        self.handle_x_collisions()
        self.rect.y += self.MOVE_SPEED * self.move_dir_y
        self.handle_y_collisions()

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
        shooting_angle = degrees(-atan2(rel_y, rel_x))
        self.image = pygame.transform.rotate(
            self.original_image, int(shooting_angle))
        self.rect = self.image.get_rect(center=self.rect.center)

    def dot(self, x, y):
        return sum(x_i*y_i for x_i, y_i in zip(x, y))

    def norm(self, vector):
        square_sum = 0
        for el in vector:
            square_sum += el**2
        return sqrt(square_sum)

    def handle_weapon_change(self, keys):
        weapons_dict = {pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2}
        for key in weapons_dict:
            if keys[key]:
                self.current_weapon = self.weapons[weapons_dict[key]]

    def handle_x_collisions(self):
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                if self.rect.right > wall.rect.left and self.move_dir_x == 1:
                    self.rect.right = wall.rect.left
                elif self.rect.left < wall.rect.right and self.move_dir_x == -1:
                    self.rect.left = wall.rect.right

    def handle_y_collisions(self):
            for wall in self.walls:
                if self.rect.colliderect(wall.rect):
                    if self.rect.bottom > wall.rect.top and self.move_dir_y == 1:
                        self.rect.bottom = wall.rect.top
                    elif self.rect.top < wall.rect.bottom and self.move_dir_y == -1:
                        self.rect.top = wall.rect.bottom