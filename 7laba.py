import tkinter as tk
from tkinter import ttk
import numpy as np
from itertools import permutations
import time

def process_matrix():
    try:
        max_sum = int(entry_max_sum.get())
        matrix_data = text_matrix.get("1.0", tk.END)  # Получаем текст из текстового поля
        matrix = np.array([list(map(int, line.split())) for line in matrix_data.strip().split('\n')])

        def get_permutations_with_diagonal_limit(matrix, max_diagonal_sum):
            n = matrix.shape[0]
            all_indices = list(range(n))
            perm_rows = permutations(all_indices)
            result_matrices = []
            processed_permutations = set()

            for row_perm in perm_rows:
                for col_perm in permutations(all_indices):
                    row_tuple = tuple(row_perm)
                    col_tuple = tuple(col_perm)

                    if (row_tuple, col_tuple) in processed_permutations:
                        continue

                    new_matrix = matrix[list(row_perm), :][:, list(col_perm)]
                    if sum(new_matrix[0]) >= max_diagonal_sum:
                        if all(new_matrix[i][i]==0 for i in range(len(matrix))):
                            result_matrices.append(new_matrix)
                            processed_permutations.add((row_tuple, col_tuple))

            return result_matrices

        start_time = time.time()
        limited_results = get_permutations_with_diagonal_limit(matrix, max_sum)
        end_time = time.time()

        output_text.delete("1.0", tk.END)  # Очищаем окно вывода
        output_text.insert(tk.END, f"Найдено {len(limited_results)} вариантов.\n")
        output_text.insert(tk.END, f"Время: {end_time - start_time:.6f} секунд\n")
        for m in limited_results:
            output_text.insert(tk.END, str(m) + "\n\n")

    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Ошибка: Введите корректное число для max_sum и целые числа в матрицу.\n")
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Ошибка: {e}\n")


root = tk.Tk()
root.title("Обработка матрицы")


label_max_sum = ttk.Label(root, text="Введите число, которое не должно превышать сумма элементов первой строки матрицы:")
label_max_sum.pack()
entry_max_sum = ttk.Entry(root)
entry_max_sum.pack()

label_matrix = ttk.Label(root, text="Введите матрицу (числа через пробел, строки через Enter):")
label_matrix.pack()
text_matrix = tk.Text(root, height=5, width=30)
text_matrix.pack()


process_button = ttk.Button(root, text="Обработать", command=process_matrix)
process_button.pack()

label_output = ttk.Label(root, text="Результат:")
label_output.pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text['yscrollcommand'] = scrollbar.set

root.mainloop()
