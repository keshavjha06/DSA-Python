def print_binary_triangle(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            # 1 where i + j is even, 0 otherwise
            if (i + j) % 2 == 0:
                row += "1 "
            else:
                row += "0 "
        print(row)


n = int(input("Enter no of rows: "))
print_binary_triangle(n)
