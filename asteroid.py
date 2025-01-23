from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        ran_angle = random.uniform(20, 50)

        first_vector = self.velocity.rotate(ran_angle)
        second_vector = self.velocity.rotate(-ran_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteriod = Asteroid(self.position.x, self.position.y, new_radius)
        asteriod.velocity = first_vector * 1.2
        asteriod = Asteroid(self.position.x, self.position.y, new_radius)
        asteriod.velocity = second_vector * 1.2 