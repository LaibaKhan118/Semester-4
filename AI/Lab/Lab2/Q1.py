#Task 1
class Vehicle:
  def __init__(self, id, brand, rent):
    self.vehicle_id = id
    self.brand = brand
    self.rent_per_day = rent

  def display_details(self):
    print(f" Vehicle ID: {self.vehicle_id}\n Brand: {self.brand}\n Rent: {self.rent_per_day} /per day")
  
  def calculate_rent(self, days):
    rent = self.rent_per_day * days
    print(f"Total rent for {days} days: {rent}")
  
v1 = Vehicle(1, "Toyota", 5000)
print("Vehicle Details:")
v1.display_details()
v1.calculate_rent(7)
v1.calculate_rent(12)

v2 = Vehicle(2, "Honda", 4500)
print("\nVehicle Details:")
v2.display_details()
v2.calculate_rent(30)
v2.calculate_rent(16)
