def print_pyramid(n):
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * (2 * i - 1))


def print_pyramid_nsp_nst(n):
    # nsp = number of spaces, nst = number of stars
    nsp = n - 1
    nst = 1
    for i in range(n):
        print("  " * nsp + "* " * nst)
        nsp -= 1
        nst += 2


n = int(input("Enter no of rows: "))
print_pyramid(n)
print_pyramid_nsp_nst(n)
