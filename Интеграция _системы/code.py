def sort_rows_ascending(matrix):
    for row in matrix:
        row.sort()

# Пример двумерного массива
matrix = [
    [4, 2, 7, 1],
    [9, 5, 3, 8],
    [6, 0, 2, 3]
]

sort_rows_ascending(matrix)

# Вывод отсортированного массива
for row in matrix:
    print(row)

