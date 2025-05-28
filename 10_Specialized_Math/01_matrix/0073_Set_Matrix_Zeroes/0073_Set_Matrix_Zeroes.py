def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    is_first_col_zero = False

    # Step 1: Use first row & column as markers
    for i in range(rows):
        if matrix[i][0] == 0:
            is_first_col_zero = True
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Step 2: Fill zero using markers (excluding first row/col)
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 3: Handle first row
    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0

    # Step 4: Handle first column
    if is_first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0
