def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
input_str = "Never odd or even"
print(is_palindrome(input_str))
