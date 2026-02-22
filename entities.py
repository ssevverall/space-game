import random
from os import path

from pygame import image, sprite
from pygame.transform import rotate, scale

from movements import move_rectangle_track_object, move_rectangle_with_bounds


class Player(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = scale(
            image.load(path.join("assets", "player_starship.png")).convert_alpha(),
            (96, 96),
        )
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 300

    def update(self, screen, keys, dt):
        move_rectangle_with_bounds(screen, self.rect, self.image, keys, self.speed, dt)


class Enemy(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = rotate(
            scale(image.load(path.join("assets", "enemy_starship.png")), (64, 64)), 180
        )
        self.initial_image = scale(
            image.load(path.join("assets", "enemy_starship.png")), (64, 64)
        )
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(150, 250)
        self.direction = "down"

    def update(self, screen, dt, target):
        direction = move_rectangle_track_object(screen, self, self.speed, dt, target)
        if direction == "up" and self.direction != "up":
            self.image = self.initial_image
        if direction == "down" and self.direction != "down":
            self.image = rotate(self.image, 180)
        # if direction == "left" and self.direction != "left":
        #     self.image = rotate(self.initial_image, 90)
        # if direction == "right" and self.direction != "right":
        #     self.image = rotate(self.initial_image, -90)
