def print_odd_number_triangle(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += str(2 * j - 1) + " "  # j-th odd number = 2 * j - 1
        print(row)


def print_odd_number_triangle_counter(n):
    for i in range(1, n + 1):
        row = ""
        a = 1
        for j in range(i):
            row += str(a) + " "
            a += 2
        print(row)


n = int(input("Enter no of rows: "))
print_odd_number_triangle(n)
print_odd_number_triangle_counter(n)
