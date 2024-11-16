import pygame
from bird import Bird
from pipe import Pipe
from settings import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        self.running = True
        self.reset_game()

    def reset_game(self):
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.spawn_pipe()

    def spawn_pipe(self):
        self.pipes.append(Pipe())

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

    def update(self):
        self.bird.update()
        
        # 파이프 업데이트
        for pipe in self.pipes[:]:
            pipe.update()
            if pipe.x < -pipe.PIPE_WIDTH:
                self.pipes.remove(pipe)
            if not pipe.scored and pipe.x < self.bird.x:
                self.score += 1
                pipe.scored = True

        # 새로운 파이프 생성
        if len(self.pipes) < 3:
            if self.pipes[-1].x < SCREEN_WIDTH - 200:
                self.spawn_pipe()

        # 충돌 검사
        for pipe in self.pipes:
            if self.bird.check_collision(pipe):
                self.reset_game()

    def draw(self):
        self.screen.fill(SKY_BLUE)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.bird.draw(self.screen)
        
        # 점수 표시
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()