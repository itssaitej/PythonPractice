def name():
  while True:
   try:
    user_name = input("Please enter your name: ").strip()
    
    if user_name.isalpha():
        print(f"Hey, {user_name}!")
        break
    else:
       print("Invalid input. Please use letters only (no numbers or symbols).") 
   except ValueError:
        print("Invalid input. Please use letters only (no numbers or symbols).")
  return user_name

def age(n):
   while True:
      try:
         user_age=int(input("Enter your Age: "))
         if user_age<0:
            print("Please Enter a valide age greater than or equal to 0")
         else:
            print(f"Ohhh...{n},so you are {user_age} years young...!")
            break
      except ValueError:
         print("Age must be in numbers only.")
         
   return user_age

def marks(n):
   while True:
      try:
         user_tenth_perc=float(input("Enter your 10th percentile: "))
         if user_tenth_perc < 0 or user_tenth_perc > 100:
            print(f"{n} Please enter your 10th percentile >=0 or <=100")
            continue
         elif  user_tenth_perc<40:
            print(f"{n}...! So sorry that you have failed in your tenth with a {user_tenth_perc}%, Please don't lose hope you can try once again...!")
         elif  user_tenth_perc<60:
            print(f"{n}...! So you have passed in your tenth in Second Class level with a {user_tenth_perc}%. Good")
         elif  user_tenth_perc<75:
            print(f"{n}...! So you have passed in your tenth in First Class level with a {user_tenth_perc}%, Very Good")
         elif  user_tenth_perc<100:
            print(f"{n}...! So you have passed in your tenth at a Distinction level with a {user_tenth_perc}%, Congratulations")
         else:
            print(f"{n} You have gained {user_tenth_perc}%...! Congratulations and very prouf of you...!")
         break
      except ValueError:
         print("Please a number value only")
   return user_tenth_perc

n=name()
a=age(n)
p=marks(n)