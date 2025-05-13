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
    
    def solve(self, row=0, col=0):
        """
        Resuelve el tablero de Sudoku utilizando backtracking
        
        Args:
            row (int): Fila actual (0-3)
            col (int): Columna actual (0-3)
            
        Returns:
            bool: True si se encontró una solución, False en caso contrario
        """
        # Si llegamos al final del tablero, hemos resuelto el Sudoku
        if row == 4:
            return True
        
        # Calcular la siguiente celda
        next_row, next_col = (row, col + 1) if col < 3 else (row + 1, 0)
        
        # Si la celda ya tiene un valor, pasar a la siguiente
        if self.board[row][col] != 0:
            return self.solve(next_row, next_col)
        
        # Probar cada número del 1 al 4
        for num in range(1, 5):
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num
                
                # Continuar con la siguiente celda
                if self.solve(next_row, next_col):
                    return True
                
                # Si no se encontró solución, deshacer y probar otro número
                self.board[row][col] = 0
        
        # No se encontró solución
        return False
    
    def generate(self):
        """
        Genera un tablero de Sudoku 4x4 aleatorio y completo
        """
        # Partir de un tablero vacío
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        
        # Resolver para generar un tablero válido
        self.solve()
        
        # Guardar la solución completa
        self.solution = copy.deepcopy(self.board)
    
    def remove_cells(self, num_cells):
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