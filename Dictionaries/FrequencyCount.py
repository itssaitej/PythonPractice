n=input("Enter a string: ")
freq={}
for ch in n:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)