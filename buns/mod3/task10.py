size = int(input())

matrix = [[i+1 for i in range(size)] for _ in range(size)]
trans_matrix = [[i+1 for _ in range(size)] for i in range(size)]


def print_matrix(matrix, n):
    for i in range(n):
        print(', '.join(map(str, matrix[i])))


print_matrix(matrix, size)
print()
print_matrix(trans_matrix, size)