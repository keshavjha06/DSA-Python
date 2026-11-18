# Move zeroes to the end: [0, 1, 0, 4, 12] -> [1, 4, 12, 0, 0]


def move_zeros(arr, n):
    j = 0  # points at a zero
    for i in range(n):  # i looks for non-zero elements
        if arr[i] != 0 and arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
        if arr[j] != 0:
            j += 1


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [0, 1, 0, 2, 1, 0, 4, 12]
print_array(arr)
move_zeros(arr, len(arr))
print_array(arr)
