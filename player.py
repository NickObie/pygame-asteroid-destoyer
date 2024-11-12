import pygame
from circleshape import *
from constants import *
from shot import Shot


class Player(CircleShape):
   def __init__(self, x, y):
      super().__init__(x, y, PLAYER_RADIUS)
      self.rotation = 0
      self.shoot_cooldown = 0
      self.shield_active = False
      self.shield_duration = 0.0
      self.lazer_active = False
      self.lazer_duration = 0.0

   def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c] 
   
   def draw(self, screen):
     pygame.draw.polygon(screen, pygame.Color('white'), self.triangle(), 2)
     if self.shield_active == True:
        pygame.draw.circle(screen, pygame.Color('green'), self.position, PLAYER_RADIUS + 5, 2)

   def rotate(self, dt):
     self.rotation += PLAYER_TURN_SPEED * dt

   def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt
   
   def shoot(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      
      if self.shoot_cooldown <= 0 and self.lazer_active == True:
         new_beam = Shot(self.position.x, self.position.y, True, self.rotation)
         new_beam.velocity = forward * PLAYER_SHOOT_SPEED
         self.shoot_cooldown = LAZER_SHOOT_COOLDOWN

      if self.shoot_cooldown <= 0 and self.lazer_active == False:
         new_shot = Shot(self.position.x, self.position.y, False, self.rotation)
         new_shot.velocity = forward * PLAYER_SHOOT_SPEED
         self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

   def update(self, dt):
         self.shoot_cooldown = self.shoot_cooldown - dt
         if self.shield_duration > 0.0 and self.shield_active == True:
            self.shield_duration = self.shield_duration - dt
            if self.shield_duration <= 0.0:
               self.shield_active = False

         elif self.lazer_duration > 0.0 and self.lazer_active == True:
            self.lazer_duration = self.lazer_duration - dt
            if self.lazer_duration <= 0.0:
               self.lazer_active = False


         keys = pygame.key.get_pressed()

         if keys[pygame.K_a]:
            self.rotate(-dt)
         if keys[pygame.K_d]:
            self.rotate(dt)
         if keys[pygame.K_w]:
            self.move(dt)
         if keys[pygame.K_s]:
            self.move(-dt)
         if keys[pygame.K_SPACE]:
            self.shoot(dt)