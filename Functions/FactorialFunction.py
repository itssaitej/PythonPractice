def factorial(num):
    fact=1
    for i in range(1,num+1):
      fact=fact*i
    return fact
def in_out():
  n=int(input("Enter any number, I shall give you its Factorial..!: "))
  if n < 0:
    print("Factorial not defined")
    in_out()
  else:
   f=factorial(n)
   print(f"{n}! = {f}")
in_out()