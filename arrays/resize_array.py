def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def resize(arr, capacity):
    # Python lists grow on their own; this shows the fixed-size array idea
    temp = [0] * capacity
    for i in range(len(arr)):
        temp[i] = arr[i]
    return temp


original = [5, 1, 2, 9, 10]
print("The size of original array is " + str(len(original)))
original = resize(original, 10)
print("The size of original array after resize is " + str(len(original)))
