# README.md
# Sudoku 4x4

Una aplicación de consola en Python para jugar Sudoku en una versión de tablero 4x4.

## Descripción

Este proyecto implementa un juego de Sudoku 4x4 que se ejecuta en la consola. El juego incluye:

- Diferentes niveles de dificultad (Fácil y Difícil)
- Múltiples opciones de visualización (Numérica, Letras y Símbolos)
- Sistema de puntuación con bonificación por rachas
- Registro de mejores puntajes

## Requisitos

- Python 3.6 o superior

## Cómo jugar

1. Ejecute el juego con Python:
2. Siga las instrucciones en pantalla:
- Seleccione el tipo de visualización
- Elija el nivel de dificultad
- Complete los tableros para acumular puntos

3. Controles:
- Para colocar un valor, ingrese fila, columna y valor separados por espacio
- Ejemplo: `2 3 4` (coloca el valor 4 en la fila 2, columna 3)
- Para salir de una partida, escriba "salir" o "exit"

## Reglas del Sudoku 4x4

- Se deben completar los cuadros vacíos con un solo número del 1 al 4
- En una fila no puede haber números repetidos
- En una columna no puede haber números repetidos
- En una región (cuadrado 2x2) no puede haber números repetidos

## Desarrollo

Este proyecto fue desarrollado por nuestro equipo usando la metodología Scrum:

- Ana: Encargada de la visualización, menú y sistema de puntuación
- Carlos: Responsable de la lógica del tablero y gestión de archivos
- María: Coordinación, integración y documentación

## Licencia

Este proyecto está bajo licencia MIT.
sudoku/
├── README.md
├── main.py
├── src/
│   ├── __init__.py
│   ├── board/
│   │   ├── board.py          # Lógica y manejo del tablero (T-03, T-04, T-06)
│   │   └── visualization.py  # Visualización del tablero (T-05)
│   ├── game/
│   │   ├── difficulty.py     # Sistema de dificultad (T-07)
│   │   ├── game.py           # Lógica de juego (T-08)
│   │   └── scoring.py        # Sistema de puntuación (T-10)
│   ├── menu/
│   │   └── menu.py           # Menú principal (T-09, T-12)
│   └── utils/
│       ├── __init__.py
│       ├── constants.py      # Constantes y configuración (T-02)
│       └── file_manager.py   # Gestión de archivos (T-11)
├── tests/
│   └── test_integration.py  # Pruebas de integración (T-14)
└── data/
    └── highscores.json      # Archivo de mejores puntajes