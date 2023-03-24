import pygame
import os

TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
FONT_STYLE = "freesansbold.ttf"

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
pygame.mixer.init()
SOUNDTRACK = pygame.mixer.Sound('dino_runner/assets/Sounds/soundtrack.mp3')
SOUNDTRACK.set_volume(0.5)
DEATHSOUND = pygame.mixer.Sound('dino_runner/assets/Sounds/death.wav')
HITSOUND = pygame.mixer.Sound('dino_runner/assets/Sounds/hit01.wav')


RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

PLANT = [
    pygame.image.load(os.path.join(IMG_DIR, "Monsters/planta1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Monsters/planta2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Monsters/planta3.png"))
]
SKELETON = [
    pygame.image.load(os.path.join(IMG_DIR, "Monsters/esqueleto1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Monsters/esqueleto2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Monsters/esqueleto3.png"))

]
MINOTAUR = [
    pygame.image.load(os.path.join(IMG_DIR, "Monsters/minotaur1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Monsters/minotaur2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Monsters/minotaur3.png"))
]

BAT = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bat1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bat2.png"))
    ]

METEOR = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/1.png")),
]

LOGODINORUN = pygame.image.load(os.path.join(IMG_DIR, 'Other/logo.png'))
half_screen_height = SCREEN_HEIGHT // 2
half_screen_width = SCREEN_WIDTH // 2
LOSE_TEXT = pygame.image.load(os.path.join(IMG_DIR, 'Other/gameovertest2.png'))

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/teste3.jpg'))
BG_MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/backmenu2.jpg'))
COIN = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star3.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star5.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star6.png'))
]

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))

DEFAULT_TYPE = "default"
