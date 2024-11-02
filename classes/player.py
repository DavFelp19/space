import pygame


class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen, es_jugador_uno=True):
        super().__init__()
        self.image = pygame.image.load(f'graficos/{imagen}')
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.velocidad = 1
        self.es_jugador_uno = es_jugador_uno  # Para distinguir entre jugador 1 y 2

    def update(self):
        teclas = pygame.key.get_pressed()

        if self.es_jugador_uno:
            # Controles para el jugador 1 (flechas)
            if teclas[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.velocidad
            if teclas[pygame.K_RIGHT] and self.rect.right < 800:
                self.rect.x += self.velocidad
        else:
            # Controles para el jugador 2 (A y D)
            if teclas[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= self.velocidad
            if teclas[pygame.K_d] and self.rect.right < 800:
                self.rect.x += self.velocidad