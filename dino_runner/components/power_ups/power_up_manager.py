import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.extra_life import Heart
from dino_runner.components.power_ups.coin import Coin
from dino_runner.components.game import *


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.extra_life = []
        self.when_appears = 100
        self.heart_appears = 200
    
    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(300,500)

            randomic_choice = random.randint(0,1)

            if randomic_choice == 0:
                self.power_ups.append(Shield())
            elif randomic_choice == 1:
                self.power_ups.append(Hammer())

        if len(self.extra_life) == 0 and self.heart_appears == score:
            self.heart_appears += random.randint(300,500)

            randomic_choice2 = random.randint(0,1)

            if randomic_choice2 == 0:
                self.extra_life.append(Heart())
                self.item = 1
            elif randomic_choice2 == 1:
                self.extra_life.append(Coin(COIN))
                self.item = 2

    def update(self, game):
        self.generate_power_up(game.score)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            player = game.player
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.has_power_up = True
                player.type = power_up.type 
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

        for heart in self.extra_life:
            heart.update(game.game_speed, self.extra_life)

            player = game.player
            if player.dino_rect.colliderect(heart.rect) and self.item == 1:
                self.extra_life.remove(heart)
                game.lifes +=1
            elif player.dino_rect.colliderect(heart.rect) and self.item == 2:
                self.extra_life.remove(heart)
                game.score += 100
        
        if game.playing == False:
            self.when_appears = 0
            self.heart_appears = 100
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        
        for heart in self.extra_life:
            heart.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups.clear()   
    def reset_spawn(self):
        self.when_appears = 0
        self.heart_appears = 0