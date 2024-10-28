import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()
   dt = 0

   updateable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()

   Asteroid.containers = (asteroids, updateable, drawable)
   Player.containers = (updateable, drawable)
   AsteroidField.containers = (updateable)
   Shot.containers = (shots, updateable, drawable)

   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   asteroid_field = AsteroidField()

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

      pygame.Surface.fill(screen, pygame.Color('black'))

      for item in updateable:
         item.update(dt)

      for item in drawable:
         item.draw(screen)

      for item in asteroids:
         if item.collision(player):
            print("Game Over!")
            sys.exit()
         for bullet in shots:
            if item.collision(bullet):
               item.split()
               bullet.kill()


      pygame.display.flip()
      dt = clock.tick(60) / 1000
      

if __name__ == "__main__":
    main()
