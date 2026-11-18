karan = [0] * 7  # default values 0 0 0 0 0 0 0

# input, one number per line
for i in range(7):
    karan[i] = int(input())

for i in range(7):
    print(2 * karan[i], end=" ")
print()
