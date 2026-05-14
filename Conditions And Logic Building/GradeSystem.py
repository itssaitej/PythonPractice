mathMarks=int(input("Enter the marks you gained in Mathematics out of 100: "))
scienceMarks=int(input("Enter the marks you gained in Science out of 100: "))
englishMarks=int(input("Enter the marks you gained in English out of 100: "))
hindiMarks=int(input("Enter the marks you gained in Hindi out of 100: "))
teluguMarks=int(input("Enter the marks you gained in Telugu out of 100: "))
socialMarks=int(input("Enter the marks you gained in Social Studies out of 100: "))

totalMarks=mathMarks+scienceMarks+englishMarks+hindiMarks+teluguMarks+socialMarks
avgMarksPercent=totalMarks / 6
if avgMarksPercent >= 90:
    print(f"Congratulations.....!!! You have passed in Distinction with an A GRADE\nYour Total Marks are {totalMarks} out of 600, equal to a percentage of {avgMarksPercent}%")
elif avgMarksPercent >= 75:
    print(f"Congratulations.....!!! You have passed in FirstClass with a B GRADE\nYour Total Marks are {totalMarks} out of 600, equal to a percentage of {avgMarksPercent}%")
elif avgMarksPercent >= 50:
    print(f"Congratulations.....!!! You have passed in SecondClass with a C GRADE\nYour Total Marks are {totalMarks} out of 600, equal to a percentage of {avgMarksPercent}%")    
else:
    print(f"We are sorry but you have failed with a total of {totalMarks} Marks out of 600, equal to a percentage of {avgMarksPercent}%")