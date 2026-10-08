def print_letter_triangle(n):
    for i in range(1, n + 1):
        letter = chr(i + 64)  # 'A' is 65
        print((letter + " ") * i)


n = int(input())
print_letter_triangle(n)
