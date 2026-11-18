arr = [10, 20, 30, 40]

# copy element by element into a new list
brr = [0] * len(arr)
for i in range(len(arr)):
    brr[i] = arr[i]

# x = arr only creates another name for the same list (changing x changes arr)

# arr.copy() makes a new list, so changing y doesn't affect arr
# (for nested lists use copy.deepcopy)
y = arr.copy()
y[0] = 100
print(y[0])
print(arr[0])
