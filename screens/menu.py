import pygame

def mostrar_menu(pantalla, fuente, game_state):
    pantalla.fill('black')
    menu_texto = [
        'Presiona 1 para jugar en modo individual',
        'Presiona 2 para jugar en modo multijugador',
        'Presiona 3 para ver los high scores',
        'Presiona 4 para ver la ayuda',
        'Presiona 5 para salir'
    ]

    for i, linea in enumerate(menu_texto):
        texto = fuente.render(linea, True, 'white')
        pantalla.blit(texto, (100, 50 + i * 30))

    pygame.display.flip()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_state.estado = "juego"
                    game_state.modo = "individual"
                    esperando = False
                elif event.key == pygame.K_2:
                    game_state.estado = "juego"
                    game_state.modo = "multijugador"
                    esperando = False
                elif event.key == pygame.K_3:
                    game_state.estado = "highscores"
                    esperando = False
                elif event.key == pygame.K_4:
                    game_state.estado = "ayuda"
                    esperando = False
                elif event.key == pygame.K_5:
                    pygame.quit()
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                return
