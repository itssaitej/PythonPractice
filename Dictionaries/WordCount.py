n="I am Sai Tej Tej Sai"
m=n.split()

freq={}
for word in m:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
for word in freq:
    print(f"{word}: {freq[word]}")