def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def remove_even(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            result.append(arr[i])
    return result


arr = [3, 2, 4, 7, 10, 6, 5]  # 3, 7, 5
print_array(arr)
print_array(remove_even(arr))
