# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# creating class syntax
class Car:
    # init is a special method called constructor. It gets called automatically when you create a new object of the Car class

    def __init__(self, brand, model): # self refers to the instance of the class being created!! 
    # brand and model are parameters that will be passed in when creating a Car Object

        # Assign the values of brand and model passed into corresponding attributes of the Car object
        self.brand = brand 
        self.model = model

# Creating a car object
my_car = Car('Ford', 'Mustang')
print(my_car.brand + ' - ' + my_car.model)

# Creating another car object
my_another_car = Car('Toyota', 'Fortuneer')
print(my_another_car.brand + ' - ' + my_another_car.model)