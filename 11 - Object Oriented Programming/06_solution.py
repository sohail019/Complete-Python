# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car = 0 # variable declare
    
    def __init__(self, brand, model):


        self.brand = brand
        self.model = model

        Car.total_car += 1


Car('Tata', 'Nexon')
Car('Tata', 'Safari')
Car('Ford', 'Mustang')
Car('Tesla', 'Model M')

print("Total Car is: ", Car.total_car) # 4