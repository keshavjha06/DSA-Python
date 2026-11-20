def bubble_sort_basic(arr):
    n = len(arr)
    for i in range(n - 1):  # n - 1 passes
        for j in range(n - 1 - i):  # last i elements are already sorted
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # n - 1 passes
        swapped = False
        for j in range(n - 1 - i):  # last i elements are already sorted
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # no swaps means the array is sorted
            break


arr = [3, 5, 1, 4, 2, 0]
print("Arrays before Sorting", arr)
bubble_sort(arr)
print("Arrays after Sorting", arr)

arr2 = [3, 5, 1, 4, 2, 0]
bubble_sort_basic(arr2)
print("Arrays after Sorting (basic)", arr2)
