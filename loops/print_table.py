def count_down(n):
    for i in range(n, 0, -1):
        print(i)


def print_table_of_17():
    for i in range(1, 10):
        print(i * 17, end=" ")
    print()


def print_odd_multiples_of_3():
    for i in range(1, 100):
        if i % 3 == 0 and i % 2 != 0:
            print(i, end=" ")
    print()


n = int(input("Enter a number: "))
count_down(n)
print_table_of_17()
print_odd_multiples_of_3()
