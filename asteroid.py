import pygame
import random
from circleshape import *
from constants import *
from powerup import Powerup


class Asteroid(CircleShape):
   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)

   def draw(self, screen):
      pygame.draw.circle(screen, pygame.Color('white'), self.position, self.radius, 2)

   def update(self, dt):
      self.position += self.velocity * dt
      if self.position.x < -ASTEROID_MAX_RADIUS:
         self.position.x = SCREEN_WIDTH + ASTEROID_MAX_RADIUS
      if self.position.x > SCREEN_WIDTH + ASTEROID_MAX_RADIUS:
         self.position.x = -ASTEROID_MAX_RADIUS
      if self.position.y < -ASTEROID_MAX_RADIUS:
         self.position.y = SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
      if self.position.y > SCREEN_HEIGHT + ASTEROID_MAX_RADIUS:
         self.position.y = -ASTEROID_MAX_RADIUS

   def split(self):
      self.kill()
      randomNum = random.randint(0,99)
      if randomNum < 4:
         if randomNum % 2 == 0:
            shieldPowerup = Powerup(self.position.x, self.position.y, 'shield')
         else:
            lazerPowerup = Powerup(self.position.x, self.position.y, 'lazer')
   
      if self.radius <= ASTEROID_MIN_RADIUS:
         return
      randomAngle = random.uniform(20, 50)
      newVelocity1 = self.velocity.rotate(randomAngle)
      newVelocity2 = self.velocity.rotate(-randomAngle)
      newRadius = self.radius - ASTEROID_MIN_RADIUS

      asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
      asteroid1.velocity = newVelocity1 * 1.2
      asteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
      asteroid2.velocity = newVelocity2 * 1.2

