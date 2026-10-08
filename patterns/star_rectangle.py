def print_star_rectangle(rows, cols):
    for i in range(rows):
        print("* " * cols)


rows = int(input("Enter no of rows: "))
cols = int(input("Enter no of columns: "))
print_star_rectangle(rows, cols)
