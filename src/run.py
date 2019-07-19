import random

import pygame

from src.models.body import Body
from src import app
from src.models.food import Food
from src.models.snake import Snake

(width, height) = (800, 800)

#screen objects
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

#screen flip
pygame.display.flip()

#initialize
run = True
snake = Snake(20, screen, 5, 20, 20)
(x, y) = (0, 0)
food_exists = False
tick_timer = 0

while run:
    clockobject = pygame.time.Clock()
    clockobject.tick(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Reset screen
    screen.fill(255)

    #Time to refresh screen
    tick_timer += 1

    #Generate Food
    if food_exists == False:
        apple = Food(20, screen, (255,100,100), random.randint(0,39), random.randint(0,39))
        food_exists = True
    apple.draw()

    #Key input
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w and y != 1:
            (x, y) = (0, -1)
        if event.key == pygame.K_s and y != -1:
            (x, y) = (0, 1)
        if event.key == pygame.K_a and x != 1:
            (x, y) = (-1, 0)
        if event.key == pygame.K_d and x != -1:
            (x, y) = (1, 0)

    if tick_timer % 8 == 0:
        #Move Snake
        if x != 0 or y != 0:
            snake.move(x, y)
        snake.render()

        #Eat
        if snake.eating(apple):
            snake.eat(x, y)
            food_exists = False
            apple = None

        #Lose Game
        if snake.kill() is True:
            print("You lose!")
            run = False

        #Update Game
        pygame.display.update()