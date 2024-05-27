import pygame
from utilities.global_variables import GV

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load("images/yellowbird-upflap.png"),
                       pygame.image.load("images/yellowbird-midflap.png"),
                       pygame.image.load("images/yellowbird-downflap.png")]
        
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image, (GV.BIRD_WIDTH, GV.BIRD_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (625, 370)
        self.speed = GV.JUMP_SPEED
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.score = 0
        self.passed_pipes = []

    def update(self):
        self.speed += GV.GRAVITY
        self.rect.y += self.speed
        self.passed_pipes = []

        if self.speed < 0:
            self.angle = GV.MAX_ROTATION_UP
        else:
            if self.angle > GV.MAX_ROTATION_DOWN:
                self.angle -= GV.GAME_SPEED
        self.image = pygame.transform.rotate(self.images[self.current_image], self.angle)

    def jump(self):
        self.speed = -GV.JUMP_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision_ground(self):
        if self.rect.top <= 0: # Verfica se bate no topo para nao ultrapassar
            self.rect.top = 0
            self.speed = 0
            return False

        # Verifica se o passaro bateu no chao
        elif self.rect.bottom >= GV.SCREEN_HEIGHT - GV.GROUND_HEIGHT:
            self.rect.bottom = GV.SCREEN_HEIGHT - GV.GROUND_HEIGHT
            self.speed = 0
            return True
        
    def check_collision_top(self):
        if self.rect.top <= 0: # Verfica se bate no topo para nao ultrapassar
            self.rect.top = 0
            self.speed = 0
            return True
        
    def check_collision_pipe(self, pipe_group):
        for pipe in pipe_group:
            if pygame.sprite.collide_mask(self, pipe):
                return True
        return False
            
    def scored(self, pipe_group):
        for i in range(0, len(pipe_group), 2):
            if not pipe_group.sprites()[i].marked and pipe_group.sprites()[i].rect.right < self.rect.centerx:
                # Verifica se o pássaro passou completamente pelo cano
                self.score += 1
                pipe_group.sprites()[i].marked = True 
        return self.score
