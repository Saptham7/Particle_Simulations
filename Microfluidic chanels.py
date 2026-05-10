import pygame
import random

pygame.init()

WIDTH = 1200
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Microfluidic Channel Simulation")

clock = pygame.time.Clock()

BLACK = (10, 10, 15)
BLUE = (80, 180, 255)
PINK = (255, 120, 200)
WHITE = (240, 240, 240)
CHANNEL = (40, 40, 50)

CHANNEL_TOP = 200
CHANNEL_BOTTOM = 400
CHANNEL_HEIGHT = CHANNEL_BOTTOM - CHANNEL_TOP

particles = []

N_PARTICLES = 1200

for i in range(N_PARTICLES):

    y = random.uniform(CHANNEL_TOP, CHANNEL_BOTTOM)
    x = random.uniform(-200, 0)

    color = BLUE if i % 2 == 0 else PINK

    particles.append({
        "x": x,
        "y": y,
        "color": color
    })

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.draw.rect(
        screen,
        CHANNEL,
        (
            0,
            CHANNEL_TOP,
            WIDTH,
            CHANNEL_HEIGHT
        )
    )

    pygame.draw.line(
        screen,
        WHITE,
        (0, CHANNEL_TOP),
        (WIDTH, CHANNEL_TOP),
        3
    )

    pygame.draw.line(
        screen,
        WHITE,
        (0, CHANNEL_BOTTOM),
        (WIDTH, CHANNEL_BOTTOM),
        3
    )

    for p in particles:

        yc = (CHANNEL_TOP + CHANNEL_BOTTOM) / 2

        dy = p["y"] - yc

        R = CHANNEL_HEIGHT / 2

        vmax = 8

        vx = vmax * (1 - (dy / R) ** 2)

        diffusion = 0.3

        p["y"] += random.uniform(
            -diffusion,
            diffusion
        )

        p["x"] += vx

        if p["y"] < CHANNEL_TOP:
            p["y"] = CHANNEL_TOP

        if p["y"] > CHANNEL_BOTTOM:
            p["y"] = CHANNEL_BOTTOM

        if p["x"] > WIDTH + 20:

            p["x"] = random.uniform(-100, 0)

            p["y"] = random.uniform(
                CHANNEL_TOP,
                CHANNEL_BOTTOM
            )

        pygame.draw.circle(
            screen,
            p["color"],
            (int(p["x"]), int(p["y"])),
            2
        )

    pygame.display.flip()

pygame.quit()