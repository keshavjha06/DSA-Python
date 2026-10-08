def print_alphabet_alternate(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            letter = chr(i + 64)  # uppercase, 'A' is 65
        else:
            letter = chr(i + 96)  # lowercase, 'a' is 97
        print((letter + " ") * n)


n = int(input())
print_alphabet_alternate(n)
