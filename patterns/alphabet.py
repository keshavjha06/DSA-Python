def print_alphabet_square(n):
    for i in range(1, n + 1):
        letter = chr(i + 96)  # 'a' is 97
        print((letter + " ") * n)


n = int(input())
print_alphabet_square(n)
