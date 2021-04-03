import sys

import pygame


class Player:
    def __init__(self, screen):
        self.sprite = pygame.Rect(0, 0, 20, 20)
        self.sprite.midbottom = screen.get_rect().midbottom
        self.collide_rect = self.sprite
        self.speed = 10

    def draw(self, screen):
        screen.fill(0)
        pygame.draw.rect(screen, (255, 255, 255), self.sprite)

    def get_position(self):
        pass

    def move(self, keys):
        self.sprite.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        self.move(keys)

    def reset(self):
        pass
