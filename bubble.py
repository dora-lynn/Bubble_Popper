import random, math
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

    def is_point_in(self, p):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        distance = ((x - self.circX)**2 +
                    (y - self.circY)**2)**0.5
        return distance <= self.radius

    def draw(self):
        pygame.draw.circle(screen, 'skyblue2', (self.circX, self.circY), self.radius)

    def move(self, screen):
        self.circX += self.velocityX
        self.circY += self.velocityY
        if self.circX + self.radius >= SCREEN_WIDTH:
            self.velocityX = -.05
        elif self.circX - self.radius <= 0:
            self.velocityX = .05
        elif self.circY + self.radius >= SCREEN_HEIGHT:
            self.velocityY = -.05
        elif self.circY - self.radius <= 0:
            self.velocityY = .05
