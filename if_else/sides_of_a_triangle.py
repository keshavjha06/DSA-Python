def is_valid_triangle(a, b, c):
    # sum of any two sides must be greater than the third
    return a + b > c and b + c > a and c + a > b


a = int(input("Enter 1st Side: "))
b = int(input("Enter 2nd Side: "))
c = int(input("Enter 3rd Side: "))
if is_valid_triangle(a, b, c):
    print("Valid Triangle")
else:
    print("Invalid Triangle")
