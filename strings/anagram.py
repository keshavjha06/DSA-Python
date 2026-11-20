def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


s1 = "LISTEN"
s2 = "SILENT"
if is_anagram(s1, s2):
    print("Anagram")
else:
    print("Not Anagram")
