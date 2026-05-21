while True:
    try:
     num = int(input("Enter an Integer: "))
    except ValueError:
     print("Invalid Integer Entered")
    else:
     print("Valid Integer Entered")
     break