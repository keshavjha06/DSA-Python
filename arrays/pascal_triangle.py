def generate(num_rows):
    ans = []
    prev = None
    for i in range(num_rows):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(prev[j - 1] + prev[j])
        prev = row
        ans.append(row)
    return ans


print(generate(5))
