import pygame
import os

class Highscores:
    def __init__(self):
        self.archivo = 'highscores.txt'
        self.puntajes = []

    def cargar_highscores(self):
        """Carga los puntajes más altos desde un archivo."""
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                self.puntajes = [int(line.strip()) for line in f.readlines()]

    def guardar_highscores(self):
        """Guarda los puntajes más altos en un archivo."""
        with open(self.archivo, 'w') as f:
            for puntaje in sorted(self.puntajes, reverse=True)[:10]:  # Guarda solo los 10 mejores
                f.write(f"{puntaje}\n")

    def agregar_puntaje(self, puntaje):
        """Agrega un nuevo puntaje a la lista de puntajes."""
        self.puntajes.append(puntaje)

    def mostrar_highscores(self, pantalla, fuente):
        """Muestra los puntajes más altos en la pantalla."""
        pantalla.fill('black')
        texto = fuente.render('High Scores', True, 'white')
        pantalla.blit(texto, (300, 50))

        for i, puntaje in enumerate(sorted(self.puntajes, reverse=True)[:10]):
            texto_puntaje = fuente.render(f"{i + 1}. {puntaje}", True, 'white')
            pantalla.blit(texto_puntaje, (300, 100 + i * 30))

        pygame.display.flip()
        pygame.time.wait(3000)  # Espera 3 segundos antes de volver al menúblit(options, (SCREEN_WIDTH // 2 - options.get_width() // 2, SCREEN_HEIGHT - 50))