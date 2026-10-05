def print_factors(n):
    # factors (other than 1 and n) come in pairs: i and n // i
    i = 2
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i != n // i:
                print(n // i)
        i += 1


n = int(input("Enter a number: "))
print_factors(n)
