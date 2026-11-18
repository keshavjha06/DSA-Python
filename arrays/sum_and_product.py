# sum of elements
n = int(input("Enter the size of the array: "))
values = input("Enter the elements of the array: ").split()
total = 0
for i in range(n):
    total = total + int(values[i])
print("The sum is " + str(total))

# product of elements (Python ints never overflow, so no need for long)
array = [2, 3, 5, 6, 7]
product = 1
for i in range(len(array)):
    product = product * array[i]
print("The product is " + str(product))
