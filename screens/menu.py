import pygame

def mostrar_menu(pantalla, fuente, game_state):
    pantalla.fill('black')
    menu_texto = [
        'Space Invaders',
        '1 - Modo Individual',
        '2 - Modo Multijugador',
        f'3 - Dificultad: {game_state.dificultad}',
        '4 - Ver High Scores',
        '5 - Ayuda',
        '6 - Salir'
    ]

    for i, linea in enumerate(menu_texto):
        texto = fuente.render(linea, True, 'white')
        pantalla.blit(texto, (100, 50 + i * 50))

    pygame.display.flip()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_state.estado = "juego"
                    game_state.modo = "individual"
                    game_state.reiniciar()
                    esperando = False
                elif event.key == pygame.K_2:
                    game_state.estado = "juego"
                    game_state.modo = "multijugador"
                    game_state.reiniciar()
                    esperando = False
                elif event.key == pygame.K_3:
                    game_state.cambiar_dificultad()
                    return  # Volver a mostrar el menú con la nueva dificultad
                elif event.key == pygame.K_4:
                    game_state.estado = "highscores"
                    esperando = False
                elif event.key == pygame.K_5:
                    game_state.estado = "ayuda"
                    esperando = False
                elif event.key == pygame.K_6:
                    pygame.quit()
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                return