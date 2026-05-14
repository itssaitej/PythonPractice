from collections import Counter
"""
n=input("Enter a word or a sentence: ")
c=Counter(n)
print(c)

"""
n=input("Enter a string: ")
freq={}
for ch in n:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
