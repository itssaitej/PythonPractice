i=1
with open("names.txt", "a") as file: 
 while True:
  n=input("Enter Your Name: ")
  if n.lower=="exit":
   break
  file.write(f"{i}. {n}\n")
  i=i+1