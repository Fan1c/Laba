#будем исключать перестановки строк и столбцов, после которых сумма всех
#диагональных элементов превышает заданное значение max_diagonal_sum.

import numpy as np
from itertools import permutations
import time
matrix = np.array([list(map(int, line.split())) for line in open('matrix.txt')])

def get_permutations_with_diagonal_limit(matrix, max_diagonal_sum):
    #Поиск перестановок строк и столбцов матрицы, при которых сумма
    #элементов на главной диагонали не превышает заданное значение.

    n = matrix.shape[0]
    all_indices = list(range(n))  # Индексы всех строк/столбцов
    perm_rows = permutations(all_indices)  # Генерация всех перестановок индексов строк
    result_matrices = []

    for row_perm in perm_rows:  # Перебор всех перестановок строк
        for col_perm in permutations(all_indices):  # Перебор всех перестановок столбцов
            new_matrix = matrix[list(row_perm), :][:, list(col_perm)]  # Создание новой матрицы с переставленными строками и столбцами
            diagonal_sum = np.trace(new_matrix)  # Вычисление суммы элементов на главной диагонали новой матрицы
            if diagonal_sum <= max_diagonal_sum:
                if all(new_matrix[i][i]==0 for i in range(len(matrix))):# Проверка условий на сумму диагонали и на 0-ой диагональ
                    result_matrices.append(new_matrix)  # Добавление матрицы в список, если условие выполняется

    return result_matrices

max_diagonal_sum = int(input('Введите число, которое не превышает сумма после перестановок строк и столбцов: '))
start_time = time.time()
limited_results = get_permutations_with_diagonal_limit(matrix, max_diagonal_sum)
end_time = time.time()
print(f"Найдено {len(limited_results)} вариантов перестановок с ограничением на сумму диагонали.")
print(f"Время выполнения: {end_time - start_time:.6f} секунд")
for m in limited_results:
    print(m)
    print()
