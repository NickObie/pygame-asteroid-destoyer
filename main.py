import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import Powerup


def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()
   dt = 0
   score_text = "0"
   score = 0

   text_font = pygame.font.SysFont(None, 30)

   updateable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()
   powerups = pygame.sprite.Group()
   

   Asteroid.containers = (asteroids, updateable, drawable)
   Player.containers = (updateable, drawable)
   AsteroidField.containers = (updateable)
   Shot.containers = (shots, updateable, drawable)
   Powerup.containers = (powerups, drawable, updateable)

   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   asteroid_field = AsteroidField()

   def draw_text(text, font, text_color, x, y):
      img = font.render(text, True, text_color)
      screen.blit(img, (x, y))

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

      pygame.Surface.fill(screen, pygame.Color('black'))
      draw_text(score_text, text_font, pygame.Color('white'), 20, 20)

      for item in updateable:
         item.update(dt)

      for item in drawable:
         item.draw(screen)

      for item in powerups:
         if item.collision(player):
            if item.type == 'shield':
               player.shield_active = True
               player.shield_duration = POWERUP_DURATION
            elif item.type == 'lazer':
               player.lazer_active = True
               player.lazer_duration = POWERUP_DURATION
            item.kill()

      for item in asteroids:
         if item.collision(player):
            if player.shield_active == True:
               player.shield_active = False
               item.kill()
            else:
               print("Game Over!")
               print(f"You ended with a score of: {score}")
               sys.exit()
         for bullet in shots:
            if item.collision(bullet):
               item.split()
               bullet.kill()
               score += 1
               score_text = str(score)


      pygame.display.flip()
      dt = clock.tick(60) / 1000
      

if __name__ == "__main__":
    main()
