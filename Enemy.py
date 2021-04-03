import random
import pygame


class Enemy:
    def __init__(self, screen):
        self.position = (0, 0)
        self.sprite = 0
        self.collide_rect = 0
        self.speed = 5

    def draw(self, screen):
        screen.fill(0)
        self.sprite = pygame.Rect(self.position[0], self.position[1], 10, 10)
        pygame.draw.rect(screen, (255, 0, 0), self.sprite)
        self.collide_rect = self.sprite

    def get_position(self):
        pass

    def randomize_position(self):
        self.position = (random.randint(0,  600), random.randint(0, 100))

    def move(self):
        self.sprite.x -= self.speed

    def is_collided_with(self, player_collide_rect):
        return self.collide_rect.colliderect(player_collide_rect)
