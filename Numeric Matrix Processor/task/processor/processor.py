import sys


def two_matrices():
    dimensions_1 = input("Enter size of first matrix: ").split()
    print("Enter first matrix:")
    matrix_1 = [input().split() for _ in range(int(dimensions_1[0]))]
    dimensions_2 = input("Enter size of second matrix: ").split()
    print("Enter second matrix:")
    matrix_2 = [input().split() for _ in range(int(dimensions_2[0]))]
    return dimensions_1, dimensions_2, matrix_1, matrix_2


def print_result(result):
    print("The result is:")
    for r in result:
        print(*r, sep=' ')
    print()


def add_matrices():
    row_col_1, row_col_2, matrix_1, matrix_2 = two_matrices()
    if (row_col_1[0] != row_col_2[0]) or (row_col_1[1] != row_col_2[1]):  # if number of rows and columns are not equal
        print("The operation cannot be performed.\n")
    else:
        result = [[float(matrix_1[i][j]) + float(matrix_2[i][j]) for j in range(len(matrix_1[0]))] for i in
                  range(len(matrix_1))]
        print_result(result)


def multiply_by_constant():
    row_col = input("Enter size of matrix: ").split()
    print("Enter matrix:")
    matrix = [input().split() for _ in range(int(row_col[0]))]
    constant = float(input("Enter constant: "))
    result = [[float(matrix[i][j]) * constant for j in range(len(matrix[0]))] for i in range(len(matrix))]
    print_result(result)


def multiply_matrices():
    row_col_1, row_col_2, m_1, m_2 = two_matrices()
    if row_col_1[1] != row_col_2[0]:  # if number of matrix A columns is not equal to matrix B rows
        print("The operation cannot be performed.")
    else:
        result = [[sum(float(a) * float(b) for a, b in zip(x_row, y_col)) for y_col in zip(* m_2)] for x_row in m_1]
        print_result(result)


def transpose_matrix():
    print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    transposition_choice = input("Your choice: ")
    matrix_size = input("Enter matrix size: ").split()
    print("Enter matrix: ")
    matrix = [input().split() for _ in range(int(matrix_size[0]))]
    if transposition_choice == "1":
        result = [[float(matrix[j][i]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        print_result(result)
    elif transposition_choice == "2":
        result = [[float(matrix[j][i]) for j in reversed(range(len(matrix[0])))] for i in reversed(range(len(matrix)))]
        print_result(result)
    elif transposition_choice == "3":
        result = [[float(matrix[i][j]) for j in reversed(range(len(matrix[0])))] for i in range(len(matrix))]
        print_result(result)
    elif transposition_choice == "4":
        result = [[float(matrix[i][j]) for j in range(len(matrix[0]))] for i in reversed(range(len(matrix)))]
        print_result(result)


def det_matrix():
    matrix_size = input("Enter matrix size: ").split()
    print("Enter matrix: ")
    matrix = [input().split() for _ in range(int(matrix_size[0]))]
    return matrix


def smaller_matrix(original_matrix, column):
    new_matrix = [row[:] for row in original_matrix]
    new_matrix = new_matrix[1:]
    for i in range(len(new_matrix)):
        new_matrix[i] = new_matrix[i][0:column] + new_matrix[i][column + 1:]
    return new_matrix


def determinant(matrix):
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            print("Not a square matrix.")
    if len(matrix[0]) == 1:
        return float(matrix[0][0])
    elif len(matrix) == 2:
        simple_determinant = float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
        return simple_determinant
    x = 0
    num_columns = num_rows
    for i in range(num_columns):
        cofactor = pow(-1, i) * float(matrix[0][i]) * determinant(smaller_matrix(matrix, i))
        x += cofactor

    return x


def menu_choice(num_choice):
    if num_choice == "1":
        add_matrices()
    elif num_choice == "2":
        multiply_by_constant()
    elif num_choice == "3":
        multiply_matrices()
    elif num_choice == "4":
        transpose_matrix()
    elif num_choice == "5":
        print(f"The result is:\n{round(determinant(det_matrix()), 2)}\n")
    else:
        sys.exit()


def menu_display():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("0. Exit")
        num = input("Your choice: ")
        if num == "0":
            break
        else:
            menu_choice(num)


if __name__ == "__main__":
    menu_display()
