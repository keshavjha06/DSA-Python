def add_arrays(arr1, arr2):
    ans = []
    i = len(arr1) - 1
    j = len(arr2) - 1
    carry = 0
    while i >= 0 or j >= 0 or carry > 0:
        total = carry
        if i >= 0:
            total = total + arr1[i]
            i -= 1
        if j >= 0:
            total = total + arr2[j]
            j -= 1
        ans.append(total % 10)
        carry = total // 10
    ans.reverse()
    return ans


# [3, 5, 2, 0, 7] + [9, 2, 1] = [3, 6, 1, 2, 8]
arr1 = [3, 5, 2, 0, 7]
arr2 = [9, 2, 1]
ans = add_arrays(arr1, arr2)
for ele in ans:
    print(ele, end=" ")
print()
