import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen):
        super().__init__()
        self.image = pygame.image.load(f'graficos/{imagen}')
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.velocidad = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.velocidad