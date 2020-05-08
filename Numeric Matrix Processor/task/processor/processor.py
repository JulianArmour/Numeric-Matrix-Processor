def prompt_dimensions(query):
    height, width = [int(dimension) for dimension in input(query).split()]
    return height, width


def as_number(number_str):
    return int(number_str) if number_str.isnumeric() else float(number_str)


def prompt_matrix(height):
    return [[as_number(e) for e in input().split()] for _ in range(height)]


def is_valid_matrix(height, width, matrix):
    return height == len(matrix) and all(len(row) == width for row in matrix)


def add_vectors(v1, v2):
    return [elem1 + elem2 for elem1, elem2 in zip(v1, v2)]


def inner_product(v1, v2):
    return sum(elem1 * elem2 for elem1, elem2 in zip(v1, v2))


def add_matrices(m1, m2):
    return [add_vectors(row1, row2) for row1, row2 in zip(m1, m2)]


def matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


def scalar_mul_matrix(scalar, matrix):
    return [[scalar * elem for elem in row] for row in matrix]


def mul_matrices(m1, m2):
    return [[inner_product(m1_row, m2_col) for m2_col in zip(*m2)] for m1_row in m1]


def matrix_str(matrix):
    rows = (' '.join(map(str, row)) for row in matrix)
    return '\n'.join(rows)


def menu():
    return '\n'.join(['1. Add matrices', '2. Multiply matrix by a constant',
                      '3. Multiply matrices', '0. Exit'])


def prompt_two_matrices():
    m1_height, m1_width = prompt_dimensions('Enter size of first matrix: ')
    print('Enter first matrix: ')
    matrix1 = prompt_matrix(m1_height)

    m2_height, m2_width = prompt_dimensions('Enter size of second matrix: ')
    print('Enter second matrix: ')
    matrix2 = prompt_matrix(m2_height)
    return matrix1, matrix2


def matrix_addition_routine():
    matrix1, matrix2 = prompt_two_matrices()
    if matrix_dimensions(matrix1) != matrix_dimensions(matrix2):
        print('The operation cannot be performed')
    else:
        print(matrix_str(add_matrices(matrix1, matrix2)))


def matrix_scalar_multiplication_routine():
    m_height, m_width = prompt_dimensions('Enter size of matrix: ')
    print('Enter matrix: ')
    m = prompt_matrix(m_height)
    constant = float(input('Enter constant: '))
    print('The result is:')
    print(matrix_str(scalar_mul_matrix(constant, m)))


def multiply_matrices_routine():
    matrix1, matrix2 = prompt_two_matrices()
    height1, width1 = matrix_dimensions(matrix1)
    height2, width2 = matrix_dimensions(matrix2)
    if width1 != height2:
        print('The operation cannot be performed')
    else:
        print(matrix_str(mul_matrices(matrix1, matrix2)))


while True:
    print(menu())
    choice = input('Your choice: ')
    if choice == '1':
        matrix_addition_routine()
    elif choice == '2':
        matrix_scalar_multiplication_routine()
    elif choice == '3':
        multiply_matrices_routine()
    else:
        break
