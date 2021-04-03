import sys
import pygame
from Enemy import Enemy
from Player import Player

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
LEFT = (-1, 0)
RIGHT = (1, 0)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(screen)
    enemy = Enemy(screen)

    i = 3
    running = True
    while running:
        clock.tick(60)
        player.handle_keys()
        player.draw(screen)
        if i > 0:
            enemy.randomize_position()
            enemy.draw(screen)
            enemy.move()
            i -= 1

        if enemy.is_collided_with(player.collide_rect):
            print("colliding")

        pygame.display.flip()


main()
