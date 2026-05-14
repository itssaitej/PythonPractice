n=input("Enter a string: ")
i=0
l=0
u=0
d=0
sc=0
for i in range(len(n)):
   if n[i].isupper():
     u+=1
   elif n[i].islower():
     l+=1
   elif n[i].isdigit():
     d+=1
   else:
     sc+=1
print(f"Number of \nlowercased letters= {l}\nuppercased letters= {u}\ndigits= {d}\nspaces= {sc}")