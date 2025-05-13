# tests/test_integration.py
"""
Tests de integración para el juego Sudoku 4x4
"""

import unittest
from src.board.board import Board
from src.utils.constants import VISUALIZATION_TYPES, DIFFICULTY_LEVELS
from src.board.visualization import BoardVisualizer

class TestIntegration(unittest.TestCase):
    """
    Clase para tests de integración
    """
    
    def test_board_generation_and_validation(self):
        """
        Prueba la generación y validación del tablero
        """
        board = Board()
        board.generate()
        
        # Verificar que el tablero generado es válido
        self.assertTrue(board.is_valid())
        
        # Verificar que el tablero está completo
        self.assertTrue(board.is_complete())
        
        # Modificar una celda y verificar que sigue siendo válido
        original_value = board.board[0][0]
        board.board[0][0] = 0
        self.assertFalse(board.is_complete())
        
        # Restaurar y verificar
        board.board[0][0] = original_value
        self.assertTrue(board.is_complete())
    
    def test_visualization_format_conversion(self):
        """
        Prueba la conversión entre formatos de visualización
        """
        board = Board()
        board.generate()
        
        # Probar visualización numérica
        viz_numeric = BoardVisualizer(board, VISUALIZATION_TYPES["NUMERIC"], DIFFICULTY_LEVELS["EASY"])
        self.assertEqual(viz_numeric.convert_value(1), "1")
        self.assertEqual(viz_numeric.convert_value(4), "4")
        
        # Probar visualización con letras
        viz_letters = BoardVisualizer(board, VISUALIZATION_TYPES["LETTERS"], DIFFICULTY_LEVELS["EASY"])
        self.assertEqual(viz_letters.convert_value(1), "A")
        self.assertEqual(viz_letters.convert_value(4), "D")
        
        # Probar visualización con símbolos
                viz_symbols = BoardVisualizer(board, VISUALIZATION_TYPES["SYMBOLS"], DIFFICULTY_LEVELS["EASY"])
        self.assertEqual(viz_symbols.convert_value(1), "♠")
        self.assertEqual(viz_symbols.convert_value(4), "♣")
        
        # Probar conversión de entrada
        self.assertEqual(viz_numeric.convert_input_value("2"), 2)
        self.assertEqual(viz_letters.convert_input_value("C"), 3)
        self.assertEqual(viz_symbols.convert_input_value("♥"), 2)
        
        # Probar entrada inválida
        self.assertIsNone(viz_numeric.convert_input_value("X"))
        self.assertIsNone(viz_letters.convert_input_value("Z"))
        self.assertIsNone(viz_symbols.convert_input_value("?"))

if __name__ == "__main__":
    unittest.main()