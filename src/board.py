"""
Módulo para la generación y manejo del tablero de Sudoku 4x4
"""

import random
import copy

class Board:
    """
    Clase que representa un tablero de Sudoku 4x4
    """
    def __init__(self):
        """
        Inicializa un tablero de Sudoku 4x4 vacío
        """
        # Matriz 4x4 inicializada con ceros (celdas vacías)
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        # Tablero original antes de eliminar celdas (para verificación)
        self.solution = None
        # Coordenadas de las celdas que están fijas desde el inicio
        self.fixed_cells = set()
    
    
        """
        Elimina celdas del tablero para crear el puzzle
        
        Args:
            num_cells (int): Número de celdas a vaciar
        """
        # Reiniciar las celdas fijas
        self.fixed_cells = set()
        
        # Lista de todas las posiciones del tablero
        positions = [(i, j) for i in range(4) for j in range(4)]
        
        # Barajar las posiciones
        random.shuffle(positions)
        
        # Seleccionar las celdas a eliminar
        for i, j in positions[:num_cells]:
            self.board[i][j] = 0
        
        # Registrar las celdas fijas (las que no se eliminaron)
        for i, j in positions[num_cells:]:
            self.fixed_cells.add((i, j))
    
    def is_valid_move(self, row, col, num):
        """
        Verifica si es válido colocar un número en una celda específica
        
        Args:
            row (int): Fila de la celda (0-3)
            col (int): Columna de la celda (0-3)
            num (int): Número a colocar (1-4)
            
        Returns:
            bool: True si el movimiento es válido, False en caso contrario
        """
        # Verificar fila
        for i in range(4):
            if self.board[row][i] == num:
                return False
                
        # Verificar columna
        for i in range(4):
            if self.board[i][col] == num:
                return False
        
        # Verificar región 2x2
        region_row, region_col = 2 * (row // 2), 2 * (col // 2)
        for i in range(region_row, region_row + 2):
            for j in range(region_col, region_col + 2):
                if self.board[i][j] == num:
                    return False
        
        return True
    
    def is_complete(self):
        """
        Verifica si el tablero está completo (sin celdas vacías)
        
        Returns:
            bool: True si está completo, False en caso contrario
        """
        for row in self.board:
            if 0 in row:
                return False
        return True
    
 
        """
        Verifica si el tablero actual es válido
        
        Returns:
            bool: True si el tablero es válido, False en caso contrario
        """
        # Verificar filas
        for row in self.board:
            if sorted(row) != [1, 2, 3, 4]:
                return False
        
        # Verificar columnas
        for col in range(4):
            column = [self.board[row][col] for row in range(4)]
            if sorted(column) != [1, 2, 3, 4]:
                return False
        
        # Verificar regiones 2x2
        for region_row in range(0, 4, 2):
            for region_col in range(0, 4, 2):
                region = []
                for i in range(region_row, region_row + 2):
                    for j in range(region_col, region_col + 2):
                        region.append(self.board[i][j])
                if sorted(region) != [1, 2, 3, 4]:
                    return False
        
        return True
    
    def is_valid(self):
        """
        Verifica si el tablero actual es válido
        
        Returns:
            bool: True si el tablero es válido, False en caso contrario
        """
        # Verificar filas
        for row in self.board:
            if sorted(row) != [1, 2, 3, 4]:
                return False
        
        # Verificar columnas
        for col in range(4):
            column = [self.board[row][col] for row in range(4)]
            if sorted(column) != [1, 2, 3, 4]:
                return False
        
        # Verificar regiones 2x2
        for region_row in range(0, 4, 2):
            for region_col in range(0, 4, 2):
                region = []
                for i in range(region_row, region_row + 2):
                    for j in range(region_col, region_col + 2):
                        region.append(self.board[i][j])
                if sorted(region) != [1, 2, 3, 4]:
                    return False
        
        return True
    
    def set_cell(self, row, col, value):
        """
        Establece un valor en una celda del tablero
        
        Args:
            row (int): Fila de la celda (0-3)
            col (int): Columna de la celda (0-3)
            value (int): Valor a colocar (1-4)
            
        Returns:
            bool: True si se pudo establecer el valor, False si la celda es fija
        """
        # No permitir modificar celdas fijas
        if (row, col) in self.fixed_cells:
            return False
        
        self.board[row][col] = value
        return True
    
    def get_cell(self, row, col):
        """
        Obtiene el valor de una celda
        
        Args:
            row (int): Fila de la celda (0-3)
            col (int): Columna de la celda (0-3)
            
        Returns:
            int: Valor de la celda (0 si está vacía)
        """
        return self.board[row][col]
    
    def is_cell_fixed(self, row, col):
        """
        Verifica si una celda es fija (no se puede modificar)
        
        Args:
            row (int): Fila de la celda (0-3)
            col (int): Columna de la celda (0-3)
            
        Returns:
            bool: True si la celda es fija, False en caso contrario
        """
        return (row, col) in self.fixed_cells