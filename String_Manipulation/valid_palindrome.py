def isPalindrome(s: str) -> bool:
    clean_str = ""
    for c in s:
        if c.isalpha() or c.isdigit():
            clean_str += c

    clean_str = clean_str.lower()

    return clean_str == clean_str[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))