import pygame
from pygame.locals import *


pygame.init()

windowSize = (1500, 800)
window = pygame.display.set_mode((windowSize), pygame.NOFRAME|SCALED, vsync=1)

obj = pygame.image.load(f'assets/ball.png').convert_alpha()
bg = pygame.image.load(f'assets/bg.png').convert_alpha()
font = pygame.font.Font('assets/fonts/font.ttf', 25)
font2 = pygame.font.Font('assets/fonts/font.ttf', 15)

def text(text, font, x, y):
    text = font.render(text, True, (255, 255, 255))
    window.blit(text, (x, y))