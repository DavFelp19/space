import pygame

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 40))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mascara = pygame.mask.from_surface(self.image)

    def dañar(self, x, y):
        pos_relativa = x - self.rect.x, y - self.rect.y
        if self.mascara.get_at(pos_relativa):
            pygame.draw.circle(self.image, 'black', pos_relativa, 3)
            self.mascara = pygame.mask.from_surface(self.image)
