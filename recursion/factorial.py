def factorial(n):
    if n == 0:
        return 1
    partial_ans = factorial(n - 1)
    return n * partial_ans


n = int(input())
if n < 0:
    print("Error")
else:
    print(factorial(n))
