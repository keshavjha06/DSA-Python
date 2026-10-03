def greatest_of_three(a, b, c):
    if a >= b:
        if a >= c:
            return a
        return c
    # b > a
    if b >= c:
        return b
    return c


a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
c = int(input("Enter 3rd no: "))
print(greatest_of_three(a, b, c))
