def change(x):
    # rebinding x only changes the local name; ints are immutable,
    # so the caller's variable is not affected
    x = 10


x = 6
print(x)  # 6
change(x)
print(x)  # 6
