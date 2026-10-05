# Decorators using Function methond
def greet_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@greet_decorator
def greet():
    print("Hello, welcome!")

greet()
print("\n------------------------")
#Decorators using Class method
def logger(func):
    def wrapper(*args, **kwargs):
        print("Method is being called")
        result = func(*args, **kwargs)
        print("Method execution finished")
        return result
    return wrapper

class Student:
    @logger
    def show(self, name):
        print(f"Student name: {name}")

s = Student()
s.show("Shreyaa")