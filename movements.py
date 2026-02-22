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


def move_rectangle_track_object(screen, entity, speed, dt, target):
    if target.rect.x < entity.rect.x:
        move_rectangle_with_direction(screen, entity.rect, speed, dt, "left")
        return "left"
    if target.rect.x > entity.rect.x:
        move_rectangle_with_direction(screen, entity.rect, speed, dt, "right")
        return "right"
    if target.rect.y < entity.rect.y:
        move_rectangle_with_direction(screen, entity.rect, speed, dt, "up")
        return "up"
    if target.rect.y > entity.rect.y:
        move_rectangle_with_direction(screen, entity.rect, speed, dt, "down")
        return "down"


# What this should do:
# - Receive a start point a(x, y) and end point b(x, y) which will be the period,
# a frequency, amplitude, wavelenght and speed
# - Calculate all the points and store them in a list of tuples
# - Return the list
def trace_sine_wave_route():
    pass


# What this should do:
# - Receive a list of (x, y) coordinates
# - Create successive lines from list[i](x, y) to list[i+1](x, y)
def draw_route():
    pass
