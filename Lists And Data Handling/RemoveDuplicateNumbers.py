n=[]
wd=[]
l=int(input("How many numbers do you want in the list? : "))
for i in range(0,l):
  n.append(i)
  n[i]=int(input(f"number {i+1}: ")) 

print(f"the given list of numbers is: ")
print(n)

"""
m=set(n)
print(m)
"""
for num in n:
  if num not in wd:
    wd.append(num)
print("the given list without duplicates is: ")
print(wd)