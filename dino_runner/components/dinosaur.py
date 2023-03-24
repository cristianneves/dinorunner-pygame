import pygame

from dino_runner.utils.constants import *
from dino_runner.components.power_ups.shield import *

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE:DUCKING_SHIELD, HAMMER_TYPE:DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE:JUMPING_SHIELD, HAMMER_TYPE:JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE:RUNNING_HAMMER}

X_POS = 80
Y_POS = 400
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.has_power_up = False

    def run(self):
        self.image = RUN_IMG[self.type][0] if self.step_index < 5 else RUN_IMG[self.type][1] 
        self.dino_rect.y = Y_POS
        self.step_index+=1        
       
    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*5
            self.jump_vel -=1
        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
    
    def duck(self):
        self.image = DUCK_IMG[self.type][0] if self.step_index < 5 else DUCK_IMG[self.type][1]
        self.dino_rect.y = Y_POS + 35
        self.step_index+=1
        self.dino_duck = False
        
    def update(self, user_input):

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        if user_input[pygame.K_DOWN] and not self.dino_jump: 
            self.dino_duck = True
            self.dino_run = False
        if user_input[pygame.K_DOWN] and self.dino_jump:
            self.jump_vel -= 1.7
        elif not self.dino_duck and not self.dino_jump:
            self.dino_run = True
        if user_input[pygame.K_RIGHT]:
            self.dino_rect.x +=10
            if self.dino_rect.x > 1000:
                self.dino_rect.x = 1000  
        elif user_input[pygame.K_LEFT]:
            self.dino_rect.x -=10
            if self.dino_rect.x < 1:
                self.dino_rect.x = 1

        if self.dino_run:
            self.run()
        elif self.dino_duck:
            self.duck()  
        elif self.dino_jump:
            self.jump()      

        if self.step_index >= 10: 
            self.step_index = 0    
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))
    