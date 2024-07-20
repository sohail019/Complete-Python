# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:

    def __init__(self, brand, model, fuel_type):

        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    
class ElectricCar(Car):

    def __init__(self, brand, model, fuel_type, battery_size):

        super().__init__(brand, model, fuel_type)

        self.battery_size = battery_size

my_normal_car = Car("Toyota", "Fortuner", "Diesel")

print("Brand: " + my_normal_car.brand + " - Model: " + my_normal_car.model + " - Fuel Type: " + my_normal_car.fuel_type)

my_electric_car = ElectricCar("Tesla", "Model S", "Battery power", "60.0 kWh")

print("Brand: " + my_electric_car.brand + " - Model: " + my_electric_car.model + " - Fuel Type: " + my_electric_car.fuel_type + " - Battery Size: " + my_electric_car.battery_size)
