"""
def calculator():
    print(" 1. ADD \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. End")
    n=int(input("Choose what you wanna do: "))
    
    if n==1:
        print("So you wanna add, then")
        add()
    elif n==2:
        print("So you wanna subtract, then")
        subtract()
    elif n==3:
        print("So you wanna multiply, then")
        multiply()
    elif n==4:
        print("So you wanna divide, then")
        divide()
    elif n==5:
        print("See You Next Time...!")
    else:
        print("Invalid option, Please")
    return n

def add():
    s=0
    l=int(input("Enter how many numbers you wanna add: "))
    for i in range(0,l):
     a=int(input("Enter the numbers you wanna add: "))
     s=s+a
    print(f"The sum of the given numbers = {s}")

def subtract():
    l=int(input("Enter how many numbers you wanna subtract: "))  
    if l>0:
     s=int(input("Enter the first number you wanna subtract from: "))
     for j in range(2,l+1): 
      a=int(input(f"Enter the number {j} : "))
      s=s-a
     print(f"The subtraction of the given numbers = {s}")
    else:
     print("Please enter a positive input")
     subtract()
      
def multiply():
    l=int(input("Enter how many numbers you wanna multiply: "))  
    if l>0:
     s=int(input("Enter the first number you wanna start multiplying from: "))
     for j in range(2,l+1): 
      a=int(input(f"Enter the number {j} : "))
      s=s*a
     print(f"The Product/Multiplication of the given numbers = {s}")
    else:
     print("Please enter a positive input")
     multiply()

def divide():
    l=int(input("Enter how many numbers you wanna divide: "))  
    if l>0:
     s=float(input("Enter the first number you wanna divide: "))
     for j in range(2,l+1): 
      a=int(input(f"Enter the number {j} : "))
      if a==0:
       print("Cannot divide with 0")
       divide()
      s=s/a
     print(f"The division of the given numbers = {s}")
    else:
     print("Please enter a positive input")
     divide()

n=calculator()
    
while n!=5:
   n=calculator()

"""
def get_numbers():
    nums = []

    count = int(input("How many numbers? "))

    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        nums.append(num)

    return nums


def add(nums):
    total = 0

    for num in nums:
        total += num

    return total


def subtract(nums):
    result = nums[0]

    for num in nums[1:]:
        result -= num

    return result


def multiply(nums):
    result = 1

    for num in nums:
        result *= num

    return result


def divide(nums):
    result = nums[0]

    for num in nums[1:]:

        if num == 0:
            return "Cannot divide by zero"

        result /= num

    return result


while True:

    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Goodbye!")
        break

    nums = get_numbers()

    if choice == 1:
        print(add(nums))

    elif choice == 2:
        print(subtract(nums))

    elif choice == 3:
        print(multiply(nums))

    elif choice == 4:
        print(divide(nums))

    else:
        print("Invalid choice")