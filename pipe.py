import pygame
import random
from settings import *

class Pipe:
    PIPE_WIDTH = 50
    GAP = 200

    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(50, SCREEN_HEIGHT - self.GAP - 50)
        self.scored = False

    def update(self):
        self.x -= 3

    def draw(self, screen):
        # 위쪽 파이프
        pygame.draw.rect(screen, GREEN, (self.x, 0, self.PIPE_WIDTH, self.height))
        # 아래쪽 파이프
        pygame.draw.rect(screen, GREEN, 
                        (self.x, self.height + self.GAP, 
                         self.PIPE_WIDTH, SCREEN_HEIGHT - (self.height + self.GAP)))