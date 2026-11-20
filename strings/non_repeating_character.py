def non_repeating_character(s):
    freq = [0] * 256  # supports all ASCII characters
    for ch in s:
        freq[ord(ch)] += 1
    for ch in s:
        if freq[ord(ch)] == 1:
            return ch
    return "$"  # no non-repeating character


print(non_repeating_character("racecar"))
