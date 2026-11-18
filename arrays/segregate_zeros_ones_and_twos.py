arr = [2, 1, 2, 2, 2, 1, 0]

number_of_zeros = 0
number_of_ones = 0
for ele in arr:
    if ele == 0:
        number_of_zeros += 1
    elif ele == 1:
        number_of_ones += 1

for i in range(number_of_zeros):
    arr[i] = 0
for i in range(number_of_zeros, number_of_zeros + number_of_ones):
    arr[i] = 1
for i in range(number_of_zeros + number_of_ones, len(arr)):
    arr[i] = 2

for ele in arr:
    print(ele, end=" ")
print()
