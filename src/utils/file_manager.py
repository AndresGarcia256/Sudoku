"""
Módulo para la gestión de archivos del juego Sudoku 4x4
"""

import os
import json
from src.utils.constants import HIGHSCORES_FILE

class FileManager:
    """
    Clase para manejar la lectura y escritura de archivos
    """
    def __init__(self):
        """
        Inicializa el gestor de archivos y asegura que la estructura de directorios exista
        """
        # Crear el directorio de datos si no existe
        data_dir = os.path.dirname(HIGHSCORES_FILE)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        # Crear el archivo de mejores puntajes si no existe
        if not os.path.exists(HIGHSCORES_FILE):
            self.save_highscores([])
    
    def load_highscores(self):
        """
        Carga los mejores puntajes desde el archivo
        
        Returns:
            list: Lista de diccionarios con los mejores puntajes
        """
        try:
            with open(HIGHSCORES_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o está corrupto, crear uno nuevo
            self.save_highscores([])
            return []
    
    def save_highscores(self, highscores):
        """
        Guarda la lista de mejores puntajes en el archivo
        
        Args:
            highscores (list): Lista de diccionarios con los mejores puntajes
        """
        with open(HIGHSCORES_FILE, 'w', encoding='utf-8') as file:
            json.dump(highscores, file, indent=4)
    
    def save_highscore(self, name, score):
        """
        Añade un nuevo puntaje a la lista de mejores puntajes
        
        Args:
            name (str): Nombre del jugador
            score (int): Puntaje obtenido
        """
        highscores = self.load_highscores()
        
        # Añadir el nuevo puntaje
        highscores.append({
            "name": name,
            "score": score
        })
        
        # Ordenar por puntaje de mayor a menor
        highscores = sorted(highscores, key=lambda x: x["score"], reverse=True)
        
        # Mantener solo los 5 mejores puntajes
        highscores = highscores[:5]
        
        # Guardar la lista actualizada
        self.save_highscores(highscores)