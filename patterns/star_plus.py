def print_star_plus(n):
    mid = n // 2 + 1
    for i in range(1, n + 1):
        if i == mid:
            print("* " * n)
        else:
            print("  " * (mid - 1) + "* " + "  " * (n - mid))


n = int(input("Enter no of rows: "))
print_star_plus(n)
