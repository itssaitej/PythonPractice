n=input("Enter A String: ")
with open("newfile.txt", "w") as file:
    file.write(n)
with open("newfile.txt", "r") as file:
    data = file.read()
print(len(data.split()))