import random
n = int(input("Введите колличество строк матрицы: "))
m = int(input("Введите колличество столбцов матрицы: "))
matrix_1 = [[random.randint(0, 10) for i in range(m)]for i in range(n)]
matrix_2 = [[random.randint(0, 10) for i in range(m)]for i in range(n)]
matrix_3 =[[matrix_1[i][j] + matrix_2[i][j] for j in range (len(matrix_1[0]))] for i in range (len(matrix_1))]
for i in matrix_3:print(i)
