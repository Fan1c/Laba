import itertools
import timeit

def algoritm(matrix):
    n = len(matrix)

    # Генерация всех перестановок индексов
    def generate_permutations(arr):
        if len(arr) == 1:
            return [arr]
        permutations = []
        for i in range(len(arr)):
            first = arr[i]
            rest = arr[:i] + arr[i + 1:]
            for p in generate_permutations(rest):
                permutations.append([first] + p)
        return permutations

    # Перестановка строк
    def apply_row_permutation(matrix, row_perm):
        return [matrix[i] for i in row_perm]

    # Перестановка столбцов
    def apply_column_permutation(matrix, col_perm):
        return [[row[i] for i in col_perm] for row in matrix]

    # Генерация всех возможных перестановок строк и столбцов
    row_perms = generate_permutations(list(range(n)))
    col_perms = generate_permutations(list(range(n)))

    # Все возможные комбинации перестановок строк и столбцов
    all_permuted_matrices = []
    for rp in row_perms:
        permuted_by_rows = apply_row_permutation(matrix, rp)
        for cp in col_perms:
            permuted_matrix = apply_column_permutation(permuted_by_rows, cp)
            if all(permuted_matrix[i][i]==0 for i in range(len(matrix))):
                all_permuted_matrices.append(permuted_matrix)
    return all_permuted_matrices

def generate_matrices_python(matrix):
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
time_algorithmic = timeit.timeit(lambda: algoritm(matrix), number=10)
print(f"Алгоритмический способ: {time_algorithmic:.4f} сек")
print(f"Количество матриц: {len(algoritm(matrix))}")

# Замер времени для pythonic способа
time_pythonic = timeit.timeit(lambda: find_zero_diagonal_matrices(generate_matrices_python(matrix)), number=10)
print(f"Itertools способ: {time_pythonic:.4f} сек")
print(f"Количество матриц: {len(find_zero_diagonal_matrices(generate_matrices_python(matrix)))}")
