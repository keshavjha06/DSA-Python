def print_sequence(n):
    # n = 10: 1 10 2 9 3 8 4 7 5 6
    for i in range(1, n + 1):
        if i % 2 != 0:
            print((i + 1) // 2, end=" ")
        else:
            print(n - i // 2, end=" ")
    print()


n = int(input("Enter number: "))
print_sequence(n)
