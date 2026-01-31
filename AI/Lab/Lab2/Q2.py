# Task 2
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.employee_id = id

  def calculate_salary(self):
    pass

class FullTimeEmployee(Employee):
  def __init__(self, name, id, salary):
    super().__init__(name, id)
    self.monthly_salary = salary
  def calculate_salary(self):
    print(f"Employee ID: {self.employee_id}\nEmployee name: {self.name}\nSalary: {self.monthly_salary} /per month")

class PartTimeEmployee(Employee):
  def __init__(self, name, id, hours, rate):
    super().__init__(name, id)
    self.hours_worked = hours
    self.hourly_rate = rate
  
  def calculate_salary(self):
    print(f"Employee ID: {self.employee_id}\nEmployee name: {self.name}\nRate: {self.hourly_rate} /per hour\nHours Worked: {self.hours_worked}\nSalary: {self.hours_worked * self.hourly_rate} /-")


e1 = PartTimeEmployee("Laiba", 101, 5, 20)
e1.calculate_salary()
print("\n")
e2 = FullTimeEmployee("Laraib", 110, 30000)
e2.calculate_salary()
