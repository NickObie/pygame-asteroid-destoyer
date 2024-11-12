import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
   def __init__(self, x, y, boolLazer, rotation):
      super().__init__(x, y, SHOT_RADIUS)
      self.isLazer = boolLazer
      self.rotation = rotation

   def draw(self, screen):
      if self.isLazer == False:
         pygame.draw.circle(screen, pygame.Color('white'), self.position, self.radius, 2)
      else: 
         pygame.draw.polygon(screen, pygame.Color('white'), self.lazer(), 6)

   def update(self, dt): 
      self.position += self.velocity * dt
   
   def lazer(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0,1).rotate(self.rotation + 90) * LAZER_WIDTH
      a = self.position + forward * LAZER_LENGTH + right
      b = self.position + forward * LAZER_LENGTH - right
      c = self.position - forward * LAZER_LENGTH - right
      d = self.position - forward * LAZER_LENGTH + right
      return [a, b, c, d]