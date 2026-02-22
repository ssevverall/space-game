import random
import pygame
import movements

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 300
player = pygame.Rect(player_pos.x, player_pos.y, 10, 10)

enemy_speed = 200


def generate_x_coordinate():
    return random.randint(0, screen.get_width())


def generate_y_coordinate():
    return random.randint(0, screen.get_height())


spawn = pygame.Vector2(generate_x_coordinate(), 0)
enemy = pygame.Rect(spawn.x, spawn.y, 10, 10)

pygame.mixer.music.load("main_background_loop.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.rect(screen, "blue", player)
    pygame.draw.rect(screen, "red", enemy)

    keys = pygame.key.get_pressed()
    movements.move_rectangle_with_bounds(screen, player, keys, player_speed, dt)
    movements.move_rectangle_track_object(screen, enemy, enemy_speed, dt, player)

    if pygame.Rect.colliderect(player, enemy):
        screen.fill("red")
        running = False

    if enemy.y > screen.get_height():
        enemy.x, enemy.y = generate_x_coordinate(), 0

    pygame.display.flip()

    dt = clock.tick(60) / 1000
