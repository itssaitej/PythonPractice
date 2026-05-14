sm=[]
total=0
for i in range(0,5):
  sm.append(i)
  sm[i]=int(input(f"Marks of Student {i+1}: ")) 

for i in range(5):
  total=total+sm[i]

for i in range(5):
  for j in range(0,4):
    if sm[j]>sm[j+1]:
      temp=sm[j]
      sm[j]=sm[j+1]
      sm[j+1]=temp

print(f"Average marks of the 5 students is: {total/5}")
print(f"The Highest marks: {sm[4]}")
print(f"The Lowest marks: {sm[0]}")