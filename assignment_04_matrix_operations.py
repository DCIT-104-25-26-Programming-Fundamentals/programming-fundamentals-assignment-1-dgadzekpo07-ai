# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
# =============================================================================


def read_matrix(rows, cols, label="matrix"):
    """Read a rows x cols matrix from the user, one row per line."""
    matrix = []
    for i in range(rows):
        while True:
            raw = input(f"Enter row {i + 1} of {label}: ").split()
            if len(raw) != cols:
                print(f"  Please enter exactly {cols} numbers.")
                continue
            row = [float(value) for value in raw]
            matrix.append(row)
            break
    return matrix


def display_matrix(matrix):
    """Print a matrix in a neat, aligned grid format."""
    # Find the widest formatted number so every column lines up.
    width = 0
    for row in matrix:
        for value in row:
            width = max(width, len(f"{value:g}"))

    for row in matrix:
        line = "  ".join(f"{value:g}".rjust(width) for value in row)
        print(line)


def transpose_matrix(matrix):
    """Return the transpose of a matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-size matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product A x B (A is MxN, B is NxP, result is MxP)."""
    m = len(matrix_a)
    n = len(matrix_b)
    p = len(matrix_b[0])

    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


def part_a_transpose():
    print("\n--- Part A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transposed)


def part_b_add():
    print("\n--- Part B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nMatrix A:")
    matrix_a = read_matrix(rows, cols, "matrix A")

    print("\nMatrix B:")
    matrix_b = read_matrix(rows, cols, "matrix B")

    result = add_matrices(matrix_a, matrix_b)

    print("\nSum of Matrices:")
    display_matrix(result)


def part_c_multiply():
    print("\n--- Part C: Multiply Two Matrices ---")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))

    print("\nMatrix A:")
    matrix_a = read_matrix(m, n, "matrix A")

    print("\nMatrix B:")
    matrix_b = read_matrix(n, p, "matrix B")

    result = multiply_matrices(matrix_a, matrix_b)

    print("\nProduct A x B:")
    display_matrix(result)


def main():
    part_a_transpose()
    part_b_add()
    part_c_multiply()


if __name__ == "__main__":
    main()