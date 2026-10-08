def print_bridge(n):
    print("* " * (2 * n - 1))
    for i in range(1, n):
        side = "* " * (n - i)
        gap = "  " * (2 * i - 1)
        print(side + gap + side)


n = int(input())
print_bridge(n)
