import pygame
import sys
from Player import Player
from Map import Map, Wall
from utils import *


def main():
    pygame.init()
    pygame.mixer.quit()
    size = WINDOW_WIDTH, WINDOW_HEIGHT
    screen = pygame.display.set_mode(size)

    player = Player()
    players_list = [player]
    all_players = pygame.sprite.Group(players_list)

    borders_points = Map().border
    walls_list = [Wall(border) for border in borders_points]
    borders = pygame.sprite.Group(walls_list)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(BLACK)

        borders.draw(screen)

        all_players.update()
        collision(players_list, walls_list)
        all_players.draw(screen)

        pygame.display.flip()


def collision(players_list, walls_list):
    for player in players_list:
        for wall in walls_list:
            if player.rect.colliderect(wall.rect):
                if player.rect.right > wall.rect.left and player.move_dir_x == 1:
                    player.rect.right = wall.rect.left
                if player.rect.left < wall.rect.right and player.move_dir_x == -1:
                    player.rect.left = wall.rect.right

                if player.rect.bottom > wall.rect.top and player.rect.top < wall.rect.top and player.move_dir_y == 1:
                    player.rect.bottom = wall.rect.top
                # if player.rect.top < wall.rect.bottom and player.move_dir_y == -1:
                #     player.rect.top = wall.rect.bottom


if __name__ == "__main__":
    main()
