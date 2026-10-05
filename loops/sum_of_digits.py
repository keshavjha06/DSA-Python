def sum_of_digits(num):
    num = abs(num)
    total = 0
    while num != 0:
        total = total + num % 10
        num = num // 10
    return total


num = int(input("Enter a number: "))
print("The sum is:", sum_of_digits(num))
