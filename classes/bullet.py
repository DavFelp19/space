import pygame
from config import *


class Bullet(pygame.sprite.Sprite):
    """
    Clase que representa las balas tanto de jugadores como de enemigos.
    Maneja el movimiento y colisiones de las balas.
    """

    def __init__(self, x, y, direction=-1):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = BULLET_SPEED * direction

    def update(self):
        """Actualiza la posición de la bala y la elimina si sale de la pantalla"""
        self.rect.y += self.speed

        # Eliminar si sale de la pantalla
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()