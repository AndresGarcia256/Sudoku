"""
Módulo para la visualización del tablero de Sudoku 4x4
"""

class BoardVisualizer:
    """
    Clase para visualizar el tablero de Sudoku en diferentes formatos
    """
    def __init__(self, board, visualization_type, difficulty):
        """
        Inicializa el visualizador con el tablero y tipo de visualización
        
        Args:
            board: Objeto Board que se va a visualizar
            visualization_type: Diccionario con el tipo de visualización
            difficulty: Diccionario con la configuración de dificultad
        """
        self.board = board
        self.viz_type = visualization_type
        self.border_char = difficulty["border"]
    
    def convert_value(self, value):
        """
        Convierte un valor numérico al formato de visualización seleccionado
        
        Args:
            value (int): Valor numérico (0-4)
            
        Returns:
            str: Valor convertido según el tipo de visualización
        """
        if value == 0:
            return " "
        
        # Restar 1 porque los arrays están indexados desde 0
        return self.viz_type["values"][value - 1]
    
    def display(self):
        """
        Muestra el tablero en la consola con el formato seleccionado
        """
        border_line = f"{self.border_char * 17}"
        
        print(f"\nTipo de visualización: {self.viz_type['type']}")
        print(border_line)
        
        for i in range(4):
            row_values = []
            
            for j in range(4):
                value = self.board.get_cell(i, j)
                display_value = self.convert_value(value)
                
                # Destacar celdas fijas con corchetes
                if self.board.is_cell_fixed(i, j) and value != 0:
                    display_value = f"[{display_value}]"
                else:
                    display_value = f" {display_value} "
                
                row_values.append(display_value)
            
            # Dibujar la línea con los valores
            print(f"{self.border_char} {' | '.join(row_values)} {self.border_char}")
            
            # Dibujar línea divisoria entre regiones 2x2 o al final
            if i == 1:
                print(f"{self.border_char}-------+-------{self.border_char}")
            else:
                print(border_line)
    
    def get_input_format_help(self):
        """
        Devuelve instrucciones sobre el formato de entrada
        
        Returns:
            str: Mensaje con instrucciones de formato
        """
        values_list = ', '.join(self.viz_type["values"])
        return f"Ingrese fila (1-4), columna (1-4) y valor ({values_list}) separados por espacio, ejemplo: 1 3 {self.viz_type['values'][0]}"
    
    def convert_input_value(self, value_str):
        """
        Convierte un valor de entrada al formato numérico del tablero
        
        Args:
            value_str (str): Valor en el formato de visualización
            
        Returns:
            int: Valor numérico correspondiente (1-4), o None si no es válido
        """
        try:
            # Si es numérico, convertir directamente
            if self.viz_type["type"] == "Numérico":
                return int(value_str)
            
            # Buscar el índice del valor en la lista y sumar 1
            return self.viz_type["values"].index(value_str) + 1
        except (ValueError, IndexError):
            return None