def power(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a, "raised to the power", b, "is", power(a, b))
