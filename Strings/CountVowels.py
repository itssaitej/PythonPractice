n=input("Enter a word: ")
count=0
vowels=["a","e","i","o","u"]
l=len(n)
for i in range(0,l):
  for v in range(0,5):
    if n[i]==vowels[v]:
      count=count+1
print(f"The total number of vowels in {n} is/are {count}")

"""
n = input("Enter a word: ").lower()
count = 0

for ch in n:
    if ch in "aeiou":
        count += 1

print(f"Vowel count: {count}")
"""