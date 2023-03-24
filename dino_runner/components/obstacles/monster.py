import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle 

class Monster(Obstacle):
    def __init__(self, images,y): 
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = y
        self.last_walk = 0

    def draw(self, screen):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_walk > 100:  
            self.last_walk = current_time
            screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
            self.type += 1
            if self.type == 3:
                self.type = 0
        else:
            screen.blit(self.images[self.type], (self.rect.x, self.rect.y))