"""
Constantes utilizadas en el juego Sudoku 4x4
"""

# Tipo de visualización del tablero
VISUALIZATION_TYPES = {
    "NUMERIC": {
        "type": "Numérico",
        "values": ["1", "2", "3", "4"]
    },
    "LETTERS": {
        "type": "Letras",
        "values": ["A", "B", "C", "D"]
    },
    "SYMBOLS": {
        "type": "Símbolos",
        "values": ["♠", "♥", "♦", "♣"]
    }
}

# Niveles de dificultad
DIFFICULTY_LEVELS = {
    "EASY": {
        "name": "Fácil",
        "empty_cells": 6,
        "border": "*"
    },
    "HARD": {
        "name": "Difícil",
        "empty_cells": 10,
        "border": "-"
    }
}

# Ruta al archivo de mejores puntajes
HIGHSCORES_FILE = "data/highscores.json"