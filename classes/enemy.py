import pygame
import random
from config import *


class Enemy(pygame.sprite.Sprite):
    """
    Clase que representa a los enemigos en el juego.
    Maneja el movimiento, disparo y comportamiento de los enemigos.
    """

    def __init__(self, enemy_type, x, y, difficulty):
        super().__init__()
        # Cargar imagen según el tipo de enemigo
        self.enemy_type = enemy_type
        self.image = pygame.image.load(os.path.join(GRAPHICS_DIR, f'{enemy_type}.png')).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        # Configuración de movimiento
        self.direction = 1
        self.speed = DIFFICULTY_LEVELS[difficulty]['enemy_speed']
        self.bullet_freq = DIFFICULTY_LEVELS[difficulty]['enemy_bullet_freq']

        # Puntuación
        self.points = SCORE_PER_ENEMY[enemy_type]

    def move(self, group_should_descend):
        """
        Mueve al enemigo horizontalmente y desciende cuando el grupo lo requiere
        """
        self.rect.x += self.speed * self.direction
        if group_should_descend:
            self.rect.y += 20

    def should_shoot(self):
        """Determina si el enemigo debe disparar en este frame"""
        return random.random() < self.bullet_freq

    def update(self, group_should_descend):
        """Actualiza el estado del enemigo en cada frame"""
        self.move(group_should_descend)


class EnemyGroup:
    """
    Clase que maneja el grupo completo de enemigos.
    Controla el movimiento coordinado y los disparos.
    """

    def __init__(self, difficulty):
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.difficulty = difficulty
        self.setup_enemies()

        # Sonido de explosión
        self.explosion_sound = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, 'explosion.wav'))
        self.explosion_sound.set_volume(0.3)

    def setup_enemies(self):
        """Configura la formación inicial de enemigos"""
        enemy_types = ['rojo', 'verde', 'verde', 'amarillo', 'amarillo']
        for row, enemy_type in enumerate(enemy_types):
            for column in range(8):
                x = 100 + column * 60
                y = 100 + row * 50
                enemy = Enemy(enemy_type, x, y, self.difficulty)
                self.enemies.add(enemy)

    def update(self):
        """Actualiza el estado de todos los enemigos"""
        should_descend = False

        # Verificar si algún enemigo tocó los bordes
        for enemy in self.enemies:
            if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
                should_descend = True
                for e in self.enemies:
                    e.direction *= -1
                break

        # Actualizar posiciones
        for enemy in self.enemies:
            enemy.update(should_descend)
            if enemy.should_shoot():
                self.bullets.add(Bullet(enemy.rect.centerx, enemy.rect.bottom, direction=1))

        # Actualizar balas
        self.bullets.update()
