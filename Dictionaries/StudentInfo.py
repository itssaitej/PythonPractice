keys = ["Name", "Age", "Marks"]

Student_Info={}



for key in keys:
    Student_Info[key]=input(f"Enter {key}: ")

for key in keys:
    print(f"{key}: {Student_Info[key]}")