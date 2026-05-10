import pygame
import random
import math

pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laminar Microfluidic Flow")

clock = pygame.time.Clock()

BLACK = (10, 10, 15)
BLUE = (80, 180, 255)
PINK = (255, 120, 200)
WHITE = (240, 240, 240)
CHANNEL = (40, 40, 50)

N_PARTICLES = 1400

CHANNEL_WIDTH = 120

particles = []

for i in range(N_PARTICLES):

    x = random.uniform(-200, WIDTH)

    center_y = HEIGHT / 2 + 120 * math.sin(x * 0.008)

    y = random.uniform(
        center_y - CHANNEL_WIDTH / 2,
        center_y + CHANNEL_WIDTH / 2
    )

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

    upper_points = []
    lower_points = []

    for x in range(0, WIDTH, 5):

        center_y = HEIGHT / 2 + 120 * math.sin(x * 0.008)

        upper_points.append((
            x,
            center_y - CHANNEL_WIDTH / 2
        ))

        lower_points.append((
            x,
            center_y + CHANNEL_WIDTH / 2
        ))

    polygon_points = upper_points + lower_points[::-1]

    pygame.draw.polygon(
        screen,
        CHANNEL,
        polygon_points
    )

    pygame.draw.lines(
        screen,
        WHITE,
        False,
        upper_points,
        3
    )

    pygame.draw.lines(
        screen,
        WHITE,
        False,
        lower_points,
        3
    )

    for p in particles:

        center_y = HEIGHT / 2 + 120 * math.sin(
            p["x"] * 0.008
        )

        dy = p["y"] - center_y

        R = CHANNEL_WIDTH / 2

        vmax = 4

        vx = vmax * (1 - (dy / R) ** 2)

        slope = 120 * 0.008 * math.cos(
            p["x"] * 0.008
        )

        vy_flow = vx * slope

        p["x"] += vx
        p["y"] += vy_flow

        if abs(dy) > R:

            if dy > 0:
                p["y"] = center_y + R

            else:
                p["y"] = center_y - R

        if p["x"] > WIDTH + 50:

            p["x"] = random.uniform(-200, -20)

            center_y = HEIGHT / 2 + 120 * math.sin(
                p["x"] * 0.008
            )

            p["y"] = random.uniform(
                center_y - R,
                center_y + R
            )

        pygame.draw.circle(
            screen,
            p["color"],
            (int(p["x"]), int(p["y"])),
            2
        )

    pygame.display.flip()

pygame.quit()