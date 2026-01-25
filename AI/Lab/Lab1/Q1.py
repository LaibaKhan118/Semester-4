name = input("Enter student name: ")
marks = float(input("Enter student marks: "))

if(marks >= 80):
    grade = 'A'
elif(marks >= 70):
    grade='B'
elif(marks >= 50):
    grade='C'
else:
    grade='F'

print("Grade: ", grade)
