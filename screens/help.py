import pygame
import sys
def mostrar_ayuda(pantalla, fuente):
    pantalla.fill('black')
    texto_titulo = fuente.render('Ayuda', True, 'white')
    pantalla.blit(texto_titulo, (350, 50))

    instrucciones = [
        "Controles:",
        "Jugador 1: Flechas para moverse, Enter para disparar",
        "Jugador 2: A/D para moverse, Espacio para disparar",
        "Objetivo: Elimina a todos los aliens antes de que te eliminen",
        "Presiona cualquier tecla para volver al menú"
    ]

    for i, linea in enumerate(instrucciones):
        texto = fuente.render(linea, True, 'white')
        pantalla.blit(texto, (50, 100 + i * 40))

    pygame.display.flip()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return "menu"  # Retorna al menú cuando se presiona una tecla
            if event.type == pygame.MOUSEBUTTONDOWN:
                return "menu"  # Retorna al menú cuando se hace clic