import random

def pl(list):
    for i in list:
        print(i)

def matrix(x, y):
    matrix = [[random.randint(1, 100) for j in range(y)] for i in range(x)]
    return matrix 

def sum_matrices(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
        print("Матрицы разной размерности. Невозможно выполнить сложение.")
        return None

    sum_matrices = [[] for i in range(len(first_matrix))]
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix)):
            if i == j:
                for a in range(len(first_matrix[i])):
                    for b in range(len(second_matrix[j])):
                        if a == b:
                           c = first_matrix[i][a] + second_matrix[j][b]
                           sum_matrices[i].append(c)
    return sum_matrices

matrix_1 = []
matrix_2 = []

for i in range(2):
    x = int(input('Введите количество столбцов матриц: '))
    y = int(input('Введите количество строк матриц: '))
    if not matrix_1:
        matrix_1 = matrix(x,y)
    else:
        matrix_2 = matrix(x,y)

print("Первая матрица:")
pl(matrix_1)
print("Вторая матрица:")
pl(matrix_2)

result = sum_matrices(matrix_1, matrix_2)

if result:
    print("Результат сложения матриц:")
    pl(result) 