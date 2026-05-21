def get_numbers():
    while True: 
     try: 
      nums = []
      count = int(input("How many numbers? "))
      for i in range(count):  
        num = float(input(f"Enter number {i+1}: "))
        nums.append(num) 
      return nums 
     except ValueError:
      print("Invalid Input") 
    


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
            raise ZeroDivisionError

        result /= num

    return result


while True:
    try:
     print("\n1.Add")
     print("2.Subtract")
     print("3.Multiply")
     print("4.Divide")
     print("5.Exit")
    
     
     choice = int(input("Enter choice: "))

     if choice == 5:
        print("Goodbye....See You Next Time...!")
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
    except ValueError:
        print("Invalid choice")