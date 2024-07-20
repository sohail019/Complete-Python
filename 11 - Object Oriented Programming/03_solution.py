# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = Car('Ford', 'Mustang')
print(my_car.brand)
print(my_car.model)

my_another_car = ElectricCar('Tesla', 'Model S', '60.0 kWh')
print(my_another_car.brand)
print(my_another_car.model)
print(my_another_car.battery_size)
print(my_another_car.full_name())
