import random
from os import path
import pygame
import movements
from entities import Player, Enemy

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


def generate_x_coordinate():
    return random.randint(0, screen.get_width())


def generate_y_coordinate():
    return random.randint(0, screen.get_height())


player = Player(generate_x_coordinate(), generate_y_coordinate())

enemies = []
for e in range(3):
    enemies.append(Enemy(generate_x_coordinate(), generate_y_coordinate()))

pygame.mixer.music.load("main_background_loop.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    screen.blit(player.image, player.rect)
    for e in enemies:
        screen.blit(e.image, e.rect)

    keys = pygame.key.get_pressed()
    player.update(screen, keys, dt)
    for e in enemies:
        e.update(screen, dt, player)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
