import pygame
import sys
def mostrar_pantalla_victoria(pantalla, fuente, game_state):
    pantalla.fill('black')
    texto_victoria = fuente.render('¡VICTORIA!', True, 'white')
    texto_puntuacion = fuente.render(f'Puntuación: {game_state.puntuacion1}', True, 'white')
    texto_opciones = fuente.render('1 - Menú   2 - Salir', True, 'white')

    pantalla.blit(texto_victoria, (300, 200))
    pantalla.blit(texto_puntuacion, (300, 250))
    pantalla.blit(texto_opciones, (300, 300))

    pygame.display.flip()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_state.estado = "menu"
                    esperando = False
                elif event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()