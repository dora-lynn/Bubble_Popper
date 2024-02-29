import pygame
import random
from bubble import Bubble

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bubble Popper")

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

#display score in upper left corner
textX = 10
textY = 10

bubbles = []
for i in range(4):
    bubbles.append(Bubble())

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, 'black')
    screen.blit(score, (x, y))

run = True
while run:
    screen.fill('deepskyblue4')
    show_score(textX, textY)
    for bubble in bubbles:
        bubble.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()