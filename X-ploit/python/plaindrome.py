def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False

word = "able"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
