def calculate_average(marks, count):
    sum = 0
    for i in marks:
        sum = sum + i
    return sum/ count

n = int(input("Enter total number: "))
marks=[]
for i in range(n):
    m = float(input(f"Enter marks of student {i+1}: "))
    marks.append(m)
    
print("Average: ", calculate_average(marks, n))
