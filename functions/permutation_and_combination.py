def fact(x):
    f = 1
    for i in range(1, x + 1):
        f = f * i
    return f


n = int(input())
r = int(input())

ncr = fact(n) // (fact(r) * fact(n - r))
npr = fact(n) // fact(n - r)
print(ncr, npr)
