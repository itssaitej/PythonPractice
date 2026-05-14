"""
keys = ["Username","Password"]

register_Info={}
login_Info={}

login="False"

print("User Registeration:")
for key in keys:
    register_Info[key]=input(f"Enter {key}: ")


print("Login:")
while login=="False": 
 for key in keys:
    login_Info[key]=input(f"Enter {key}: ")

 mismatched_keys = [k for k in keys if login_Info[k] != register_Info[k]]

 if mismatched_keys:
    print(f"{mismatched_keys} does not match")
 else:
    login="True"
    print("Login Successful...!")

"""
print("User Registeration:")
register_username = input("Enter username: ")
register_password = input("Enter password: ")

print("Login:")
while True:
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")

    if login_username == register_username and login_password == register_password:
        print("Login Successful!")
        break
    elif login_username != register_username:
        print("Username not found")
    else:
        print("Incorrect password")