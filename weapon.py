import pygame

class _Weapon:
    def __init__(self, shoot_delay, projectile_speed, damage, player):
        self.shoot_delay = shoot_delay
        self.projectile_speed = projectile_speed
        self.damage = damage
        self.player = player
    
    def shoot(self):
        proj = Projectile(self.player.rect.center, self)
        proj.rect.right = self.player.rect.right
        proj.rect.centery = self.player.rect.centery
        proj.add(self.player.all_projectiles)

class Shotgun(_Weapon):
    def __init__(self, player):
        _Weapon.__init__(self, 100, 5, 20, player)


class Sniper_Rifle(_Weapon):
    def __init__(self, player):
        super.__init__(self, 50, 10, 40, player)


class Assault_Rifle(_Weapon):
    def __init__(self, player):
        super.__init__(self, 5, 15, 10, player)


class Projectile(pygame.sprite.Sprite):
    PROJECTILE_COLOR = (255, 255, 255)
    RADIUS = 5
    CENTER = (RADIUS, RADIUS)
    SURFACE_SIZE = (RADIUS*2, RADIUS*2)

    def __init__(self, position, weapon):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface(self.SURFACE_SIZE)
        pygame.draw.circle(self.image, self.PROJECTILE_COLOR, self.CENTER, self.RADIUS)
        self.rect = self.image.get_rect(center = position)
        self.speed = weapon.projectile_speed
        self.screen = pygame.display.get_surface()

    def update(self):
        self.rect.x += self.speed
        if not self.screen.get_rect().colliderect(self.rect):
            self.kill()