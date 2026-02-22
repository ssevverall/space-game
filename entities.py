from movements import move_rectangle_with_bounds, move_rectangle_track_object
import pygame
from os import path
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(
            path.join("assets", "ship_2.png")
        ).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 300

    def update(self, screen, keys, dt):
        move_rectangle_with_bounds(screen, self.rect, self.image, keys, self.speed, dt)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(path.join("assets", "ship_1.png"))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(150, 250)

    def update(self, screen, dt, target):
        move_rectangle_track_object(
            screen, self.rect, self.image, self.speed, dt, target
        )
