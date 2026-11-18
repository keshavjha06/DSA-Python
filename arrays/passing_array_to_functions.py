def change(y):
    # y refers to the same list object, so the change is visible to the caller
    y[2] = 99


x = [10, 3, 29, 38]
print(x[2])
change(x)
print(x[2])
