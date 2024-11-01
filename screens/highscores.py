import pygame

class Highscores:
    def __init__(self):
        self.puntajes = []
        self.archivo = 'highscores.txt'

    def cargar_highscores(self):
        try:
            with open(self.archivo, 'r') as f:
                self.puntajes = [int(linea.strip()) for linea in f]
        except FileNotFoundError:
            self.puntajes = []

    def guardar_highscores(self):
        with open(self.archivo, 'w') as f:
            for puntaje in self.puntajes:
                f.write(f"{puntaje}\n")

    def agregar_puntaje(self, puntaje):
        self.puntajes.append(puntaje)
        self.puntajes.sort(reverse=True)
        self.puntajes = self.puntajes[:10]  # Mantener solo los 10 mejores

    def mostrar_highscores(self, pantalla, fuente):
        pantalla.fill('black')
        texto_titulo = fuente.render('High Scores', True, 'white')
        pantalla.blit(texto_titulo, (300, 50))

        for i, puntaje in enumerate(self.puntajes):
            texto_puntaje = fuente.render(f"{i+1}. {puntaje}", True, 'white')
            pantalla.blit(texto_puntaje, (300, 100 + i * 30))

        pygame.display.flip()

        esperando = True
        while esperando:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    esperando = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return