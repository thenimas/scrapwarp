#########################################
# File Name: main.py
# Description: Main project file for ScrapWarp
# Author: J. Towns
# Date: 2025-07-06
#########################################

import pygame

from scripts.objects.config import Config

globalConfig = Config()
FPS = globalConfig.FRAMERATE

FramePerSec = pygame.time.Clock()

pygame.init()
gameWindow = pygame.display.set_mode((globalConfig.WIDTH, globalConfig.HEIGHT))
pygame.display.set_caption("ScrapWarp")

while True:

    pygame.display.update()
    FramePerSec.tick(FPS)