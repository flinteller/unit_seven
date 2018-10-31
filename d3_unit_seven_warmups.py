def is_palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False


print(is_palindrome("racecar"))
print(is_palindrome("reverse"))
