def is_divisible_by_5_or_3(n):
    return n % 5 == 0 or n % 3 == 0


def is_four_digit(n):
    return n > 999 and n < 10000


n = int(input("Enter Number: "))

if is_divisible_by_5_or_3(n):
    print("Divisible by 5 or 3")
else:
    print("Not divisible by 5 or 3")

if is_four_digit(n):
    print("4 Digit Number")
else:
    print("Not a 4 digit no.")
