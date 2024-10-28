import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)

   def draw(self, screen):
      pygame.draw.circle(screen, pygame.Color('white'), self.position, self.radius, 2)

   def update(self, dt):
      self.position += self.velocity * dt
   
   def split(self):
      self.kill()
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

