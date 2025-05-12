"""
Módulo de menú para el juego Sudoku 4x4
Gestiona la interacción con el usuario
"""

import os
from src.game.game import Game
from src.utils.constants import VISUALIZATION_TYPES
from src.utils.file_manager import FileManager

class Menu:
    """
    Clase que maneja el menú principal y la interacción con el usuario
    """
    def __init__(self):
        """
        Inicializa el menú con los valores por defecto
        """
        self.running = True
        self.game = Game()
        self.file_manager = FileManager()
        self.current_score = 0
        self.consecutive_wins = 0
    
    def clear_screen(self):
        """
        Limpia la pantalla de la consola según el sistema operativo
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        """
        Muestra el menú principal del juego
        """
        self.clear_screen()
        print("\n===== SUDOKU 4x4 =====")
        print("1. Jugar Sudoku")
        print("2. Seleccionar nivel de dificultad")
        print("3. Mejores puntajes")
        print("4. Salir")
        print(f"\nPuntaje actual: {self.current_score}")
        print(f"Victorias consecutivas: {self.consecutive_wins}")
        print("======================")
    
    def select_visualization(self):
        """
        Permite al usuario seleccionar el tipo de visualización para el tablero
        """
        self.clear_screen()
        print("\n== Seleccione tipo de visualización ==")
        print("1. Numérico (1-4)")
        print("2. Letras (A-D)")
        print("3. Símbolos (♠,♥,♦,♣)")
        
        choice = input("\nSeleccione una opción (1-3): ")
        
        if choice == "1":
            return VISUALIZATION_TYPES["NUMERIC"]
        elif choice == "2":
            return VISUALIZATION_TYPES["LETTERS"]
        elif choice == "3":
            return VISUALIZATION_TYPES["SYMBOLS"]
        else:
            print("\nOpción no válida. Se usará el modo numérico por defecto.")
            return VISUALIZATION_TYPES["NUMERIC"]
    
    def play_game(self):
        """
        Inicia un nuevo juego de Sudoku
        """
        viz_type = self.select_visualization()
        
        # Iniciar el juego con el tipo de visualización seleccionado
        result = self.game.play(viz_type)
        
        # Actualizar puntuación según resultado
        if result:
            self.consecutive_wins += 1
            self.current_score += 10 + (2 ** (self.consecutive_wins - 1) - 1)
            print(f"\n¡Felicidades! Tablero resuelto correctamente.")
            print(f"Puntaje actual: {self.current_score}")
            print(f"Victorias consecutivas: {self.consecutive_wins}")
        else:
            print("\nEl tablero no se resolvió correctamente.")
            print("Se ha reiniciado tu racha de victorias consecutivas.")
            self.consecutive_wins = 0
        
        input("\nPresione Enter para continuar...")
    
    def show_highscores(self):
        """
        Muestra la lista de mejores puntajes
        """
        self.clear_screen()
        print("\n==== MEJORES PUNTAJES ====")
        
        highscores = self.file_manager.load_highscores()
        
        if not highscores:
            print("No hay puntajes registrados aún.")
        else:
            # Ordenar por puntaje de mayor a menor
            sorted_scores = sorted(highscores, key=lambda x: x["score"], reverse=True)
            
            for i, score in enumerate(sorted_scores, 1):
                print(f"{i}. {score['name']}: {score['score']} puntos")
        
        input("\nPresione Enter para volver al menú principal...")
    
    def select_difficulty(self):
        """
        Permite al usuario seleccionar el nivel de dificultad
        """
        self.clear_screen()
        print("\n==== NIVEL DE DIFICULTAD ====")
        print("1. Fácil (6 casillas vacías)")
        print("2. Difícil (10 casillas vacías)")
        
        choice = input("\nSeleccione dificultad (1-2): ")
        
        if choice == "1":
            self.game.set_difficulty("EASY")
            print("\nNivel de dificultad establecido a: Fácil")
        elif choice == "2":
            self.game.set_difficulty("HARD")
            print("\nNivel de dificultad establecido a: Difícil")
        else:
            print("\nOpción no válida. Se mantendrá la dificultad actual.")
        
        input("\nPresione Enter para volver al menú principal...")
    
    def exit_game(self):
        """
        Finaliza el juego y guarda el puntaje si es necesario
        """
        self.clear_screen()
        
        # Verificar si el puntaje actual supera alguno de los mejores puntajes
        highscores = self.file_manager.load_highscores()
        
        if not highscores or min([score["score"] for score in highscores], default=0) < self.current_score or len(highscores) < 5:
            if self.current_score > 0:
                print("\n¡Felicidades! Has obtenido un puntaje alto.")
                name = input("Ingresa tu nombre para guardar el puntaje: ")
                
                # Guardar el nuevo puntaje
                self.file_manager.save_highscore(name, self.current_score)
                print(f"\nPuntaje guardado: {name} - {self.current_score} puntos")
        
        print("\n¡Gracias por jugar Sudoku 4x4!")
        self.running = False
    
    def start(self):
        """
        Inicia el menú principal y maneja la interacción con el usuario
        """
        while self.running:
            self.display_menu()
            choice = input("\nSeleccione una opción (1-4): ")
            
            if choice == "1":
                self.play_game()
            elif choice == "2":
                self.select_difficulty()
            elif choice == "3":
                self.show_highscores()
            elif choice == "4":
                self.exit_game()
            else:
                print("\nOpción no válida. Inténtelo de nuevo.")
                input("Presione Enter para continuar...")