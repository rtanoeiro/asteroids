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
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    delta = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for updatable_object in updatable:
            updatable_object.update(delta)

        for asteroid in asteroids:
            if player.check_colision(asteroid):
                print("Player died!")
                return 1

            for shot in shots:
                if shot.check_colision(asteroid):
                    asteroid.split()
                    shot.kill()

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

        delta = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
