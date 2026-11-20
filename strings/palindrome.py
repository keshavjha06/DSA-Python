def is_palindrome(text):
    if text is None or len(text) == 0:
        return True
    text = text.lower()
    i = 0
    j = len(text) - 1
    while i <= j:
        if text[i] != text[j]:
            return False
        i += 1
        j -= 1
    return True


text = "abcdcba"
print(is_palindrome(text))
