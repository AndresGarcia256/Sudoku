"""
Módulo para gestionar el sistema de puntuación del juego Sudoku 4x4
"""

class ScoreManager:
    """
    Clase para manejar el sistema de puntuación del juego
    """
    def __init__(self):
        """
        Inicializa el gestor de puntuación
        """
        self.current_score = 0
        self.consecutive_wins = 0
    
    def add_win(self):
        """
        Incrementa la puntuación al ganar un tablero
        Otorga 10 puntos base más un bono exponencial según la racha
        """
        # Puntuación base por resolver el tablero
        base_points = 10
        
        # Calcular puntos adicionales según racha
        # La fórmula es 2^(racha-1) - 1, que da 0, 1, 3, 7, 15... para rachas de 1, 2, 3, 4, 5...
        bonus_points = (2 ** self.consecutive_wins - 1) if self.consecutive_wins > 0 else 0
        
        # Incrementar la puntuación
        self.current_score += base_points + bonus_points
        
        # Incrementar la racha de victorias
        self.consecutive_wins += 1
        
        return base_points, bonus_points
    
    def reset_streak(self):
        """
        Reinicia la racha de victorias consecutivas al perder
        """
        self.consecutive_wins = 0
    
    def get_score(self):
        """
        Obtiene la puntuación actual
        
        Returns:
            int: Puntuación actual
        """
        return self.current_score
    
    def get_consecutive_wins(self):
        """
        Obtiene el número de victorias consecutivas
        
        Returns:
            int: Número de victorias consecutivas
        """
        return self.consecutive_wins
    
    def calculate_next_win_points(self):
        """
        Calcula cuántos puntos se obtendrían con la siguiente victoria
        
        Returns:
            int: Puntos que se obtendrían con la siguiente victoria
        """
        base_points = 10
        future_bonus = (2 ** self.consecutive_wins - 1) if self.consecutive_wins > 0 else 0
        return base_points + future_bonus