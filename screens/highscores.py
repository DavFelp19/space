import sys
import pygame
import os

class Highscores:
    def __init__(self):
        self.puntajes = []
        self.archivo = 'highscores.txt'
        self.max_puntajes = 3  # Cambiado a 3 para guardar solo el top 3

    def cargar_highscores(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    self.puntajes = [int(linea.strip()) for linea in f if linea.strip()]
            else:
                with open(self.archivo, 'w') as f:
                    f.write('')
                self.puntajes = []
        except Exception as e:
            print(f"Error al cargar highscores: {e}")
            self.puntajes = []

    def guardar_highscores(self):
        try:
            with open(self.archivo, 'w') as f:
                for puntaje in self.puntajes:
                    f.write(f"{puntaje}\n")
        except Exception as e:
            print(f"Error al guardar highscores: {e}")

    def agregar_puntaje(self, puntaje):
        if puntaje > 0:  # Solo agregar puntajes mayores que 0
            self.puntajes.append(puntaje)
            self.puntajes = list(set(self.puntajes))  # Eliminar duplicados
            self.puntajes.sort(reverse=True)  # Ordenar de mayor a menor
            self.puntajes = self.puntajes[:self.max_puntajes]  # Mantener solo el top 3
            self.guardar_highscores()

    def mostrar_highscores(self, pantalla, fuente):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return "menu"

            pantalla.fill('black')
            texto_titulo = fuente.render('Top 3 Mejores Puntajes', True, 'white')
            pantalla.blit(texto_titulo, (250, 50))

            if len(self.puntajes) == 0:
                texto_vacio = fuente.render('No hay puntajes guardados', True, 'white')
                pantalla.blit(texto_vacio, (250, 250))
            else:
                medallas = ['🥇', '🥈', '🥉']
                for i, puntaje in enumerate(self.puntajes):
                    medalla = medallas[i] if i < 3 else ''
                    texto_puntaje = fuente.render(f"{medalla} {puntaje}", True, 'white')
                    pantalla.blit(texto_puntaje, (300, 150 + i * 50))

            texto_volver = fuente.render('Presiona cualquier tecla para volver', True, 'white')
            pantalla.blit(texto_volver, (200, 500))

            pygame.display.flip()
            clock.tick(30)