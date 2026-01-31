from ast import And
# Task 3
class Result:
  def __init__(self, name, marks=0):
    self.name = name
    self.__marks = marks

  def set_marks(self, marks):
    if 0 <= marks <= 100:
      self.__marks = marks
      print(f"Marks for {self.name} are set to {self.__marks}")
    else:
      print("Marks must be between 0 and 100 (inclusive)")
  
  def get_marks(self): 
    return self.__marks
    
  def calculate_grade(self):
    if self.__marks >= 80:
      return "A"
    elif self.__marks >= 70:
      return "B"
    elif self.__marks >= 60:
      return "C"
    else:
      return "F"

s1 = Result("Laiba")
s1.set_marks(85)
print(f"Name: {s1.name}\nGrade: {s1.calculate_grade()}\n")
s2 = Result("Ali", 67)
print(f"Name: {s2.name}\nMarks: {s2.get_marks()}\nGrade: {s2.calculate_grade()}")

print(f"\nChanging {s2.name}'s marks:")
s2.set_marks(-19)
s2.set_marks(19)
print(f"Grade: {s2.calculate_grade()}\n")
