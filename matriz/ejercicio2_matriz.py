"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""

import random

def create_matriz(rows, columns):

    matriz = [[random.randint(1, 100) for r in range(rows)] for c in range(columns)]
    return matriz

def print_matriz(matriz):
    for row in matriz:
        print(row)

def search_consecutives(matriz, rows, columns):
    """
    Test searh_consecutives
    >>> matriz = [[1, 2, 44, 4, 6], [2, 3, 4, 5, 5], [3, 4, 4, 4, 4], [4, 8, 8, 8, 8], [52, 1, 1, 1, 1]]
    >>> search_consecutives(matriz, 5, 5)
    Secuencia encontrada Verticalmente
    Posicion Inicial: (0, 0), Posicion Final:(3, 0)
    >>> matriz = [[1, 22, 33, 4, 6], [5, 5, 5, 5, 5], [4, 4, 4, 4, 4], [8, 8, 8, 8, 8], [6, 7, 8, 9, 1]]
    >>> search_consecutives(matriz, 5, 5)
    Secuencia encontrada Horizontalmente
    Posicion Inicial: (4, 0), Posicion Final:(4, 3)
    """
    for row in range(rows):
        cont_horizontal = 0
        cont_vertical = 0
        consecutive_horizontal_positions = []
        consecutive_vertical_positions = []

        for col in range(columns):
            try:
                if cont_horizontal < 3 and matriz[row][col] - matriz[row][col + 1] == -1: #HORIZONTAL ASCENDENTE
                    cont_horizontal += 1
                    consecutive_horizontal_positions.append((row, col)) 
                elif cont_horizontal == 3 and matriz[row][col] - matriz[row][col - 1] == 1:
                    cont_horizontal += 1
                    consecutive_horizontal_positions.append((row, col))
            except IndexError as e:
                if matriz[row][col] - matriz[row][col - 1] == 1:
                    cont_horizontal += 1
                    consecutive_horizontal_positions.append((row, col))
            finally:
                if cont_horizontal == 4:
                    print("Secuencia encontrada Horizontalmente")
                    print(f"Posicion Inicial: {consecutive_horizontal_positions[0]}, Posicion Final:{consecutive_horizontal_positions[-1]}")
                    break
            try:
                if cont_vertical < 3 and matriz[col][row] - matriz[col + 1][row] == -1: #VERTICAL ASCENDENTE
                    cont_vertical += 1
                    consecutive_vertical_positions.append((col, row))
                elif cont_vertical == 3 and matriz[col][row] - matriz[col - 1][row] == 1:
                    cont_vertical += 1
                    consecutive_vertical_positions.append((col, row))
            except IndexError as e:
                if matriz[col][row] - matriz[col - 1][row] == 1:
                    cont_vertical += 1
                    consecutive_vertical_positions.append((col, row))
            finally:
                if cont_vertical == 4:
                    print("Secuencia encontrada Verticalmente") 
                    print(f"Posicion Inicial: {consecutive_vertical_positions[0]}, Posicion Final:{consecutive_vertical_positions[-1]}")
                    break
        if cont_horizontal == 4 or cont_vertical == 4:
            break
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
