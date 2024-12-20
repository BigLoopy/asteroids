# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import player
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

    player.Player.containers = (updatable, drawable)
    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        update(dt, updatable)
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


if __name__ == "__main__":
    main()
