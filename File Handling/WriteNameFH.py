n=input("Enter Your Name: ")
with open("names.txt", "w") as file:
    file.write(f"I am {n}..!")