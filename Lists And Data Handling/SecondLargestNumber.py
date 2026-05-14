n=[]
l=int(input("Enter the total number of numbers from which you wanna find out the Second Largest number: "))
for i in range(0,l):
  n.append(i)
  n[i]=int(input(f"number {i+1}: ")) 

print(f"the given list of numbers is: ")
print(n)

"""
n.sort()
print(n)
"""

j=0
while j<l-1:
  if n[j]>n[j+1]:
      temp=n[j]
      n[j]=n[j+1]
      n[j+1]=temp
      j=-1
  j=j+1

"""
for i in range(l):
  for j in range(0,l-1):
    if n[j]>n[j+1]:
      temp=n[j]
      n[j]=n[j+1]
      n[j+1]=temp
"""

print(f"Second Largest number is: {n[l-2]}")