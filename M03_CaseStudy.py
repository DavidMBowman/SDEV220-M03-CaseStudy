
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

car_type = input("Enter the type of vehicle: ")
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors: ")
roof = input("Enter the type of roof: ")

car = Automobile(car_type, year, make, model, doors, roof)

print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)
