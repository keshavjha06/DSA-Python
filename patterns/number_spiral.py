def print_number_spiral(n):
    size = 2 * n - 1
    for i in range(1, size + 1):
        row = ""
        for j in range(1, size + 1):
            a = i
            b = j
            # mirror the bottom half and right half
            if i > n:
                a = 2 * n - i
            if j > n:
                b = 2 * n - j
            row += str(min(a, b)) + " "
        print(row)


n = int(input())
print_number_spiral(n)
