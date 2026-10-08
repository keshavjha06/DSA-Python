def print_x_star(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            if j == i or j == n + 1 - i:
                row += "* "
            else:
                row += "  "
        print(row)


n = int(input("Enter n: "))
print_x_star(n)
