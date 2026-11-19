def linear_search_flag(arr, target):
    found = False
    for i in range(len(arr)):
        if arr[i] == target:
            print("Target exist in array at index " + str(i))
            found = True
            break
    if found:
        print("Target exists in Array")
    else:
        print("Target missing in Array")


def linear_search_index(arr, target):
    # -1 means target not found, since -1 is never a valid index here
    found = -1
    for i in range(len(arr)):
        if arr[i] == target:
            found = i
            break
    if found != -1:
        print("Target exists in Array at index " + str(found))
    else:
        print("Target missing in Array")


arr = [20, 30, 40, 20, 50, 60, 70, 80, 90, 100]
linear_search_flag(arr, 70)
linear_search_index(arr, 20)
