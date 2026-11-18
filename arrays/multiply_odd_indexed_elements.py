arr = [10, 20, 30, 40, 50, 60]
for i in range(len(arr)):
    if i % 2 == 1:
        arr[i] = arr[i] * 2
    else:
        arr[i] = arr[i] + 10
    print(arr[i], end=" ")
print()
