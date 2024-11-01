import pygame

def mostrar_ayuda(pantalla, fuente):
    pantalla.fill('black')
    texto_titulo = fuente.render('Ayuda', True, 'white')
    pantalla.blit(texto_titulo, (350, 50))

    instrucciones = [
        "Controles:",
        "Jugador 1: Flechas izquierda/derecha para moverse, Enter para disparar",
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
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                esperando = False
            if event.type == pygame.QUIT:
                pygame.quit()
                return