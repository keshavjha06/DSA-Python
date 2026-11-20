def change_the_string(s):
    if len(s) == 0:
        return ""
    if s[0].isupper():
        return s.upper()
    return s.lower()


s = "TbCD"
print(change_the_string(s))
