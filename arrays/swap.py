def swap(arr, num1, num2):
    temp = arr[num1]
    arr[num1] = arr[num2]
    arr[num2] = temp


def reverse(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        swap(arr, start, end)
        start += 1
        end -= 1


arr = [1, 5, 7, 9, 10, 56]
reverse(arr)
print(arr)
