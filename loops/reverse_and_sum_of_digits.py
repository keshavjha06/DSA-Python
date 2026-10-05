def reverse_number(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return sign * rev


# 1234 reversed is 4321 and their sum is 5555
n = int(input("Enter a number: "))
rev = reverse_number(n)
print("Reverse:", rev)
print("Sum of number and its reverse:", n + rev)
