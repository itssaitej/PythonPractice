num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", abs(num1 - num2))
print("Product:", num1 * num2)
if not(num2==0):
    print("Division:", num1 / num2)
else:
    print("Division not possible (cannot divide by zero)")