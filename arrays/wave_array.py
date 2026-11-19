arr = [2, 4, 7, 8, 9, 10]
# stop at len - 1 so arr[i + 1] never goes out of range
for i in range(0, len(arr) - 1, 2):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]

for ele in arr:
    print(ele, end=" ")
print()
