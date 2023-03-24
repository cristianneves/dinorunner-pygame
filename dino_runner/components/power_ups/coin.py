from dino_runner.utils.constants import *
from dino_runner.components.obstacles.obstacle import *
import random


class Coin(Obstacle):
    def __init__(self, images): 
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = random.randint(290,320)
        self.last_rotate = 0

    def draw(self, screen):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_rotate > 50:  
            self.last_rotate = current_time
            screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
            self.type += 1
            if self.type == 5:
                self.type = 0
        else:
            screen.blit(self.images[self.type], (self.rect.x, self.rect.y))