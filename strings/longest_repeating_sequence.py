def longest_repeating_sequence(text):
    n = len(text)
    substring_counts = {}
    # count every possible substring
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = text[i:j]
            substring_counts[sub] = substring_counts.get(sub, 0) + 1

    # longest substring that appears at least twice
    lrs = ""
    for sub in substring_counts:
        count = substring_counts[sub]
        if count > 1 and len(sub) > len(lrs):
            lrs = sub
    return lrs


text = "acbdfghybdf"
print("Longest repeating sequence: " + longest_repeating_sequence(text))
