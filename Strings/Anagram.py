n=input("Enter first word: ")
m=input("Enter second word: ")

ln=len(n)
lm=len(m)

check=False

s1=''.join(sorted(n))
s2=''.join(sorted(m))

a=0
na=0
if ln!=lm:
   print(f"{n} and {m} are not Anagrams")
   
elif ln==lm:
   for i in range(0,ln):
      if s1[i]==s2[i]:
        a=a+1     
      else:
         na=na+1
   if a==ln:
      print(f"{n} and {m} are Anagrams")
   else:
      print(f"{n} and {m} are not Anagrams")
"""
if sorted(n) == sorted(m):
    print(f"{n} and {m} are Anagrams")
else:
    print(f"{n} and {m} are not Anagrams")
"""