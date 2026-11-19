def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def reverse(numbers, start, end):
    while start < end:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1


numbers = [2, 11, 5, 7, 8, 10]
print_array(numbers)
reverse(numbers, 0, len(numbers) - 1)
print_array(numbers)
