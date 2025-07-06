#########################################
# File Name: main.py
# Description: Main project file for ScrapWarp
# Author: thenimas
# Date: 2025-07-06
#########################################

import pygame

from scripts.objects.config import Config
from scripts.objects.playerShip import playerShip

globalConfig = Config()
FPS = globalConfig.FRAMERATE

FramePerSec = pygame.time.Clock()

pygame.init()
gameWindow = pygame.display.set_mode((globalConfig.WIDTH, globalConfig.HEIGHT))
pygame.display.set_caption("ScrapWarp")

playerShip = playerShip()

visibleGroup = pygame.sprite.Group()

visibleGroup.add(playerShip)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    gameWindow.fill((0,0,0))

    playerShip.move()

    for entity in visibleGroup:
        gameWindow.blit(entity.surf, entity.rect)
    
    pygame.display.update()
    FramePerSec.tick(FPS)