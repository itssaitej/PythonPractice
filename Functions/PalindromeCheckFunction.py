"""
def palindromeCheck(n):
    print(f"Your word is: {n}")
    m=n[::-1]
    if m==n:
     print(f"{n} is a palindrome")
    else:
     print(f"{n} is not a palindrome")
    return n
n=input("Enter a word: ").lower()
palindromeCheck(n)
"""

def is_palindrome(word):
    return word == word[::-1]


n = input("Enter word: ").lower()

if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")