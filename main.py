import pygame
import sys
from Player import Player
from Map import Map, Wall
from utils import *


def main():
    pygame.init()
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

        for player in players_list:
            for wall in walls_list:
                if player.rect.colliderect(wall.rect):
                    if player.rect.left < wall.rect.right:
                        if abs(player.rect.top-wall.rect.top) > abs(wall.rect.right-player.rect.left):
                            player.rect.left = wall.rect.right

                    elif player.rect.bottom > wall.rect.top:
                        # if abs(wall.rect.right-player.rect.left) > abs(player.rect.top-wall.rect.top):
                        player.rect.bottom = wall.rect.top

        all_players.draw(screen)

        pygame.display.flip()


def collision(players_list, walls_list):
    for player in players_list:
        for wall in walls_list:
            if player.rect.colliderect(wall.rect):
                if player.rect.right > wall.rect.left:
                    player.rect.right = wall.rect.left
                    print(player.rect)
                elif player.rect.left < wall.rect.right:
                    player.rect.left = wall.rect.right
                    print(player.rect)
                elif player.rect.bottom > wall.rect.top:
                    player.rect.bottom = wall.rect.top
                elif player.rect.top < wall.rect.bottom:
                    player.rect.top = wall.rect.bottom
    print('culi')


if __name__ == "__main__":
    main()
