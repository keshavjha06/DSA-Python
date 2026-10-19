arr = []
arr.append(25)
arr.append(12)
arr.append(2)
arr.append(89)
arr.append(9)
print(arr[2])
arr[3] = 50
print(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
print()

for ele in arr:
    print(ele, end=" ")

# 25 12 2 50 9
arr.append(78)  # 25 12 2 50 9 78
arr.insert(1, 100)
print(arr)  # 25 100 12 2 50 9 78
arr.pop()  # remove last element
print(arr)

# reverse manually (or simply arr.reverse())
i = 0
j = len(arr) - 1
while i < j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i += 1
    j -= 1
print(arr)

list1 = [100, 200, 300]
list2 = [400, 500, 600]

list1.extend(list2)  # addAll
print(list1)

# removeAll: keep only the elements not in list2
remaining = []
for ele in list1:
    if ele not in list2:
        remaining.append(ele)
list1 = remaining
print(list1)

print(len(list1))

print("printing list2:", list2)
list2.clear()
print(len(list2))

# traverse list (a for loop uses an iterator behind the scenes)
for ele in list1:
    print("Element:", ele)

list3 = [11, 12, 14]
print(list3[2])
print("Before Set", list3)
list3[0] = 100
print("After Set", list3)

# toArray -> tuple (an immutable copy)
array = tuple(list3)
for obj in array:
    print(str(obj) + " ")

# contains
print(100 in list3)  # True

list1.append(12)
list1.append(6)
print("Printing Entire list", list1)

list1.sort()
print("After sorting ascending", list1)
# list1.sort(reverse=True) for descending

new_list = list1.copy()  # clone
print("Printing Entire newList:", new_list)

marks = []  # Python lists grow automatically, no ensureCapacity needed
print(len(marks) == 0)  # True

print(new_list.index(100))  # index of element 100 -> 2
