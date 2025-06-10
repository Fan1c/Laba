#будем исключать перестановки строк и столбцов, после которых сумма 1
#строки элементов матрицы превышает заданное значение max_sum.
import itertools
import timeit

def get_permutations_with_diagonal_limit(matrix, max_diagonal_sum):
    n = len(matrix)
    all_indices = list(range(n))
    result_matrices = []
    processed_permutations = set()

    for row_perm in itertools.permutations(all_indices):
        for col_perm in itertools.permutations(all_indices):
            # Преобразуем перестановки в кортежи для хеширования
            row_tuple = tuple(row_perm)
            col_tuple = tuple(col_perm)

            # Проверяем, была ли такая комбинация перестановок уже обработана
            if (row_tuple, col_tuple) in processed_permutations:
                continue # Пропускаем, если уже обработана
            new_matrix = []
            for i in row_perm:
                row = []
                for j in col_perm:
                    row.append(matrix[i][j])
                new_matrix.append(row)

            if sum(new_matrix[0]) < max_diagonal_sum:
                if all(new_matrix[i][i]==0 for i in range(len(matrix))):
                    result_matrices.append(new_matrix)
                    # Добавляем текущую комбинацию перестановок в множество обработанных
                    processed_permutations.add((row_tuple, col_tuple))
    return result_matrices

matrix = [
    [0, 2, 3, 1],
    [7, 0, 8, 4],
    [6, 9, 0, 2],
    [1, 3, 4, 0]
]

max_diagonal_sum = int(input('Введите число: '))

# Замер времени выполнения функции
def run_permutations():
    global limited_results
    limited_results = get_permutations_with_diagonal_limit(matrix, max_diagonal_sum)

num_runs = 5  # Количество запусков для усреднения времени
execution_time = timeit.timeit(run_permutations, number=num_runs) / num_runs

print(f"Найдено {len(limited_results)} вариантов.")
print(f"Среднее время выполнения: {execution_time:.6f} секунд")

for m in limited_results:
    for row in m:
        print(row)
    print()
