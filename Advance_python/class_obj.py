
#Inheritance
class Father:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
f=Father("Ram",50)
f.display()    
super = "college"
class Son(Father):
    def __init__(self,name,age,language,clour):
        self.name = name
        self.age = age
        self.language = language
        self.clour = clour

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
        print("Father's College:",super)
s=Son("Shiv",20,"Python","Blue")
s.display()


#polymorphism
class Animal:
    def speak(self):
        print("Animal speaks")
        
class Cat(Animal):
    def speak(self):
        print("Cat meows")
        
class Dog(Animal):
    def speak(self):
        print("Dog barks")
for animal in (Animal(), Cat(), Dog()):
    animal.speak()
    
    
#Encapsulation
class Car:              
    def __init__(self, name, max_speed):
        self.__name = name
        self.__max_speed = max_speed

    def drive(self):
        print(f"{self.__name} is driving at {self.__max_speed} km/h")
c = Car("BMW", 200)
c.drive()        
        
#Abstraction
from abc import ABC, abstractmethod 

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

car = Car()
car.start_engine()