import pygame
import random
import numpy
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
        
    def update(self):
        self.rect.x -= GV.GAME_SPEED
        if self.rect.right < 0:
            self.kill()

def add_pipes(pipe_group):
    pipe_heigth = random.randint(100, GV.MAX_PIPE_HEIGHT)
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