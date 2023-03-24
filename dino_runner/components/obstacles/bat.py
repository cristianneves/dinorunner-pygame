
import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle 

class Bat(Obstacle):
    def __init__(self, images): 
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = random.randint(290,320)
        self.last_flap_time = 0
        self.moving = random.randint(1,2) % 2 == 0 and True or False
        self.touched_ground = False

    def draw(self, screen):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_flap_time > 250:  
            self.last_flap_time = current_time
            screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
            self.type += 1
            if self.type == 2:
                self.type = 0
        else:
            screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
    
    def update(self,game_speed, obstacles):
        if self.moving:
            if not self.touched_ground:
                self.rect.y +=7
                if self.rect.y > 400:
                    self.touched_ground = True
            else:
                self.rect.y -=7
                if self.rect.y < 290:
                    self.touched_ground = False
        
        super().update(game_speed, obstacles)
    
    
          


        