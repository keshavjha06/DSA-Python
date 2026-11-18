def segregate_by_counting(arr):
    number_of_zeros = 0
    for ele in arr:
        if ele == 0:
            number_of_zeros += 1
    for i in range(number_of_zeros):
        arr[i] = 0
    for i in range(number_of_zeros, len(arr)):
        arr[i] = 1


def segregate_two_pointers(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] == 0:
            i += 1
        elif arr[j] == 1:
            j -= 1
        else:
            # arr[i] is 1 and arr[j] is 0
            arr[i] = 0
            arr[j] = 1
            i += 1
            j -= 1


def print_list(arr):
    for ele in arr:
        print(ele, end=" ")
    print()


arr = [1, 0, 0, 1, 1, 0, 1]
segregate_by_counting(arr)
print_list(arr)

arr = [1, 0, 0, 1, 1, 0, 1]
segregate_two_pointers(arr)
print_list(arr)
