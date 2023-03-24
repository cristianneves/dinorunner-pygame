from dino_runner.components.obstacles.objectCloud import *

class Cloud(CloudComportament):
    def __init__(self, images):
        super().__init__(images)
        
        self.rect.y = 90