"""
def countFact():
 n=int(input("The Number you are going to enter is a Prime Number: "))
 x=1
 count=0
 while(x<=n):
   div=n%x
   if(div==0):    
     count=count+1 
   x=x+1
 return count

def check_PorC(): 
 c=countFact()
 if c==2:
   result=True
 else:
   result=False
 print(result)  
 return result

check_PorC()
"""

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input("Enter number: "))

print(is_prime(n))