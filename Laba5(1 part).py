#Задание состоит из двух частей.
#1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую
#функцию для нахождения оптимального  решения.
#Вариант 22. Дана квадратная матрица. Сформировать все возможные варианты данной
#матрицы путем перестановки строк и столбцов, в которых диагональные элементы равны нулю.

#1 часть

import itertools
import timeit

def generate_matrices_algorithmic(matrix):
    #Генерирует перестановки строк и столбцов матрицы
    n = len(matrix)
    row_permutations = list(itertools.permutations(range(n)))
    col_permutations = list(itertools.permutations(range(n)))

    matrices = []
    for row_perm in row_permutations:
        for col_perm in col_permutations:
            new_matrix = [[0] * n for _ in range(n)] # Создаем новую матрицу (список списков)
            for i in range(n):
                for j in range(n):
                    new_matrix[i][j] = matrix[row_perm[i]][col_perm[j]]
            matrices.append(new_matrix)
    return matrices

def generate_matrices_pythonic(matrix):
    #Генерирует перестановки строк и столбцов матрицы, используя срезы списков
    n = len(matrix)
    row_permutations = list(itertools.permutations(range(n)))
    col_permutations = list(itertools.permutations(range(n)))

    matrices = []
    for row_perm in row_permutations:
        for col_perm in col_permutations:
            new_matrix = []
            for i in row_perm:
                row = []
                for j in col_perm:
                    row.append(matrix[i][j])
                new_matrix.append(row)
            matrices.append(new_matrix)
    return matrices

def find_zero_diagonal_matrices(matrices):
   #Находит матрицы с нулевой диагональю
    zero_diagonal_matrices = []
    for matrix in matrices:
        trace = 0
        for i in range(len(matrix)):
            trace += matrix[i][i]
        if trace == 0:
            zero_diagonal_matrices.append(matrix)
    return zero_diagonal_matrices

matrix = [
        [0, 2, 3, 1],
        [7, 0, 8, 4],
        [6, 9, 0, 2],
        [1, 3, 4, 0]
    ]

# Замер времени для алгоритмического способа
matrices_algorithmic = generate_matrices_algorithmic(matrix)
zero_diagonal_matrices_algorithmic = find_zero_diagonal_matrices(matrices_algorithmic)
alg_time=timeit.timeit(lambda: find_zero_diagonal_matrices(generate_matrices_algorithmic(matrix)), number=10)
print(f"Алгоритмический способ: {alg_time:.4f} сек")
print("Матрицы с нулевой диагональю (алгоритмический способ):")
print(f"Количество матриц: {len(zero_diagonal_matrices_algorithmic)}")
for mat in zero_diagonal_matrices_algorithmic:
    for i in mat:
        print(i)
    print()

# Замер времени для способа с использованием NumPy
matrices_pythonic = generate_matrices_pythonic(matrix)
zero_diagonal_matrices_pythonic = find_zero_diagonal_matrices(matrices_pythonic)
it_time=timeit.timeit(lambda: find_zero_diagonal_matrices(generate_matrices_pythonic(matrix)), number=10)
print(f"Itertools способ: {it_time:.4f} сек")
print("Матрицы с нулевой диагональю (Itertools способ):")
print(f"Количество матриц: {len(zero_diagonal_matrices_pythonic)}")
for mat in zero_diagonal_matrices_pythonic:
    for i in mat:
        print(i)
    print()

