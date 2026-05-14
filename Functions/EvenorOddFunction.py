def check(num):
    return "Even" if num % 2 == 0 else "Odd"
t= check(int(input("Enter a number: ")))
print(f"the given number is an {t} number")