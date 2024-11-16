import pygame
from settings import *

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.size = 30

    def jump(self):
        self.velocity = self.jump_strength

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        # 화면 경계 처리
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > SCREEN_HEIGHT - self.size:
            self.y = SCREEN_HEIGHT - self.size
            self.velocity = 0

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, self.size, self.size))

    def check_collision(self, pipe):
        bird_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        upper_pipe = pygame.Rect(pipe.x, 0, pipe.PIPE_WIDTH, pipe.height)
        lower_pipe = pygame.Rect(pipe.x, pipe.height + pipe.GAP, pipe.PIPE_WIDTH, SCREEN_HEIGHT)
        
        return bird_rect.colliderect(upper_pipe) or bird_rect.colliderect(lower_pipe)