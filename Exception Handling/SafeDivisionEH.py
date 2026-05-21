while True:
    try:
     n = int(input("Enter first Integer: "))
     m = int(input("Enter second Integer: "))
     print(f"{n}/{m}= {n/m}")
     break
    except ValueError:
     print("Invalid input, Please Enter an Integer")
    except ZeroDivisionError:
      print("Cannot divide with zero, Enter any other integer")