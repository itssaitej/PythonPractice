year=int(input("Enter a year to check whether it's a Leap Year or not:"))

if (year%4==0 and not(year%100==0)) or year%400==0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")