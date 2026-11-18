def max_range(arr, start, end):
    if start > end:
        return -1
    if arr is None:
        return -1
    max_val = arr[start]
    for i in range(start, end + 1):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


def find_max(arr):
    if len(arr) == 0:
        return -1
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


arr = [1, 3, 23, 9, 20, 24]
print(find_max(arr))
print(max_range(arr, 2, 4))
