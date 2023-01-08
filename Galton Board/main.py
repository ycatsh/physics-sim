import pygame, sys
from pygame.locals import *
import random
import pymunk.pygame_util

clock = pygame.time.Clock()
pygame.init()

gravity = 981 #can be changed accordingly.
space = pymunk.Space()
space.gravity = 0, gravity

windowSize = (1500, 1000)
window = pygame.display.set_mode((windowSize), pygame.NOFRAME, vsync=1) #need to change to fullscreen

num_balls = int(input('enter the number of balls: ')) #exception handler yet to be added
bg = pygame.image.load('assets/bg.png').convert_alpha()


def draw(space, window, draw_options): #simulation draw window 
    window.blit(bg, (0,0))
    space.debug_draw(draw_options)
    pygame.display.update()

def add_funnel(space): #top funnel which directs the ball towards the nails
    funnels = [[(0, -30), (700, 150)], [(1500, -30), (800, 150)]]

    for pos in funnels:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, pos[0], pos[1], 5)
        shape.color = (255, 255, 255, 100)
        space.add(body,shape)

def add_cup(space): #cups which hold the balls after fall
    base_cup = [(0, 995), (1500, 995)]

    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, base_cup[0], base_cup[1], 5)
    shape.color = (255, 255, 255, 100)
    space.add(body,shape)

    n = 220
    for _ in range(8):
        cups = [(n, 995), (n, 600)]
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, cups[0], cups[1], 5)
        shape.color = (255, 255, 255, 100)
        space.add(body,shape)
        n += 150

def add_nail(space): #arranged in Pascal's Triangle sequence 
    nails = [
    [750, 250], 
    [670, 300], [830, 300], 
    [590, 350], [750, 350], [910, 350], 
    [510, 400], [670, 400], [830, 400], [990, 400],  
    [430, 450], [590, 450], [750, 450], [910, 450], [1070, 450], 
    [350, 500], [510, 500], [670, 500], [830, 500], [990, 500], [1150, 500]
    ]

    for pos in nails:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Circle(body, 18)
        space.add(body, shape)

def add_ball(space, radius, mass): #balls for simulation 
    body = pymunk.Body()
    pos = [random.randint(200, 700), random.randint(700, 1300)]
    body.position = (random.choice(pos), -(random.randint(100, 300)))
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.elasticity = 0.9
    shape.color = (154, 217, 255, 100)
    space.add(body, shape)
    return shape


def main(): #main simulation loop
    draw_options = pymunk.pygame_util.DrawOptions(window)

    add_nail(space)
    add_funnel(space)
    add_cup(space)

    for _ in range(num_balls):
        ball = add_ball(space, 9, 10)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        draw(space, window, draw_options)
        space.step(1/60)
        clock.tick(60)

main()