import pygame
import sys
from Player import Player
from Map import Map, Wall
from utils import *

def main():
    pygame.init()
    size = WINDOW_WIDTH, WINDOW_HEIGHT
    screen = pygame.display.set_mode(size)

    borders_points = Map().border
    walls_list = [Wall(border) for border in borders_points]
    borders = pygame.sprite.Group(walls_list)

    player = Player(walls_list)
    players_list = [player]
    all_players = pygame.sprite.Group(players_list)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(BLACK)
        borders.draw(screen)
        all_players.update()
        all_players.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
