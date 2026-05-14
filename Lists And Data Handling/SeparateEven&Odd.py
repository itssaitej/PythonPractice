n=[]
e=[]
o=[]

l=int(input("Enter the total number of numbers from which you wanna find out the number of Even and Odd Numbers: "))
ce=0
co=0
j=0
for i in range(0,l):
  n.append(i)
  n[i]=int(input(f"Number {i+1}: ")) 

print(f"the given list of numbers is: ")
print(n)

for i in range(0,l):
  if n[i]%2==0:
   e.append(n[i])
   
  else:
    o.append(n[i])
    
print(f"List of Even Numbers present: {e}")
print(f"List of Odd Numbers present: {o}")