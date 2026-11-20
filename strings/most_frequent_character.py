# Approach 1: sort, then count runs of equal characters
def most_frequent_sorting(s):
    arr = sorted(s)  # aeelmpsstt
    n = len(arr)
    max_freq = -1
    ans = arr[0]
    i = 0
    j = 0
    while j < n:
        if arr[i] == arr[j]:
            j += 1
        else:
            freq = j - i
            if freq > max_freq:
                max_freq = freq
                ans = arr[i]
            i = j
    freq = j - i  # last run
    if freq > max_freq:
        ans = arr[i]
    return ans


# Approach 2: frequency array for 'a'..'z'
def most_frequent_freq_array(s):
    freq = [0] * 26
    for ch in s:
        index = ord(ch) - ord("a")
        freq[index] += 1
    max_freq = 0
    ans = s[0]
    for i in range(26):
        if freq[i] > max_freq:
            max_freq = freq[i]
            ans = chr(i + ord("a"))
    return ans


s = "testsample"
print(most_frequent_sorting(s))
print(most_frequent_freq_array(s))
