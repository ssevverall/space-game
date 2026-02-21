import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
radius = 10
speed = 300

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    pygame.draw.circle(screen, "red", player_pos, radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and not (player_pos.y - (speed * dt)) < radius:
        player_pos.y -= speed * dt
    if keys[pygame.K_s] and not (player_pos.y + (speed * dt)) > (
        screen.get_height() - radius
    ):
        player_pos.y += speed * dt
    if keys[pygame.K_a] and not (player_pos.x - (speed * dt)) < radius:
        player_pos.x -= speed * dt
    if keys[pygame.K_d] and not (player_pos.x + (speed * dt)) > (
        screen.get_width() - radius
    ):
        player_pos.x += speed * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
