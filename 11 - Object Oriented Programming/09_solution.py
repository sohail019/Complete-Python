# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_electric_car is an instance of Car and ElectricCar.

class Car:

    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model

    
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = Car('Tata', 'Safari')
print(my_car.brand, my_car.model)


my_electric_car = ElectricCar('Tesla', 'Model M', '60.0 kWh')
print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.battery_size)

# isinstance() - function checks if an object is an instance of a specified class or subclass thereof
# Syntax - isinstance(object, class_name)

print(isinstance(my_electric_car, Car)) # returns True because 'ElectricCar' inherits from 'Car'

print(isinstance(my_electric_car, ElectricCar)) # returns True because 'my_electric_car' is an instance of 'ElectricCar'