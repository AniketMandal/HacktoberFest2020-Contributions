"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.
5. If bird crosses pipes a sound will play
6. Same in case if the bird fall or got hit and if it flap 
7. Showing the points in centre and increment it as bird crosses pipe
"""
from distutils.core import setup
from random import *
from turtle import *
from freegames import vector

bird = vector(0, 0)
balls = []


def tap(x, y):
    """Move bird up in response to screen tap."""
    up = vector(0, 30)
    bird.move(up)


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Draw screen objects."""
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()


def move():
    """Update object positions."""
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

#short code

import random #for generating random numbers
import sys #To Exit the game
import pygame
from pygame.locals import * #Basic Pygame Imports

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'resources\SPRITES\\bird.png'
BACKGROUND = 'resources\SPRITES\\bg.jpeg'
PIPE = 'resources\SPRITES\pipe.png '



 ### This is the point from Where Our Game is going to be Started ###
if __name__ == "__main__":

    pygame.init() #Initializing the Modules of Pygame 
    FPSCLOCK = pygame.time.Clock() #for controlling the FPS
    pygame.display.set_caption('Flappy Bird With Sameer') #Setting the Caption of The Game

    #### LOADING THE SPRITES ####

    GAME_SPRITES['numbers'] = (
        pygame.image.load('resources\SPRITES\\0.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\1.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\2.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\3.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\4.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\5.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\6.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\7.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\8.png').convert_alpha(),
        pygame.image.load('resources\SPRITES\\9.png').convert_alpha(),
    
    ) 
    S
    
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['message'] = pygame.image.load('resources\SPRITES\message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('resources\SPRITES\\b
                                               GAME_SPRITES['pipe'] = (
        
        
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), #### UPPER PIPES, WE JUST ROTATED THE PIPE BY 180deg
    pygame.image.load(PIPE).convert_alpha()   #### LOWER PIPES  
    )

    #Game Sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('resources\AUDIO\die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('resources\AUDIO\hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('resources\AUDIO\point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('resources\AUDIO\swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('resources\AUDIO\wing.wav')
