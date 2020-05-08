def prompt_matrix():
    rows, columns = [int(dimension) for dimension in input().split()]
    return [[int(e) for e in input().split()] for _ in range(rows)]


def add_vectors(v1, v2):
    return [elem1 + elem2 for elem1, elem2 in zip(v1, v2)]


def add_matrices(m1, m2):
    return [add_vectors(row1, row2) for row1, row2 in zip(m1, m2)]


def matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


def scalar_mul_matrix(scalar, matrix):
    return [[scalar * elem for elem in row] for row in matrix]


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


m = prompt_matrix()
scal = int(input())
print_matrix(scalar_mul_matrix(scal, m))
