n = input("Enter a word: ").lower()

"""
for ch in n:
    if ch in "aeiou":
        n=n.replace(ch,"")

print(f"Your String with all the Vowels removed is: {n} ")
"""
"""
result = ""

for ch in n:
    if ch not in "aeiou":
        result += ch

print(f"Your string without vowels: {result}")
"""
result = "".join(ch for ch in n if ch not in "aeiou")
print(result)