# Python has no char type; a char is just a 1-length string
ch = "\0"
print(ord(ch))

# Java's default char value is '\0'
arr = ["\0"] * 8
for i in range(len(arr)):
    print(arr[i], end=" ")

array = ["Abhinav", "Harsh", "Achyut", "Sahil", "Isha"]
for i in range(len(array)):
    print(array[i], end=" ")
print()
