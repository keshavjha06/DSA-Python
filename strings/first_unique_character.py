def first_uniq_char(s):
    freq = [0] * 256  # supports all ASCII characters
    for ch in s:
        freq[ord(ch)] += 1
    for i in range(len(s)):
        if freq[ord(s[i])] == 1:
            return i
    return -1


print(first_uniq_char("racecar"))
