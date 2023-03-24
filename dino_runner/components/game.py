import pygame
import time
from dino_runner.utils.constants import *
from dino_runner.utils.constants import BG,ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import *
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups.power_up import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.lifes = 3
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.death_count = 0
        self.score = 0
        self.font = pygame.font.Font(FONT_STYLE, 25)
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        SOUNDTRACK.play(-1)
        self.playing = True
        if self.death_count == 0:
            self.reset_game()
        else:
            self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        SOUNDTRACK.stop()


    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score(1)
        
    def update_score(self, points):
        self.score += points
        if self.score %100 == 0:
            self.game_speed += 2
            if self.score > 1500:
                self.game_speed +=0

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))

        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        self.draw_level()
        self.draw_deaths()
        self.draw_lifes()

        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            
            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 22)
                self.method_draw_score_deaths(f"Power Up: {time_to_show}",550,100,(255,0,0))
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def method_draw_score_deaths(self,texto,x,y,rgb):
        text = self.font.render(texto, True, rgb)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)

    def draw_score(self):
        self.method_draw_score_deaths(f"Score: {self.score}",1000,50,(0,0,0))

    def draw_deaths(self):
        self.method_draw_score_deaths(f"Deaths: {self.death_count}",550,50,(178,34,34))

    def draw_lose(self):
        self.screen.blit(LOSE_TEXT, (SCREEN_WIDTH - LOSE_TEXT.get_width() - 290, 170))
    
    def draw_lifes(self):
        self.method_draw_score_deaths(f"Lifes: {self.lifes}",1000,100,(0,0,0))
    
    def draw_screen_level(self,texto,rgb):
        text = self.font.render(texto, True, (rgb))
        text_rect = text.get_rect()
        text_rect.center = (140, 50)
        self.screen.blit(text, text_rect)

    def draw_level(self):

        if self.score < 400:
            self.draw_screen_level("EASY MODE",(0,128,0))
        elif self.score < 1000:
            self.draw_screen_level("MEDIUM MODE",(238, 173, 45))
        else:
            self.draw_screen_level("HARD MODE",(255, 0, 0))

    def menu_message(self,texto,rgb,x,y):
        text = self.font.render(texto, True, rgb)
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width + x, half_screen_height + y)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        
        if self.death_count == 0:
            self.screen.blit(BG_MENU, (self.x_pos_bg, self.y_pos_bg))

            self.screen.blit(LOGODINORUN, (SCREEN_WIDTH - LOGODINORUN.get_width() - 290, 180))
            self.menu_message("Press (s) to start playing.",(0,0,0),0,140)
        else:
            self.draw_lose()
            self.menu_message("Press (c) to continue playing.",(255,255,255),0,60)

            self.menu_message("Press (r) to restart game.",(255,255,255),0,100)

            self.menu_message(f"Your Score: {self.score}",(255,255,255),0,150)
        
        pygame.display.update()
        self.handle_events_on_menu()
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c]:
                    self.lifes = 1
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_r]:
                    self.death_count = 0
                    self.lifes = 3
                    self.run()

   