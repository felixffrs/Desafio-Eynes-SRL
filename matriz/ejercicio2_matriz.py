"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""

import random

def create_matriz(rows, columns):

    matriz = [[random.randint(1, 4) for r in range(rows)] for c in range(columns)]
    return matriz

def print_matriz(matriz):
    for row in matriz:
        print(row)

def search_consecutives(matriz, rows, columns):
    for row in range(rows):
        cont_horizontal = 0
        cont_vertical = 0
        consecutive_horizontal_positions = []
        consecutive_vertical_positions = []

        for col in range(columns):
            try:
                if matriz[row][col] - matriz[row][col + 1] == -1: #HORIZONTAL ASCENDENTE
                    cont_horizontal += 1
                    consecutive_horizontal_positions.append((row, col)) 
                else:
                    cont_horizontal = 0
                    consecutive_horizontal_positions = []
            except IndexError as e:
                if matriz[row][col] - matriz[row][col - 1] == 1:
                    cont_horizontal += 1
                    consecutive_horizontal_positions.append((row, col))
                else:
                    cont_horizontal = 0
                    consecutive_horizontal_positions = []
            finally:
                if cont_horizontal == 4:
                    print("Secuencia encontrada Horizontalmente")
                    print(f"Posicion Inicial: {consecutive_horizontal_positions[0]}, Posicion Final:{consecutive_horizontal_positions[-1]}")
                    break
            
            try:
                if matriz[col][row] - matriz[col + 1][row] == -1: #VERTICAL ASCENDENTE
                    cont_vertical += 1
                    consecutive_vertical_positions.append((col, row))
                else:
                    cont_vertical = 0
                    consecutive_vertical_positions = []
            except IndexError as e:
                if matriz[col][row] - matriz[col - 1][row] == 1:
                    cont_vertical += 1
                    consecutive_vertical_positions.append((col, row))
                else:
                    cont_vertical = 0
                    consecutive_vertical_positions = []
            finally:
                if cont_vertical == 4:
                    print("Secuencia encontrada Verticalmente") 
                    print(f"Posicion Inicial: {consecutive_vertical_positions[0]}, Posicion Final:{consecutive_vertical_positions[-1]}")
                    break             
        if cont_horizontal == 4 or cont_vertical == 4:
            break

if __name__ == "__main__":

    rows = 5
    columns = 5

    matriz = create_matriz(rows, columns)
    print_matriz(matriz)
    search_consecutives(matriz, rows, columns)