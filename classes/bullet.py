import pygame
from typing import Union

class Bala(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, direccion: int):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad = 1 * direccion

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()