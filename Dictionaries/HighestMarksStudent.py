Marks = {}
print("Enter Name-Marks pairs (type 'exit' as the value for 'Name' to stop the entries):")

while True:
    key = input("Name: ")
    if key.lower() == 'exit':
        break
    value = int(input("Marks: "))
    Marks[key] = value

for key in Marks:
    print(key,Marks[key])

topper=max(Marks,key=Marks.get)

print(f"The Topper of the class is {topper} by obtaining {Marks[topper]}")