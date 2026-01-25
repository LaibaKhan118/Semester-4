records={}
count=int(input('Enter number of students: '))
for i in range(count):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    records[name]=marks

print("\nStudent Records:")
for name, marks in records.items():
    print(name, " : ", marks)
