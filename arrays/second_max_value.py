def find_second_max(arr):
    # Python ints have no minimum value, so start from negative infinity
    max_value = float("-inf")
    second_max = float("-inf")
    for i in range(len(arr)):
        if arr[i] > max_value:
            second_max = max_value
            max_value = arr[i]
        elif arr[i] > second_max and arr[i] != max_value:  # skip duplicates of max
            second_max = arr[i]
    return second_max


arr = [13, 34, 2, 34, 33, 1]
print(find_second_max(arr))
