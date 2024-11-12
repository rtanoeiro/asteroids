import pygame
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_SPAWN_RATE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from player import Player


def main():
    pygame.init()
    delta = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x=x, y=y)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        player.update(delta)
        pygame.display.flip()

        delta = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
