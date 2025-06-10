#будем исключать перестановки строк и столбцов, после которых сумма 1
#строки элементов матрицы превышает заданное значение max_sum.
import timeit
import itertools

max_digital=int(input("Введите число: "))
def generate_matrices_python(matrix, max_sum):
    # Генерирует перестановки строк и столбцов матрицы,
    # исключая перестановки, где сумма элементов первой строки превышает max_sum.
    n = len(matrix)
    row_permutations = list(itertools.permutations(range(n)))
    col_permutations = list(itertools.permutations(range(n)))

    matrices = []
    for row_perm in row_permutations:
        # Создаем новую матрицу с переставленными строками
        new_matrix_rows = [matrix[i] for i in row_perm]

        # Проверяем, что сумма элементов в первой строке не превышает max_sum
        if sum(new_matrix_rows[0]) > max_sum:
            continue # Пропускаем эту перестановку строк

        for col_perm in col_permutations:
            new_matrix = []
            for row in new_matrix_rows:
                new_row = [row[j] for j in col_perm]
                new_matrix.append(new_row)
            if all(new_matrix[i][i]==0 for i in range (len(new_matrix))):
                matrices.append(new_matrix)
    return matrices


def print_matrix(M):
    for row in M:
        print("    ", row)

def print_first_n(variants, n=5):
    for k, M in enumerate(variants[:n], 1):
        print(f"Вариант {k}:")
        print_matrix(M)
        print()

if __name__ == "__main__":
    A = [
        [0, 2, 3, 1],
        [7, 0, 8, 4],
        [6, 9, 0, 2],
        [1, 3, 4, 0]
    ]
    print("Исходная матрица:")
    print_matrix(A)
    zero_idx = [i for i in range(len(A)) if A[i][i] == 0]
    first_zero = zero_idx[0]

    vars_it = generate_matrices_python(A, max_digital)

    cons = lambda M: sum(M[first_zero]) % 2 == 0
    obj = lambda M: sum(M[i][i] for i in range(len(M)))
    filtered = [M for M in vars_it if cons(M)]
    max_obj = max(obj(M) for M in filtered)
    optimal = [M for M in filtered if obj(M) == max_obj]

    print("=== Часть 2: Оптимальные варианты ===")
    print("Условия отбора:")
    print(f"  1) Сумма элементов строки 1 чётна")
    print(f"  2) Максимальная сумма диагонали = {max_obj}")
    print(f"Найдено оптимальных вариантов: {len(optimal)}")

    print_first_n(optimal)
