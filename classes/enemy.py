import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, tipo):
        super().__init__()
        self.image = pygame.image.load(f'graficos/{tipo}')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocidad = 1
        self.direccion = 1

    def update(self):
        self.rect.x += self.velocidad * self.direccion
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.direccion *= -1
            self.rect.y += 20