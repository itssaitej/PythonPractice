n=[]
l=int(input("Enter the total number of numbers from which you wanna find out the number of Even and Odd Numbers: "))
ce=0
co=0
for i in range(0,l):
  n.append(i)
  n[i]=int(input(f"Number {i+1}: ")) 

print(f"the given list of numbers is: ")
print(n)

for i in range(0,l):
  if n[i]%2==0:
   ce=ce+1
  else:
    co=co+1
print(f"Total Even numbers={ce} and Total Odd numbers={co}")