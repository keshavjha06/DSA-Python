def missing_num(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    for num in arr:
        total = total - num
    return total


arr = [2, 4, 1, 8, 6, 3, 7]
print(missing_num(arr))
