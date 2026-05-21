print("Enter file name: ")
while True:
 try:
  n=input()
  with open(f"{n}.txt", "r") as file:
    data = file.read()
 except FileNotFoundError:
  print("Please enter an existing file's name: ") 
 else: 
  print(data)
  break
