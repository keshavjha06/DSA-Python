def sum_of_all_substrings(s):
    total = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            total = total + int(s[i:j + 1])
    return total


print(sum_of_all_substrings("6759"))
