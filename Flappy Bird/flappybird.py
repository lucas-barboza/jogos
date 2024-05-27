## Projeto ainda não finalizado

import pygame
import sys
import os
from utilities.global_variables import GV
from classes.bird import Bird
from classes.ground import Ground
from classes.pipe import add_pipes, more_pipes

# Inicializa o Pygame
pygame.init()

# Iniciando o clock para os frames
clock = pygame.time.Clock()

# Funcao para desenhar as images e atualizar
def update_draws(bird, pipe_group, ground):
    # Desenhar a imagem de fundo na tela
    screen.blit(game_surface, (0, 0))

    
    # Atualizar e desenhar o bird
    bird.update()
    bird.draw(screen)

    # Atualizar e desenhar os canos
    pipe_group.update()
    pipe_group.draw(screen)
    
    # Atualizar e desenhar o ground
    ground.update()
    ground.draw(screen)


def verify_collisions(bird, pipe_group):
    if bird.check_collision_ground():
        return True
    elif bird.check_collision_pipe(pipe_group):
        return True


# Defenindo as dimensoes da tela
last_pipe_spawn_time = pygame.time.get_ticks()
screen = pygame.display.set_mode((GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Carregando a imagem de fundo e redimensione-a para o tamanho da tela
game_surface = pygame.image.load("./images/background.png").convert()
game_surface = pygame.transform.scale(game_surface, (GV.SCREEN_WIDTH, GV.SCREEN_HEIGHT))

# Criando birds
bird = Bird()

# Criando a variavel do grouds
ground = Ground()

# Criando o grupo de canos
pipe_group = pygame.sprite.Group()
add_pipes(pipe_group)

game_over = False
while not game_over:
    # Limita a taxa de quadros
    clock.tick(30)

    # Lidar com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            pipe_group.empty()
        
        # Verifique se a tecla de seta para cima é pressionada
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                bird.jump()
                
    update_draws(bird, pipe_group, ground)

    last_pipe_spawn_time = more_pipes(last_pipe_spawn_time, pipe_group)
    
    bird.scored(pipe_group)
    
    if verify_collisions(bird, pipe_group):
        game_over = True
    
    # Atualize a tela
    pygame.display.update()
