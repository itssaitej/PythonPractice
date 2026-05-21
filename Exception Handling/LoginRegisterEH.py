def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("RegisterInfo.txt", "w") as file:
        file.write(f"{username}\n")
        file.write(password)
    print("Registration Successful")

def read_user(n):
    with open(f"{n}.txt", "r") as file:
        register = file.readlines()
        username = register[0].strip()
        password = register[1].strip()
    return username, password
      
         

def login_user(saved_username, saved_password):
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == saved_username and password == saved_password:
            print("Login Successful")
            break
        elif username != saved_username:
            print("User not found")
        else:
            print("Wrong Password")

register_user()
while True: 
  try:
   n=input("Enter the file name you have saved your data in: ")
   is_empty = True
   with open(f"{n}.txt", "r") as file:
        for line in file:
            if line.strip():
                is_empty = False
                break  
                
   if is_empty:
        print("The file is empty or only contains whitespace.")
        register_user()
   else:
        print("The file contains valid data.")
   u, p = read_user(n)        
  except FileNotFoundError:
   print("File Doesn't Exist")
   continue
   
  login_user(u, p)
  break 