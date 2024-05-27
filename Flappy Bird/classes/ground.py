import pygame
from utilities.global_variables import GV

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/ground.png")
        self.image = pygame.transform.scale(self.image, (GV.GROUND_WIDTH, GV.GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.bottom = GV.SCREEN_HEIGHT
        self.x = 0

    def update(self):
        self.x -= GV.GROUND_SPEED

        if self.x <= -GV.GROUND_WIDTH:
            self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.rect.y))
        screen.blit(self.image, (self.x + GV.GROUND_WIDTH, self.rect.y))