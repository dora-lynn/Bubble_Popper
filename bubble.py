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
        self.velocityX = random.uniform(-.05, .05)
        self.velocityY = random.uniform(-.05, .05)

    def draw(self):
        pygame.draw.circle(screen, 'skyblue2', (self.circX, self.circY), self.radius)

    def move(self, screen):
        self.circX += self.velocityX
        self.circY += self.velocityY
        if self.circX >= SCREEN_WIDTH:
            self.velocityX = -.05
        elif self.circX <= 0:
            self.velocityX = .05
        elif self.circY >= SCREEN_HEIGHT:
            self.velocityY = -.05
        elif self.circY <= 0:
            self.velocityY = .05
