def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# sort - ascending order
arr = [4, 1, 7, 5, -3, 10, 2]
print_list(arr)
arr.sort()
print_list(arr)
