def print_number_square(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * n)


n = int(input("Enter number for rows: "))
print_number_square(n)
