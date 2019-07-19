import random

import pygame


class Food:
    def __init__(self, units, screen, color, x, y):
        self.units = units
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        rect = pygame.Rect(self.x*self.units, self.y*self.units, self.units, self.units)
        pygame.draw.rect(self.screen, self.color, rect, 0)

    def getX(self):
        return self.x

    def getY(self):
        return self.y