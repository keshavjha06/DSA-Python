def print_rhombus(n):
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * n)


n = int(input("Enter no of rows: "))
print_rhombus(n)
