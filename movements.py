import pygame


def move_rectangle(screen, rect, keys, speed, dt):
    if keys[pygame.K_a]:
        pygame.Rect.move_ip(rect, -speed * dt, 0)
    if keys[pygame.K_d]:
        pygame.Rect.move_ip(rect, speed * dt, 0)
    if keys[pygame.K_w]:
        pygame.Rect.move_ip(rect, 0, -speed * dt)
    if keys[pygame.K_s]:
        pygame.Rect.move_ip(rect, 0, speed * dt)


def move_rectangle_with_bounds(screen, rect, image, keys, speed, dt):
    if keys[pygame.K_a] and not rect.left - (speed * dt) < 0:
        pygame.Rect.move_ip(rect, -speed * dt, 0)
    if (
        keys[pygame.K_d]
        and not rect.left + (speed * dt) > screen.get_width() - rect.width
    ):
        pygame.Rect.move_ip(rect, speed * dt, 0)
    if keys[pygame.K_w] and not rect.top - (speed * dt) < 0:
        pygame.Rect.move_ip(rect, 0, -speed * dt)
    if (
        keys[pygame.K_s]
        and not rect.top + (speed * dt) > screen.get_height() - rect.height
    ):
        pygame.Rect.move_ip(rect, 0, speed * dt)


def move_rectangle_with_direction(screen, rect, speed, dt, direction):
    if direction == "up":
        pygame.Rect.move_ip(rect, 0, -speed * dt)
    if direction == "down":
        pygame.Rect.move_ip(rect, 0, speed * dt)
    if direction == "left":
        pygame.Rect.move_ip(rect, -speed * dt, 0)
    if direction == "right":
        pygame.Rect.move_ip(rect, speed * dt, 0)


def move_rectangle_track_object(screen, rect, image, speed, dt, target):
    if target.rect.x < rect.x:
        move_rectangle_with_direction(screen, rect, speed, dt, "left")
    if target.rect.x > rect.x:
        move_rectangle_with_direction(screen, rect, speed, dt, "right")
    if target.rect.y < rect.y:
        move_rectangle_with_direction(screen, rect, speed, dt, "up")
    if target.rect.y > rect.y:
        move_rectangle_with_direction(screen, rect, speed, dt, "down")
