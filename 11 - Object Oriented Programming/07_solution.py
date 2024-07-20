# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

# static method: it is defined using the @staticmethod decorator.
# it does not operate on an instance of a class(i.e it does not take 'self' as the first parameter), and it does not have access to instance-specific data.
# However, we can still call it on both the class itself and on instance of the class

class Car:

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

    @staticmethod # ye decorator
    def general_description():
        return "Cars is a motor vehicle with wheels"


my_car = Car("Tata", "Nexon")

print(my_car.general_description()) # this will work

print(Car.general_description()) # this will also work

