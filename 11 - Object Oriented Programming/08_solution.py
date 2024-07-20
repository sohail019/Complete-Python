# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

# property decorators are used to manage the access to instance attributes


class Car:

    def __init__(self, brand, model):

        self.brand = brand
        self.__model = model  # set the model attribute as a private by using double underscore. it ensures this should not be accessed directly

    @property #  to define a getter method without providing a corresponding setter method , it ensures the attribute can read only but can't directly modify

    def model(self):
        return self.__model


my_car = Car('Tata', 'Safari')

# let's change the value of model by overwriting it
my_car.model = "Nexon" # gives error AttributeError
print(my_car.model) # Nexon
