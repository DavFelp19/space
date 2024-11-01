import pygame
import os
import random
from random import choice, randint
from classes.player import Jugador
from classes.obstacle import Bloque
from classes.enemy import Alien  # Asegúrate de que la clase Alien esté en enemy.py

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Forma del obstáculo
forma_obstaculo = [
    '  xxxxxxx  ',
    ' xxxxxxxxx ',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxx     xxx',
    'xx       xx'
]

class Juego:
    def __init__(self):
        self.estado = "menu"
        self.modo = None
        self.fuente = pygame.font.Font(os.path.join(BASE_DIR, 'fuente', 'Pixeled.ttf'), 20)
        self.configurar_sonidos()
        self.reiniciar_juego()

    def configurar_sonidos(self):
        self.musica = pygame.mixer.Sound(os.path.join(BASE_DIR, 'sonidos', 'musica.wav'))
        self.musica.set_volume(0.2)
        self.sonido_explosion = pygame.mixer.Sound(os.path.join(BASE_DIR, 'sonidos', 'explosion.wav'))
        self.sonido_explosion.set_volume(0.3)

    def reiniciar_juego(self):
        self.jugador1 = None
        self.jugador2 = None
        self.vidas1 = 3
        self.vidas2 = 3
        self.puntuacion1 = 0
        self.puntuacion2 = 0
        self.bloques = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.lasers_alien = pygame.sprite.Group()
        self.extra = pygame.sprite.GroupSingle()
        self.tiempo_aparicion_extra = randint(40, 80)
        self.direccion_alien = 1
        self.crear_obstaculos()
        self.configurar_aliens()

    def crear_obstaculos(self):
        for indice_obstaculo in range(4):
            x_obstaculo = indice_obstaculo * (800 / 4) + 50
            self.crear_obstaculo(x_obstaculo)

    def crear_obstaculo(self, x_obstaculo):
        for indice_fila, fila in enumerate(forma_obstaculo):
            for indice_columna, columna in enumerate(fila):
                if columna == 'x':
                    x = x_obstaculo + (indice_columna * 30)
                    y = 600 - (indice_fila * 30 + 50)
                    self.bloques.add(Bloque(30, 'grey', x, y))

    def configurar_aliens(self):
        for fila in range(6):
            for columna in range(8):
                x = columna * 60 + 60
                y = fila * 40 + 100
                if fila == 0:
                    alien = Alien('rojo', x, y)
                elif fila == 1 or fila == 2:
                    alien = Alien('verde', x, y)
                else:
                    alien = Alien('azul', x, y)
                self.aliens.add(alien)

    def dibujar_elementos(self, pantalla):
        self.bloques.draw(pantalla)
        self.aliens.draw(pantalla)
        self.lasers_alien.draw(pantalla)
        self.extra.draw(pantalla)
        if self.jugador1:
            self.jugador1.lasers.draw(pantalla)
        if self.jugador2:
            self.jugador2.lasers.draw(pantalla)

    def revisar_colisiones(self):
        # Colisiones de láser jugador con aliens
        for jugador in [self.jugador1, self.jugador2]:
            if jugador:
                for laser in jugador.lasers:
                    aliens_golpeados = pygame.sprite.spritecollide(laser, self.aliens, True)
                    if aliens_golpeados:
                        laser.kill()
                        if jugador == self.jugador1:
                            self.puntuacion1 += 100 * len(aliens_golpeados)
                        else:
                            self.puntuacion2 += 100 * len(aliens_golpeados)
                        self.sonido_explosion.play()

    def jugar(self, pantalla):
        """Lógica principal del juego."""
        self.jugador1.update()
        if self.jugador2:
            self.jugador2.update()

        self.aliens .update()
        self.lasers_alien.update()
        self.extra.update()

        self.revisar_colisiones()
        self.dibujar_elementos(pantalla)