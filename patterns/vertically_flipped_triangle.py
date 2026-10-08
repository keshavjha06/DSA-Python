def print_flipped_triangle(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            if i + j > n:
                row += "* "
            else:
                row += "  "
        print(row)


def print_flipped_triangle_spaces(n):
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)


n = int(input("Enter no of rows: "))
print_flipped_triangle(n)
print_flipped_triangle_spaces(n)
