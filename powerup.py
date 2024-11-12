import pygame
import random
from circleshape import *
from constants import *

class Powerup(CircleShape):
   def __init__(self, x, y, type):
      super().__init__(x, y, POWERUP_RADIUS)
      self.type = type
      self.duration = POWERUP_DURATION

   def draw(self, screen):
      if self.type == 'shield':
         pygame.draw.circle(screen, pygame.Color('green'), self.position, POWERUP_RADIUS, SHIELD_WIDTH)
      elif self.type == 'lazer':
         pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(self.position.x, self.position.y, LAZER_WIDTH * 2, LAZER_LENGTH * 2), 2)

   def update(self, dt):
      self.duration = self.duration - dt
      if self.duration <= 0.0:
         self.kill()
