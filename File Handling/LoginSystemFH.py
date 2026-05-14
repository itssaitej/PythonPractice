"""
registerusername=input("Enter a username: ")
registerpassword=input("Enter a password: ")
with open("RegisterInfo.txt", "w") as file:
    file.write(f"{registerusername}")
    file.write(f"\n{registerpassword}")    
print("Registration Successful")
with open("RegisterInfo.txt","r") as file:
    register=file.readlines()
    r_username = register[0].strip()
    r_password = register[1].strip()

print(f"{r_username}\n{r_password}")

while True:
 login_username=input("Enter your username: ")
 login_password=input("Enter your password: ")
 if login_username==r_username and login_password==r_password:
    print("Login Successfull")
    break
 elif login_username!=r_username:
    print("User not found")
 elif login_password!=r_password :
    print("Wrong Password")

"""
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("RegisterInfo.txt", "w") as file:
        file.write(f"{username}\n")
        file.write(password)
    print("Registration Successful")

def read_user():
    with open("RegisterInfo.txt", "r") as file:
        register = file.readlines()
        username = register[0].strip()
        password = register[1].strip()
    return username, password

def login_user(saved_username, saved_password):
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == saved_username and password == saved_password:
            print("Login Successful")
            break
        elif username != saved_username:
            print("User not found")
        else:
            print("Wrong Password")

register_user()
u, p = read_user()
login_user(u, p)