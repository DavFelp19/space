class GameState:
    def __init__(self):
        self.estado = "menu"
        self.modo = None
        self.puntuacion1 = 0
        self.puntuacion2 = 0
        self.vidas = 3
        self.dificultad = "FACIL"

    def reiniciar(self):
        self.puntuacion1 = 0
        self.puntuacion2 = 0
        self.vidas = 3 if self.modo == "individual" else 6

    def cambiar_dificultad(self):
        dificultades = ["FACIL", "MEDIO", "DIFICIL"]
        indice_actual = dificultades.index(self.dificultad)
        self.dificultad = dificultades[(indice_actual + 1) % len(dificultades)]