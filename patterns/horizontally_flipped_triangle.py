def print_horizontally_flipped_triangle(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 2 - i):  # i + j_max = n + 1
            row += chr(j + 96) + " "
        print(row)


n = int(input())
print_horizontally_flipped_triangle(n)
