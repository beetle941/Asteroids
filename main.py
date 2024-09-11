import sys
import pygame
from constants import *
from player import Player
from asteriud import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over!")
                sys.exit()
        for obj in asteroids:
            for shot in shots:
                if shot.check_collision(obj):
                    shot.kill()
                    obj.kill()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        #framerate 60
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()