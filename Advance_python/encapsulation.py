#Encapsulation
class Car:              
    def __init__(self, name, max_speed):
        self.__name = name
        self.__max_speed = max_speed

    def drive(self):
        print(f"{self.__name} is driving at {self.__max_speed} km/h")
c = Car("BMW", 200)
c.drive()       