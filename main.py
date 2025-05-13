
"""
Sudoku 4x4 - Juego de consola en Python
Archivo principal que inicia la aplicación
"""

from src.menu.menu import Menu

def main():
    """
    Función principal que inicia el juego
    """
    print("\n¡Bienvenido al juego de Sudoku 4x4!\n")
    
    # Crear e iniciar el menú principal
    menu = Menu()
    menu.start()

if __name__ == "__main__":
    main()