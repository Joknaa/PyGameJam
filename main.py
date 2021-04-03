import sys

import pygame


class Player:
    def __init__(self, screen):
        self.player_sprite = pygame.Rect(0, 0, 20, 20)
        self.player_sprite.midbottom = screen.get_rect().midbottom
        self.speed = 10

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.player_sprite)

    def get_position(self):
        pass

    def move(self, keys):
        self.player_sprite.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed

    def turn(self, point):
        pass

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        self.move(keys)

    def reset(self):
        pass


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

LEFT = (-1, 0)
RIGHT = (1, 0)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(screen)

    running = True
    while running:
        clock.tick(60)
        player.handle_keys()
        player.draw(screen)

        pygame.display.flip()
        screen.fill(0)


main()
