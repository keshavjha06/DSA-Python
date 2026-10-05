def print_series(n):
    # 99, 95, 91, 87 ... down to n, positive terms only
    for i in range(99, n - 1, -4):
        if i > 0:
            print(i)


n = int(input("Enter number: "))
print_series(n)
