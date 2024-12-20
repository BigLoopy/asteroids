# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import *

def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    field = AsteroidField()
    
    Shot.containers = (shots, updatable,drawable)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        update(dt, updatable)

        if flew_into_asteroid(asteroids, player1):
            print("Game over!")
            return
        
        asteroid_shot(asteroids, shots)

        draw(screen, drawable)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def update(dt, updateables):
    for updateable in updateables:
        updateable.update(dt)
    pass

def draw(screen, drawables):
    for drawable in drawables:
        drawable.draw(screen)
    pass

def flew_into_asteroid(asteroids, player):
    for asteroid in asteroids:
        if asteroid.collision(player):
            return True
    return False

def asteroid_shot(asteroids, shots):
    for asteroid in asteroids:
        for bullet in shots:
            if bullet.collision(asteroid):
                asteroid.split()
                bullet.kill()

    
if __name__ == "__main__":
    main()
