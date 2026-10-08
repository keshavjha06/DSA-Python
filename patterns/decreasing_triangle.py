def print_decreasing_triangle(n):
    for i in range(1, n + 1):
        print("  " * (i - 1) + "* " * (n - i + 1))


n = int(input("Enter no of rows: "))
print_decreasing_triangle(n)
