import pygame
from math import sqrt, sin, cos, degrees
import random 

class _Weapon:
    def __init__(self, shoot_delay, projectile_speed, damage, player):
        self.shoot_delay = shoot_delay
        self.projectile_speed = projectile_speed
        self.damage = damage
        self.player = player

    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        direction_vector = pygame.math.Vector2(self._normalize_vector([mouse_x - self.player.rect.x, mouse_y - self.player.rect.y]))
        proj = Projectile(self.player.rect.center, direction_vector, self)
        proj.add(self.player.all_projectiles)

    def _normalize_vector(self, vector):
        norm = sqrt(sum(element * element for element in vector))
        return [element / norm for element in vector]

class Shotgun(_Weapon):
    NUM_OF_SHOTS = 6
    SPREAD = .2
    def __init__(self, player):
        super().__init__(250, 5, 20, player)

    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        base_direction_vector = pygame.math.Vector2(self._normalize_vector([mouse_x - self.player.rect.x, mouse_y - self.player.rect.y]))
        for i in range(self.NUM_OF_SHOTS):
            randomized_direction_vector = base_direction_vector + pygame.math.Vector2([random.uniform(-self.SPREAD, self.SPREAD), random.uniform(-self.SPREAD, self.SPREAD)])
            proj = Projectile(self.player.rect.center, randomized_direction_vector, self)
            proj.add(self.player.all_projectiles)

class Sniper_Rifle(_Weapon):
    def __init__(self, player):
        super().__init__(300, 10, 40, player)


class Assault_Rifle(_Weapon):
    SPREAD = .05
    def __init__(self, player):
        super().__init__(40, 15, 10, player)

    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        direction_vector = pygame.math.Vector2(self._normalize_vector([mouse_x - self.player.rect.x, mouse_y - self.player.rect.y]))
        randomized_direction_vector = direction_vector + pygame.math.Vector2([random.uniform(-self.SPREAD, self.SPREAD), random.uniform(-self.SPREAD, self.SPREAD)])
        proj = Projectile(self.player.rect.center, randomized_direction_vector, self)
        proj.add(self.player.all_projectiles)

class Projectile(pygame.sprite.Sprite):
    PROJECTILE_COLOR = (255, 255, 255)
    RADIUS = 5
    CENTER = (RADIUS, RADIUS)
    SURFACE_SIZE = (RADIUS*2, RADIUS*2)

    def __init__(self, position, direction_vector, weapon):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface(self.SURFACE_SIZE)
        pygame.draw.circle(self.image, self.PROJECTILE_COLOR, self.CENTER, self.RADIUS)
        self.rect = self.image.get_rect(center = position)
        self.position = pygame.math.Vector2(position)
        self.speed = weapon.projectile_speed
        self.direction = direction_vector
        self.screen = pygame.display.get_surface()

    def update(self):
        self.position += self.speed * self.direction
        self.rect.center = self.position
        if not self.screen.get_rect().colliderect(self.rect):
            self.kill()
    
    