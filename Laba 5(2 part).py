#будем исключать перестановки строк и столбцов, после которых сумма 1
#строки элементов матрицы превышает заданное значение max_sum.

import numpy as np
from itertools import permutations
import time

matrix = np.array([list(map(int, line.split())) for line in open('matrix.txt')])

def get_permutations_with_diagonal_limit(matrix, max_diagonal_sum):
    n = matrix.shape[0]
    all_indices = list(range(n))
    perm_rows = permutations(all_indices)
    result_matrices = []
    processed_permutations = set() # Множество для хранения обработанных перестановок

    for row_perm in perm_rows:
        for col_perm in permutations(all_indices):
            # Преобразуем перестановки в кортежи для хеширования
            row_tuple = tuple(row_perm)
            col_tuple = tuple(col_perm)

            # Проверяем, была ли такая комбинация перестановок уже обработана
            if (row_tuple, col_tuple) in processed_permutations:
                continue # Пропускаем, если уже обработана

            new_matrix = matrix[list(row_perm), :][:, list(col_perm)]
            if sum(new_matrix[0]) >= max_diagonal_sum:
                if all(new_matrix[i][i]==0 for i in range(len(matrix))):
                    result_matrices.append(new_matrix)
                    # Добавляем текущую комбинацию перестановок в множество обработанных
                    processed_permutations.add((row_tuple, col_tuple))

    return result_matrices

max_diagonal_sum = int(input('Введите число: '))
start_time = time.time()
limited_results = get_permutations_with_diagonal_limit(matrix, max_diagonal_sum)
end_time = time.time()
print(f"Найдено {len(limited_results)} вариантов.")
print(f"Время: {end_time - start_time:.6f} секунд")
for m in limited_results:
    print(m)
    print()
