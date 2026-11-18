def set_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_coords = []
    col_coords = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_coords.append(i)
                col_coords.append(j)

    for r in row_coords:
        for j in range(cols):
            matrix[r][j] = 0

    for c in col_coords:
        for i in range(rows):
            matrix[i][c] = 0

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()


nums = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
set_zeroes(nums)
