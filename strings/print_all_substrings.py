def print_all_substrings(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            print(s[i:j + 1], end=" ")  # i to j
        print()


print_all_substrings("gopi")
