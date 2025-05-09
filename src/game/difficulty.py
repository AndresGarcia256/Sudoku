"""
Módulo para gestionar los niveles de dificultad del juego Sudoku 4x4
"""

from src.utils.constants import DIFFICULTY_LEVELS

class DifficultyManager:
    """
    Clase para manejar los niveles de dificultad del juego
    """
    def __init__(self):
        """
        Inicializa el gestor de dificultad con el nivel fácil por defecto
        """
        self.current_difficulty = "EASY"
    
    def get_difficulty(self):
        """
        Obtiene la configuración de dificultad actual
        
        Returns:
            dict: Diccionario con la configuración de dificultad
        """
        return DIFFICULTY_LEVELS[self.current_difficulty]
    
    def set_difficulty(self, difficulty_key):
        """
        Establece un nuevo nivel de dificultad
        
        Args:
            difficulty_key (str): Clave del nivel de dificultad ("EASY" o "HARD")
            
        Returns:
            bool: True si se cambió la dificultad, False si la clave es inválida
        """
        if difficulty_key in DIFFICULTY_LEVELS:
            self.current_difficulty = difficulty_key
            return True
        return False
    
    def get_difficulty_name(self):
        """
        Obtiene el nombre del nivel de dificultad actual
        
        Returns:
            str: Nombre del nivel de dificultad
        """
        return DIFFICULTY_LEVELS[self.current_difficulty]["name"]
    
    def get_empty_cells_count(self):
        """
        Obtiene el número de celdas vacías según el nivel de dificultad
        
        Returns:
            int: Número de celdas vacías
        """
        return DIFFICULTY_LEVELS[self.current_difficulty]["empty_cells"]
    
    def get_border_char(self):
        """
        Obtiene el carácter de borde según el nivel de dificultad
        
        Returns:
            str: Carácter de borde
        """
        return DIFFICULTY_LEVELS[self.current_difficulty]["border"]