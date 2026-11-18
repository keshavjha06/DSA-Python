def find_minimum(arr):
    if arr is None or len(arr) == 0:
        raise ValueError("Invalid input")
    minimum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum


arr = [4, 9, 3, 1, 10, 15]
print(find_minimum(arr))
