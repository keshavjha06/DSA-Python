def print_ap(n, a, d):
    for i in range(n):
        print(a, end=" ")
        a = a + d
    print()


def print_series_2_5_8(n):
    # 2, 5, 8, 11 ... n terms: last term is 3 * n - 1
    for i in range(2, 3 * n, 3):
        print(i, end=" ")
    print()


n = int(input("Enter no of terms: "))
a = int(input("Enter First term: "))
d = int(input("Enter common difference: "))
print_ap(n, a, d)
print_series_2_5_8(n)
