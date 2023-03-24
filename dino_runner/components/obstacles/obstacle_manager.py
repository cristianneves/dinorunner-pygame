import pygame
import random
from dino_runner.components.obstacles.bat import Bat
from dino_runner.components.obstacles.meteor import Meteor
from dino_runner.components.obstacles.monster import Monster
from dino_runner.components.obstacles.cloud import *
from dino_runner.utils.constants import * 


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.clouds = []

    def lose_condition(self,game):
        HITSOUND.play()
        pygame.time.delay(500)
        game.lifes -=1
        self.reset_obstacles()
        if game.lifes == 0:
            game.playing = False
            DEATHSOUND.play()
            game.death_count += 1

    def update(self, game):

        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 4) 
            random_bird = random.randint(0, 2)

            if random_obstacle == 0:            
                self.obstacles.append(Monster(MINOTAUR,380))
                self.item = 1
            elif random_obstacle == 1:
                self.obstacles.append(Monster(PLANT,400))
                self.item = 1
            elif random_obstacle == 2:
                self.obstacles.append(Bat(BAT))
                self.item = 2
            elif random_obstacle == 3:
                self.obstacles.append(Meteor(METEOR))
                self.item = 2
            elif random_obstacle == 4:
                self.obstacles.append(Monster(SKELETON,400))
                self.item = 1
        
        if len(self.clouds) == 0:
            self.clouds.append(Cloud(CLOUD))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles) 

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    self.lose_condition(game)
                    break
                elif game.player.has_power_up:
                    if game.player.type == HAMMER_TYPE and self.item == 1: 
                        self.obstacles.remove(obstacle)
                    elif game.player.type == SHIELD_TYPE:
                        self.obstacles.remove(obstacle)
                    elif game.player.type == HAMMER_TYPE and self.item == 2:
                        self.lose_condition(game)
                        break

        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
        for cloud in self.clouds:
            cloud.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()