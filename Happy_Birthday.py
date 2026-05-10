import pygame
import numpy as np
import random

pygame.init()

WIDTH = 1400
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Srivathsa, You is Gay")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
MEGIC = (180,0,255)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 120)

text_surface = font.render(
    "Srivathsa, You is Gay",
    False,
    WHITE )

text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

targets = []

STEP = 6

for x in range(0, text_surface.get_width(), STEP):

    for y in range(0, text_surface.get_height(), STEP):

        color = text_surface.get_at((x, y))

        if color[0] > 200:

            targets.append((
                x + text_rect.x,
                y + text_rect.y
            ))


targets = random.sample(
    targets,
    min(2500, len(targets))
)

particles = []

for tx, ty in targets:

    particle = {

        "x": random.uniform(0, WIDTH),
        "y": random.uniform(0, HEIGHT),

        "vx": random.uniform(-2, 2),
        "vy": random.uniform(-2, 2),

        "tx": tx,
        "ty": ty
    }

    particles.append(particle)

running = True

frame = 0

while running:

    clock.tick(60)

    screen.fill(BLACK)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    for _ in range(80):

        sx = random.randint(0, WIDTH)
        sy = random.randint(0, HEIGHT)

        pygame.draw.circle(
            screen,
            WHITE,
            (sx, sy),
            1 )

    for p in particles:

        if frame > 60:

            dx = p["tx"] - p["x"]
            dy = p["ty"] - p["y"]


            p["vx"] += dx * 0.002
            p["vy"] += dy * 0.002


        p["vx"] *= 0.92
        p["vy"] *= 0.92

        p["x"] += p["vx"]
        p["y"] += p["vy"]

        pygame.draw.circle(
            screen,
            MEGIC,
            (int(p["x"]), int(p["y"])),
            2 )

    pygame.display.flip()

    frame += 1

pygame.quit()

