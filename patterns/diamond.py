def print_diamond(n):
    # upper half
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * (2 * i - 1))
    # lower half
    for i in range(n - 1, 0, -1):
        print("  " * (n - i) + "* " * (2 * i - 1))


def print_diamond_nsp_nst(n):
    # nsp = number of spaces, nst = number of stars
    nsp = n - 1
    nst = 1
    for i in range(n):
        print("  " * nsp + "* " * nst)
        nsp -= 1
        nst += 2

    nsp = 1
    nst = 2 * n - 3
    for i in range(n):
        print("  " * nsp + "* " * nst)
        nsp += 1
        nst -= 2


n = int(input("Enter no of rows: "))
print_diamond(n)
print_diamond_nsp_nst(n)
