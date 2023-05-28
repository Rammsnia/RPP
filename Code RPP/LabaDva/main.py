import numpy as np

def generate_matrix(N, M):
    """
    Генерирует матрицу случайных нулей и единиц размера N на M
    """
    return np.random.randint(2, size=(N, M))

def add_even_column(matrix):
    """
    Добавляет к матрице еще один столбец, каждый элемент которого делает количество единиц в каждой строке чётным.
    """
    even_count = np.sum(matrix, axis=1) % 2 == 1
    return np.column_stack((matrix, even_count))

def save_matrix(matrix, file_name):
    """
    Сохраняет матрицу в файл.
    """
    with open(file_name, "w") as f:
        np.savetxt(f, matrix, fmt="%d")

# Генерируем матрицу
N = int(input("Введите высоту: "))
M = int(input("Введите ширину матрицы: "))
matrix = generate_matrix(N, M)
print("Исходная матрица:")
print(matrix)

# Добавляем столбец с четным количеством единиц в каждой строке
matrix_with_even_column = add_even_column(matrix)
print("Матрица с дополнительным столбцом:")
print(matrix_with_even_column)

# Сохраняем матрицу в файл
file_name = "matrix.txt"
save_matrix(matrix_with_even_column, file_name)
print(f"Результат сохранен в файл {file_name}.")