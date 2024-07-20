# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:

    def __init__(self, brand, model):
        self.__brand = brand #__ lagane se private hojata hai
        self.model = model

    def get_brand(self):
        return self.__brand + "!"


    def fullname(self):
        return f"{self.__brand} {self.model}"

    
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = ElectricCar("Tesla", "Model M", "60.0 kWh")
print(my_car.model, my_car.battery_size, my_car.fullname())

print(my_car.get_brand())