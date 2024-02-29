import random
import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Bubble:

    def __init__(self):
        self.radius = random.randint(50, 150)
        self.circX = random.randint(100, 1100)
        self.circY = random.randint(-100, 700)
    def draw(self):
        pygame.draw.circle(screen, 'skyblue2', (self.circX, self.circY), self.radius)
