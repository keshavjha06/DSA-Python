def reverse_number(num):
    sign = 1
    if num < 0:
        sign = -1
        num = -num
    rev = 0
    while num != 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return sign * rev


num = int(input("Enter a number: "))
print("The Reverse is:", reverse_number(num))
