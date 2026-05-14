registerusername=input("Enter a username: ")
registerpassword=input("Enter a password: ")
age=int(input("Enter your age: "))
gender=input("Specify your gender: ")

print("Registration Completed.....!")
attempts=3

while attempts>=0:
 loginUsername=input("Enter your username: ")
 loginPassword=input("Enter your password: ")
 if registerpassword==loginPassword and registerusername==loginUsername:
    print("Login Successful...!")
    break
 elif registerusername!=loginUsername:
    print("This Username doesn't exists")
 elif registerusername==loginUsername and registerpassword!=loginPassword:
    print("Incorrect Password")
    attempts=attempts-1