def rotate_image(matrix):
    n = len(matrix)  # works for square matrices
    # transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()


# sample: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
arr = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input("Enter the elements: ")))
    arr.append(row)
rotate_image(arr)
