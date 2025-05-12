"""
Módulo principal del juego Sudoku 4x4
"""

import os
from src.board.board import Board
from src.board.visualization import BoardVisualizer

# Importación corregida de las constantes
from src.utils.constants import DIFFICULTY_LEVELS

class Game:
    """
    Clase principal que gestiona la lógica del juego
    """
    def __init__(self):
        """
        Inicializa el juego con configuración por defecto
        """
        self.board = None
        self.difficulty = DIFFICULTY_LEVELS["EASY"]  # Dificultad por defecto
    
    def clear_screen(self):
        """
        Limpia la pantalla de la consola según el sistema operativo
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def set_difficulty(self, difficulty_key):
        """
        Establece la dificultad del juego
        
        Args:
            difficulty_key (str): Clave de la dificultad ("EASY" o "HARD")
        """
        if difficulty_key in DIFFICULTY_LEVELS:
            self.difficulty = DIFFICULTY_LEVELS[difficulty_key]
    
    def generate_board(self):
        """
        Genera un nuevo tablero de Sudoku según la dificultad actual
        """
        self.board = Board()
        self.board.generate()  # Generar tablero completo
        self.board.remove_cells(self.difficulty["empty_cells"])  # Eliminar celdas según dificultad
    
    def play(self, visualization_type):
        """
        Inicia un juego de Sudoku
        
        Args:
            visualization_type (dict): Tipo de visualización seleccionado
            
        Returns:
            bool: True si se resolvió correctamente, False en caso contrario
        """
        self.clear_screen()
        self.generate_board()
        visualizer = BoardVisualizer(self.board, visualization_type, self.difficulty)
        
        print(f"\n=== SUDOKU 4x4 - Nivel {self.difficulty['name']} ===")
        print("Instrucciones:")
        print("- Complete el tablero según las reglas del Sudoku")
        print("- Para salir del juego, escriba 'salir' o 'exit'")
        print(visualizer.get_input_format_help())
        
        # Bucle principal del juego
        while not self.board.is_complete():
            visualizer.display()
            
            # Obtener entrada del usuario
            user_input = input("\nIngrese jugada (o 'salir'): ").strip()
            
            # Verificar si el usuario quiere salir
            if user_input.lower() in ["salir", "exit"]:
                return False
            
            # Procesar la entrada del usuario
            parts = user_input.split()
            if len(parts) != 3:
                print("Formato inválido. Intente nuevamente.")
                input("Presione Enter para continuar...")
                self.clear_screen()
                continue
            
            try:
                # Convertir coordenadas a índices de matriz (0-3)
                row = int(parts[0]) - 1
                col = int(parts[1]) - 1
                
                # Validar rango
                if not (0 <= row < 4 and 0 <= col < 4):
                    raise ValueError("Coordenadas fuera de rango")
                
                # Convertir valor según el tipo de visualización
                value = visualizer.convert_input_value(parts[2])
                
                if value is None or not (1 <= value <= 4):
                    raise ValueError("Valor inválido")
                
                # Intentar establecer el valor en el tablero
                if not self.board.set_cell(row, col, value):
                    print("No se puede modificar una celda fija")
                    input("Presione Enter para continuar...")
                
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione Enter para continuar...")
            
            self.clear_screen()
        
        # El tablero está completo, verificar si es correcto
        visualizer.display()
        
        if self.board.is_valid():
            print("\n¡Felicidades! Has resuelto el Sudoku correctamente.")
            return True
        else:
            print("\nEl Sudoku está completo pero contiene errores.")
            return False