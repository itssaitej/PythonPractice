n=input("Enter a sentence: ")
print(f"The given sentence is: {n}")
print(f"The given sentence with the spaces removed is:")

"""
l=len(n)
for i in range(0,l):
    if n[i]!=" ":
     print(n[i], end="")

"""
print(n.replace(" ",""))
