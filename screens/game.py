import pygame
import random
from classes.player import Jugador
from classes.enemy import Alien
from classes.obstacle import Obstaculo
from classes.bullet import Bala

class Juego:
    def __init__(self, pantalla, game_state, fuente):
        self.pantalla = pantalla
        self.game_state = game_state
        self.fuente = fuente
        self.jugadores = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()
        self.balas_jugador = pygame.sprite.Group()
        self.balas_enemigo = pygame.sprite.Group()
        self.sonido_laser = pygame.mixer.Sound('sonidos/laser.wav')
        self.sonido_explosion = pygame.mixer.Sound('sonidos/explosion.wav')
        self.inicializar_juego()

    def inicializar_juego(self):
        # Crear jugadores
        self.jugadores.add(Jugador(400, 550, 'jugador_celeste.png'))
        if self.game_state.modo == "multijugador":
            self.jugadores.add(Jugador(200, 550, 'jugador_morado.png'))

        # Crear enemigos
        for fila in range(5):
            for columna in range(11):
                x = 50 + columna * 50
                y = 50 + fila * 40
                tipo = 'rojo.png' if fila == 0 else 'verde.png' if fila < 3 else 'amarillo.png'
                self.enemigos.add(Alien(x, y, tipo))

        # Crear obstáculos
        for i in range(4):
            self.obstaculos.add(Obstaculo(100 + i * 200, 450))

    def manejar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state.estado = "menu"
                    return False
                if event.key == pygame.K_RETURN:
                    self.disparar(self.jugadores.sprites()[0])
                if event.key == pygame.K_SPACE and self.game_state.modo == "multijugador":
                    self.disparar(self.jugadores.sprites()[1])
        return True

    def actualizar(self):
        self.jugadores.update()
        self.enemigos.update()
        self.balas_jugador.update()
        self.balas_enemigo.update()

        # Colisiones
        for bala in self.balas_jugador:
            enemigos_golpeados = pygame.sprite.spritecollide(bala, self.enemigos, True)
            if enemigos_golpeados:
                self.sonido_explosion.play()
                self.game_state.puntuacion1 += 100
                bala.kill()

        for bala in self.balas_enemigo:
            jugadores_golpeados = pygame.sprite.spritecollide(bala, self.jugadores, False)
            if jugadores_golpeados:
                self.game_state.vidas -= 1
                bala.kill()

        # Disparo aleatorio de enemigos
        if random.randint(1, 100) == 1:
            if self.enemigos:
                enemigo = random.choice(self.enemigos.sprites())
                self.balas_enemigo.add(Bala(enemigo.rect.centerx, enemigo.rect.bottom, 1))

        # Verificar victoria o derrota
        if not self.enemigos:
            self.game_state.estado = "victoria"
        elif self.game_state.vidas <= 0:
            self.game_state.estado = "derrota"

    def disparar(self, jugador):
        self.sonido_laser.play()
        self.balas_jugador.add(Bala(jugador.rect.centerx, jugador.rect.top, -1))

    def dibujar(self):
        self.pantalla.fill('black')
        self.jugadores.draw(self.pantalla)
        self.enemigos.draw(self.pantalla)
        self.obstaculos.draw(self.pantalla)
        self.balas_jugador.draw(self.pantalla)
        self.balas_enemigo.draw(self.pantalla)

        # Dibujar puntuación y vidas
        texto_puntuacion = self.fuente.render(f'Puntuación: {self.game_state.puntuacion1}', True, 'white')
        texto_vidas = self.fuente.render(f'Vidas: {self.game_state.vidas}', True, 'white')
        self.pantalla.blit(texto_puntuacion, (10, 10))
        self.pantalla.blit(texto_vidas, (600, 10))

    def jugar(self):
        continuar = True
        while continuar and self.game_state.estado == "juego":
            continuar = self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            pygame.display.flip()