#########################################
# File Name: playerShip.py
# Description: logic container for the player's ship
# Author: thenimas
# Date: 2025-07-06
#########################################

import pygame

vec = pygame.math.Vector2

from scripts.objects.config import Config

globalConfig = Config()

class playerShip(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100,50))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(50,25))

        self.pos = vec((700,300))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.accVal = 0.15
        self.decVal = -0.005


    def move(self):
        self.acc = vec(0,0)
        
        pressedKeys = pygame.key.get_pressed()
        
        accVal = self.accVal
        decVal = self.decVal

        if pressedKeys[pygame.K_LEFT]:
            self.acc.x = -accVal
        if pressedKeys[pygame.K_RIGHT]:
            self.acc.x = accVal
        if pressedKeys[pygame.K_UP]:
            self.acc.y = -accVal
        if pressedKeys[pygame.K_DOWN]:
            self.acc.y = accVal

        self.acc.x += self.vel.x * decVal
        self.acc.y += self.vel.y * decVal
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x > globalConfig.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = globalConfig.WIDTH

        if self.pos.y > globalConfig.HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = globalConfig.HEIGHT
        
        self.rect.midbottom = self.pos