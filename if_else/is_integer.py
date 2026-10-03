def is_integer(n):
    return n == int(n)


n = float(input("Enter Number: "))  # e.g. 3.1415
if is_integer(n):
    print("Is an Integer")
else:
    print("Not an integer")
