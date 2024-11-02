import pygame
import sys
from screens import menu, game, victory, defeat, highscores, help
from game_state import GameState

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Space Invaders')
    fuente = pygame.font.Font(None, 36)
    game_state = GameState()
    high_scores = highscores.Highscores()
    high_scores.cargar_highscores()

    # Iniciar música de fondo
    pygame.mixer.music.load('sonidos/musica.wav')
    pygame.mixer.music.play(-1)  # -1 para reproducir en loop


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state.estado == "menu":
            menu.mostrar_menu(pantalla, fuente, game_state)
        elif game_state.estado == "juego":
            game.Juego(pantalla, game_state, fuente).jugar()
        elif game_state.estado == "victoria":
            high_scores.agregar_puntaje(game_state.puntuacion1)
            high_scores.guardar_highscores()
            victory.mostrar_pantalla_victoria(pantalla, fuente, game_state)
        elif game_state.estado == "derrota":
            high_scores.agregar_puntaje(game_state.puntuacion1)
            high_scores.guardar_highscores()
            defeat.mostrar_pantalla_derrota(pantalla, fuente, game_state)
        elif game_state.estado == "highscores":
            game_state.estado = high_scores.mostrar_highscores(pantalla, fuente)
        elif game_state.estado == "ayuda":
            game_state.estado = help.mostrar_ayuda(pantalla, fuente)

        # Solo actualiza la pantalla si no se ha cerrado el juego
        pygame.display.flip()

if __name__ == "__main__":
    main()