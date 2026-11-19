def contains_duplicate(arr):
    # sort manually (without using sort())
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    for k in range(1, len(arr)):
        if arr[k] == arr[k - 1]:
            return True
    return False


nums = [1, 2, 3, 1]
print(contains_duplicate(nums))
