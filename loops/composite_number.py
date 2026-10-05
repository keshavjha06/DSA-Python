def is_prime(n):
    # 1 and n are always factors, so check 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input("Enter a number: "))
if n == 1:
    print("Neither Prime nor Composite")
elif not is_prime(n):
    print("Composite Number")
else:
    print("Prime Number")
