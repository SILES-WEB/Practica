
n = int(input("Введите количество строк и столбцов для матрицы: "))
# Создание матрицы и заполнение элементов
matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = (i + 1) * (j + 1)

# Вывод исходной матрицы
print("Исходная матрица:")
for row in matrix:
    print(row)

# Замена элементов на диагоналях на единицы
for i in range(n):
    matrix[i][i] = 1  # Главная диагональ
    matrix[i][n - 1 - i] = 1  # Побочная диагональ

# Вывод матрицы с замененными элементами на диагоналях
print("\nМатрица с замененными диагоналями:")
for row in matrix:
    print(row)
