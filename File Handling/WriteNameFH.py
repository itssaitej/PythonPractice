n=input("Enter Your Name: ")
with open("name.txt", "w") as file:
    file.write(f"I am {n}..!")