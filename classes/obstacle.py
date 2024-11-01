import pygame
from config import *


class Obstacle:
    """
    Clase que representa los obstáculos destructibles.
    Maneja la creación y destrucción de los bloques que forman el obstáculo.
    """

    def __init__(self, x_pos, y_pos):
        self.blocks = pygame.sprite.Group()
        self.create_obstacle(x_pos, y_pos)

    def create_obstacle(self, x_start, y_start):
        """Crea la forma del obstáculo usando bloques individuales"""
        shape = [
            '  xxxxxxx  ',
            ' xxxxxxxxx ',
            'xxxxxxxxxxx',
            'xxxxxxxxxxx',
            'xxx     xxx'
        ]

        for row_index, row in enumerate(shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * 4
                    y = y_start + row_index * 4
                    block = ObstacleBlock(x, y)
                    self.blocks.add(block)


class ObstacleBlock(pygame.sprite.Sprite):
    """
    Clase que representa cada bloque individual de un obstáculo.
    """

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))