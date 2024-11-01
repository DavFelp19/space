class GameState:
    """Clase que mantiene el estado del juego."""
    def __init__(self):
        self.estado = "menu"  # Estado inicial del juego
        self.modo = None  # Modo de juego (individual o multijugador)
        self.puntuacion1 = 0  # Puntuación del jugador 1
        self.puntuacion2 = 0  # Puntuación del jugador 2
        self.vidas1 = 3  # Vidas del jugador 1
        self.vidas2 = 3  # Vidas del jugador 2

    def reiniciar(self):
        """Reinicia el estado del juego a sus valores iniciales."""
        self.estado = "menu"
        self.modo = None
        self.puntuacion1 = 0
        self.puntuacion2 = 0
        self.vidas1 = 3
        self.vidas2 = 3