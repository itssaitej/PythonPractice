n=input("Enter a word: ").lower()

print(f"Your word is: {n}")

m=n[::-1]

print(f"Your word in the reverse way is: {m}")

if m==n:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")