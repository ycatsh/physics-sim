import sys
import pygame
import pymunk
from pygame.locals import *
import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

clock = pygame.time.Clock()

pygame.init()

windowSize = (1500, 800)
window = pygame.display.set_mode((windowSize), pygame.NOFRAME, vsync=1)

text_color = (255, 255, 255)
font = pygame.font.Font('assets/fonts/C&C Red Alert [INET].ttf', 20)

particle = ''

def mtext(text, font, text_color, x, y):
    m = font.render(text, True, text_color)
    window.blit(m, (x, y))

class Particle:
    def __init__(self, x, y, temp):
        self.image = particle
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass

    def show(self):
        pass

def main():

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


main()
