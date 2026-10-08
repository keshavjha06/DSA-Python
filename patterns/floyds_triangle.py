def print_floyds_triangle(n):
    number = 1
    for i in range(1, n + 1):
        row = ""
        for j in range(i):
            row += str(number) + " "
            number += 1
        print(row)


n = int(input())
print_floyds_triangle(n)
