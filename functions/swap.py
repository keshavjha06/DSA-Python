def swap(a, b):
    temp = a
    a = b
    b = temp
    print(a, b)


def swap_using_arithmetic(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)


def swap_using_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)


def swap_pythonic(a, b):
    a, b = b, a
    print(a, b)


a = int(input())
b = int(input())
swap(a, b)
swap_using_arithmetic(a, b)
swap_using_xor(a, b)
swap_pythonic(a, b)
