def merge(c, a, b):
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    # b is finished -> take remaining elements of a
    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1
    # a is finished -> take remaining elements of b
    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1


def print_list(arr):
    for ele in arr:
        print(ele, end=" ")
    print()


a = [2, 5, 6, 9, 20]
b = [1, 3, 4, 5, 7, 8]
c = [0] * (len(a) + len(b))
print_list(c)
merge(c, a, b)
print_list(c)
