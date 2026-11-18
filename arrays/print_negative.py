n = int(input("Enter array size: "))
values = input("Enter array elements: ").split()
arr = []
for i in range(n):
    arr.append(int(values[i]))

# printing negative values
for i in range(n):
    if arr[i] < 0:
        print(arr[i], end=" ")
print()
