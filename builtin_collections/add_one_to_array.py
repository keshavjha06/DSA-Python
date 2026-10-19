def add_one(arr):
    ans = []
    carry = 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] + carry <= 9:
            ans.append(arr[i] + carry)
            carry = 0
        else:  # arr[i] + carry == 10
            ans.append(0)
            carry = 1
    if carry == 1:
        ans.append(1)
    ans.reverse()
    return ans


arr = [9, 9, 9]  # [5, 6, 7, 8]
ans = add_one(arr)
for ele in ans:
    print(ele, end=" ")
print()
