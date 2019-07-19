import pygame

class Body(object):
    def __init__(self, units, screen, x, y, color=(100, 255, 100)):
        self.units = units
        self.color = color
        self.screen = screen
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setColor(self, color):
        self.color = color

    def draw(self):
        rect = pygame.Rect(self.x*self.units, self.y*self.units, self.units, self.units)
        pygame.draw.rect(self.screen, self.color, rect, 2)