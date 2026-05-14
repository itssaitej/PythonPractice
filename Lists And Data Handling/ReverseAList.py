n=[]
m=[]
l=int(input("Enter the total number of numbers in the list you wanna see reversed: "))

for i in range(0,l):
  n.append(i)
  n[i]=int(input(f"Number {i+1}: ")) 

print(f"the given list of numbers is: ")
print(n)

j=l
while j>0:
 m.append(n[j-1])
 j-=1
  
print(f"The list after reversing: {m}")
