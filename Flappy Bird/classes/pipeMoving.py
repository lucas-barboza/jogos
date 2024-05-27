import pygame
import random
import numpy
import math
from utilities.global_variables import GV

class Pipe(pygame.sprite.Sprite):

    def __init__(self, xpos, ysize, inverted=False):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/pipe-green.png")
        self.image = pygame.transform.scale(self.image, (GV.PIPE_WIDTH, GV.PIPE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.marked = False

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.y = -(self.rect.height - ysize)
        else:
            self.rect.y = GV.SCREEN_HEIGHT - ysize

        self.initial_y = self.rect.y
        self.start_time = pygame.time.get_ticks()
        
    def update(self):
        self.rect.x -= GV.GAME_SPEED
        # Calcular o tempo decorrido desde o início
        elapsed_time = pygame.time.get_ticks() - self.start_time
        
        # Aplicar uma função de easing ao tempo para suavizar o movimento
        eased_time = self.ease_in_out(elapsed_time / GV.PIPE_EASING_DURATION)
        
        # Calcular a posição vertical do cano com base no tempo suavizado
        target_y = self.initial_y + GV.VERTICAL_AMPLITUDE * eased_time
        
        # Atualizar a posição vertical do cano
        self.rect.y = target_y
        
        
        if self.rect.right < 0:
            self.kill()

    def ease_in_out(self, t):
        # Função de easing: ease in out
        return 0.5 - 0.5 * math.cos(math.pi * t)

def not_maket_pipe(pipe_group):
    for i in range(0, len(pipe_group), 2):
        if not pipe_group.sprites()[i].marked:
            return pipe_group.sprites()[i].rect.top, pipe_group.sprites()[i + 1].rect.bottom

def add_pipes(pipe_group):
    pipe_heigth = random.randint(150, GV.MAX_PIPE_HEIGHT)
    pipe = Pipe(GV.SCREEN_WIDTH, pipe_heigth)
    inverted_pipe = Pipe(GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT - pipe_heigth - GV.PIPE_GAP, inverted=True)
    pipe_group.add(pipe)
    pipe_group.add(inverted_pipe)

def more_pipes(last_pipe_spawn_time, pipe_groups):
    current_time = pygame.time.get_ticks()
    if current_time - last_pipe_spawn_time > GV.PIPE_SPAWN_INTERVAL:
        add_pipes(pipe_groups)
        last_pipe_spawn_time = current_time
    return last_pipe_spawn_time