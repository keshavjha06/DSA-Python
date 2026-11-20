def length_of_longest_substring(s):
    if len(s) == 0:
        return 0
    last_index = {}
    max_len = 0
    j = 0  # start of the current window
    for i in range(len(s)):
        if s[i] in last_index:
            j = max(j, last_index[s[i]] + 1)
        last_index[s[i]] = i
        max_len = max(max_len, i - j + 1)
    return max_len


text = "pwwkew"
print(length_of_longest_substring(text))
