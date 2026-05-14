n=int(input("Enter the number of stars you wanna see in the last line: "))

for i in range(1,n+1):
   for j in range(i):
     print("*", end=" ")
   print("")