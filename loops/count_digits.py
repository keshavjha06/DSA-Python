def count_digits(n):
    if n == 0:
        return 1
    n = abs(n)
    count = 0
    while n != 0:
        n = n // 10  # 563 -> 56 -> 5 -> 0
        count += 1
    return count


n = int(input("Enter a number: "))
print(count_digits(n))
