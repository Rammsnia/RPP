import numpy as np


# Генерирует матрицу случайных нулей и единиц размера N на M


def generate_matrix(n, m):
    return np.random.randint(2, size=(N, M))

# Добавляет к матрице еще один столбец, каждый элемент которого делает количество единиц в каждой строке чётным.


def add_even_column(matrix):
    even_count = np.sum(matrix, axis=1) % 2 == 1
    return np.column_stack((matrix, even_count))

# Сохраняет матрицу в файл.


def save_matrix(matrix, file_name):
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
file_name_two = "matrix_first.txt"
file_name = "matrix_result.txt"
save_matrix(matrix, file_name_two)
save_matrix(matrix_with_even_column, file_name)
print(f"Результат сохранен в файл {file_name}.")