def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def reverse(arr, i, j):
    while i < j:
        swap(arr, i, j)
        i += 1
        j -= 1


def next_permutation(arr):
    # find first index from the right where arr[i] < arr[i + 1]
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        # find the rightmost element bigger than arr[i]
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        swap(arr, i, j)
    reverse(arr, i + 1, len(arr) - 1)


nums = [1, 2, 3]
next_permutation(nums)
for num in nums:
    print(num, end=" ")
print()
