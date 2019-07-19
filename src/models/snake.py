import pygame
from src.models.body import Body
import random

from src.models.food import Food


class Snake(object):
    def __init__(self, units, screen, pieces, x, y):
        self.units = units
        self.screen = screen
        self.pieces = pieces
        self.x = x
        self.y = y
        self.bodies = []

        counter = 0
        for piece in range(0,pieces):
            if piece == 0:
                body = Body(units, screen, x+counter, y, (100,100,255))
            else:
                body = Body(units, screen, x+counter, y)
            counter -= 1
            self.bodies.append(body)


    def render(self):
        for body in self.bodies:
            body.draw()


    def move(self, x, y):
        self.x += x
        self.y += y
        self.bodies.pop(-1)
        self.bodies[0].setColor((100,255,100))
        self.bodies.insert(0, Body(self.units, self.screen, self.x, self.y, (100, 100, 255)))

    def kill(self):
        for body in self.bodies:
            if body.getX() > 39 or body.getX() < 0 or body.getY() > 39 or body.getY() < 0:
                return True
            bodies = self.bodies[:]
            bodies.remove(body)
            for others in bodies:
                if body.getX() == others.getX() and body.getY() == others.getY():
                    return True

        return False

    def eat(self, x, y):
        self.bodies.append(Body(self.units, self.screen, self.x + x, self.y + y))

    def eating(self, food):
        for body in self.bodies:
            if body.getX() == food.getX() and body.getY() == food.getY():
                return True
        return False

