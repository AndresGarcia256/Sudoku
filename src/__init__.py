# src/__init__.py
"""
Paquete principal del juego Sudoku 4x4
"""

# src/board/__init__.py
"""
Paquete para el manejo del tablero de Sudoku 4x4
"""
from src.board.board import Board
from src.board.visualization import BoardVisualizer

# src/game/__init__.py
"""
Paquete con la lógica principal del juego
"""
from src.game.game import Game
from src.game.difficulty import DifficultyManager
from src.game.scoring import ScoreManager

# src/menu/__init__.py
"""
Paquete para el manejo del menú y la interfaz de usuario
"""
from src.menu.menu import Menu

# src/utils/__init__.py
"""
Paquete con utilidades y herramientas para el juego
"""
from src.utils.constants import VISUALIZATION_TYPES, DIFFICULTY_LEVELS, HIGHSCORES_FILE
from src.utils.file_manager import FileManager