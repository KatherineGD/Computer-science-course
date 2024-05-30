#читаем матрицу:

def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

#Находим максимальный элемент:
def find_max_in_column(matrix, k):
    max_value = float('inf')
    max_index = -1
    for i in range(len(matrix)):
        if matrix[i][k] < max_value:
            max_value = matrix[i][k]
            max_index = i
    return max_value, max_index

#найдем сумму отрицательных элементов, введя функцию:
def sum_of_negative_elements(row):
    return sum(min(x) for x in row)

file_path = '1.txt'
matrix = read_matrix_from_file(file_path)

k = int(input("Напишите значение k (начиная с 0):"))

max_value, max_index = find_max_in_column(matrix, k)

print(f"Максимальный элемент в {k}-м столбце: {max_value}")

row_with_min = matrix[max_index]
sum_negative = sum_of_negative_elements(row_with_min)

print(f"Сумма отрицательных элементов в строке с минимальным элементом: {sum_negative}")