def print_number_alphabet_triangle(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            if i % 2 == 0:
                row += chr(j + 64) + " "
            else:
                row += str(j) + " "
        print(row)


n = int(input())
print_number_alphabet_triangle(n)
