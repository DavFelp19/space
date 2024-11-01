import pygame

def mostrar_ayuda(pantalla, fuente):
    """Muestra la pantalla de ayuda."""
    pantalla.fill('black')
    texto = fuente.render('Ayuda', True, 'white')
    pantalla.blit(texto, (300, 50))

    ayuda_texto = [
        "Controles:",
        "Jugador 1: A (izquierda), D (derecha), W (disparo)",
        "Jugador 2: Flecha Izquierda (izquierda), Flecha Derecha (derecha), Espacio (disparo)",
        "Presiona ESC para salir."
    ]

    for i, linea in enumerate(ayuda_texto):
        texto_linea = fuente.render(linea, True, 'white')
        pantalla.blit(texto_linea, (100, 100 + i * 30))

    pygame.display.flip()
    pygame.time.wait(3000)  # Espera 3 segundos antes de volver al menú
