def prompt_matrix():
    rows, columns = [int(dimension) for dimension in input().split()]
    return [[int(e) for e in input().split()] for _ in range(rows)]


def add_vectors(v1, v2):
    return [elem1 + elem2 for elem1, elem2 in zip(v1, v2)]


def add_matrices(m1, m2):
    return [add_vectors(row1, row2) for row1, row2 in zip(m1, m2)]


def matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


matrix1 = prompt_matrix()
matrix2 = prompt_matrix()
if matrix_dimensions(matrix1) != matrix_dimensions(matrix2):
    print('ERROR')
else:
    print_matrix(add_matrices(matrix1, matrix2))
