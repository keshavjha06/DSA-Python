def print_hollow_rectangle(rows, cols):
    for i in range(1, rows + 1):
        row = ""
        for j in range(1, cols + 1):
            # stars only on the border
            if i == 1 or i == rows or j == 1 or j == cols:
                row += "* "
            else:
                row += "  "
        print(row)


rows = int(input("Enter no of rows: "))
cols = int(input("Enter no of columns: "))
print_hollow_rectangle(rows, cols)
