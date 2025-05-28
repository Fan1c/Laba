#Задание состоит из двух частей. 
#1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую
#функцию для нахождения оптимального  решения.
#Вариант 22. Дана квадратная матрица. Сформировать все возможные варианты данной 
#матрицы путем перестановки строк и столбцов, в которых диагональный элемент равен нулю.

#1 часть 

import numpy as np
import itertools
import time

def generate_matrices_algorithmic(matrix):
    #Генерация перестановок строк и столбцов алгоритмическим способом
    n = len(matrix)
    row_permutations = list(itertools.permutations(range(n)))
    col_permutations = list(itertools.permutations(range(n)))

    matrices = []
    for row_perm in row_permutations:
        for col_perm in col_permutations:
            new_matrix = np.zeros_like(matrix)
            for i in range(n):
                for j in range(n):
                    new_matrix[i, j] = matrix[row_perm[i], col_perm[j]]
            matrices.append(new_matrix)
    return matrices

def generate_matrices_pythonic(matrix):
    #Генерация перестановок строк и столбцов с использованием NumPy
    n = len(matrix)
    row_permutations = list(itertools.permutations(range(n)))
    col_permutations = list(itertools.permutations(range(n)))

    matrices = []
    for row_perm in row_permutations:
        for col_perm in col_permutations:
            new_matrix = matrix[np.ix_(list(row_perm), list(col_perm))]
            matrices.append(new_matrix)
    return matrices

def find_zero_diagonal_matrices(matrices):
    zero_diagonal_matrices = []
    for matrix in matrices:
        if np.trace(matrix) == 0:
            zero_diagonal_matrices.append(matrix)
    return zero_diagonal_matrices

matrix = np.array([list(map(int, line.split())) for line in open('matrix.txt')])

# Замер времени для алгоритмического способа
start_time = time.time()
matrices_algorithmic = generate_matrices_algorithmic(matrix)
zero_diagonal_matrices_algorithmic = find_zero_diagonal_matrices(matrices_algorithmic)
end_time = time.time()
print(f"Алгоритмический способ: {end_time - start_time:.4f} сек")
print("Матрицы с нулевой диагональю (алгоритмический способ):")
for mat in zero_diagonal_matrices_algorithmic:
    print(mat)
    print()

# Замер времени для способа с использованием NumPy
start_time = time.time()
matrices_pythonic = generate_matrices_pythonic(matrix)
zero_diagonal_matrices_pythonic = find_zero_diagonal_matrices(matrices_pythonic)
end_time = time.time()
print(f"NumPy способ: {end_time - start_time:.4f} сек")
print("Матрицы с нулевой диагональю (NumPy способ):")
for mat in zero_diagonal_matrices_pythonic:
    print(mat)
    print()



