import os
import pygame

# Directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAPHICS_DIR = os.path.join(BASE_DIR, 'graficos')
SOUNDS_DIR = os.path.join(BASE_DIR, 'sonidos')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Configuración de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Niveles de dificultad
DIFFICULTY_LEVELS = {
    'FACIL': {
        'enemy_speed': 1,
        'enemy_bullet_freq': {
            'individual': 1,
            'multijugador': 2
        }
    },
    'MEDIO': {
        'enemy_speed': 2,
        'enemy_bullet_freq': {
            'individual': 2,
            'multijugador': 3
        }
    },
    'DIFICIL': {
        'enemy_speed': 3,
        'enemy_bullet_freq': {
            'individual': 3,
            'multijugador': 4
        }
    }
}
# Puntuaciones
SCORE_PER_ENEMY = {
    'rojo.png': 100,
    'verde.png': 200,
    'amarillo.png': 300
}

# Configuración de jugadores
PLAYER_CONTROLS = {
    'P1': {
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
        'shoot': pygame.K_RETURN
    },
    'P2': {
        'left': pygame.K_a,
        'right': pygame.K_d,
        'shoot': pygame.K_SPACE
    }
}