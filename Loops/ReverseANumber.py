n=abs(int(input("Enter a number: ")))
print(f"Original Number: {n}")
rev=0
while n>0:
 digit=n%10
 rev=rev*10+digit
 n=n//10
print(f"After reversing the digits of the number: {rev}")