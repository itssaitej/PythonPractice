n=int(input("Enter a number greater than or equal to 1:\n"))

count=0

for i in range(1,n+1):
    div=n%i
    if(div==0):    
        count=count+1
if(count==1):
  print(f"{n} is neither a Prime nor a Composite Number")
elif(count==2):
   print(f"{n} is a Prime Number")
else:
   print(f"{n} is a Composite Number")

"""
if n <= 1:
    print(f"{n} is neither prime nor composite")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is a Prime Number")
    else:
        print(f"{n} is a Composite Number")
"""

"""
x=1
while(x<=n):
  div=n%x
  if(div==0):    
     count=count+1 
  x=x+1
"""