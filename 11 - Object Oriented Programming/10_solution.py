# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Car:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model

class Battery:
    def battery_info(self):
        return 'This is battery'

class Engine:
    def engine_info(self):
        return 'This is Engine'

# Multiple Inheritance: Allows a class to inherit from more than one parent class. it enables subclass to use methods from multiple base class.

class ElectricCar(Battery, Engine, Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_electric_car = ElectricCar("Tesla", "Model M", "60.9 kWh")

print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.battery_info())
print(my_electric_car.engine_info())
print(my_electric_car.battery_size)

