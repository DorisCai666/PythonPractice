'''
Python Classes/Objects
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
'''

# Create a class

class MyClass:
    x = 1

# create an object
obj = MyClass()
print(obj.x)

# The __init__() Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.

class Car:

    def __init__(self,type,color):
        self.type = type
        self.color = color

    def mycolor(self):
        print("Hello my car is " + self.color)

MyCar = Car("Camry", "Green")

print(MyCar.type)
print(MyCar.color)
MyCar.mycolor()

# you can set a value for a property
MyCar.color = "Black"
print(MyCar.color)