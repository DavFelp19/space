import pygame
from config import *


class Player(pygame.sprite.Sprite):
    """
    Clase que representa al jugador en el juego.
    Maneja el movimiento, disparo y colisiones del jugador.
    """

    def __init__(self, player_type, pos_x):
        super().__init__()
        self.player_type = player_type
        # Cargar imagen según el tipo de jugador
        image_name = 'jugador_celeste.png' if player_type == 'P1' else 'jugador_morado.png'
        self.image = pygame.image.load(os.path.join(GRAPHICS_DIR, image_name)).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(pos_x, SCREEN_HEIGHT - 20))

        # Configuración de movimiento
        self.speed = PLAYER_SPEED
        self.controls = PLAYER_CONTROLS[player_type]

        # Configuración de disparo
        self.bullets = pygame.sprite.Group()
        self.can_shoot = True
        self.shoot_cooldown = 500  # milisegundos
        self.last_shot = 0

        # Sonidos
        self.shoot_sound = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, 'laser.wav'))
        self.shoot_sound.set_volume(0.5)

    def move(self):
        """Maneja el movimiento del jugador basado en las teclas presionadas"""
        keys = pygame.key.get_pressed()

        if keys[self.controls['left']]:
            self.rect.x -= self.speed
        if keys[self.controls['right']]:
            self.rect.x += self.speed

        # Limitar movimiento a los bordes de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        """Maneja el disparo del jugador"""
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if keys[self.controls['shoot']] and self.can_shoot:
            if current_time - self.last_shot >= self.shoot_cooldown:
                self.shoot_sound.play()
                self.bullets.add(Bullet(self.rect.centerx, self.rect.top))
                self.last_shot = current_time

    def update(self):
        """Actualiza el estado del jugador en cada frame"""
        self.move()
        self.shoot()
        self.bullets.update()
