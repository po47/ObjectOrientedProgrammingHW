# ObjectOrientedProgrammingHW

**Encapsulation**

In this principle a private object has private fields including method(s) and variables. 
Other objects can call on the private object using public methods.
However, these public methods can't directly modify the private fields of that object. 

    class Bear(object):
        def sound(self):
            print("Groarrr")
    
    
    class Dog(object):
        def sound(self):
            print("Woof woof!")
    
        def makeSound(animalType):
            animalType.sound()



**Abstraction**

This concept aims to handle complex internal implementation by hiding this information for users. 
Thus, only the most relevant information is revealed including high-level mechanisms for using the objects.  

    def calculation():
        print("This is a simple calculator")
        x = int(input("Enter a value"))
        y= int(input("Enter another value"))
    
        print("Press 1 to add\n Press 2 to subtract")
        option = int(input("--> "))
    
        def add():
            res = x + y
            print(res)
    
        def subtract():
            res = x - y
            print(res)
    
        if (option ==1):
            add()
    
        elif (option == 2):
            subtract()

    calculation()








**Inheritance**

In this principle a class is created that holds methods. This class is referred to as the parent class. 
A child class is created and it takes the methods and fields of the parents class. 
However, it can also create its own methods and variables which makes this class unique and different from the parent class.

     
     class Robot:
    
        def __init__(self, name):
            self.name = name
    
        def say_hi(self):
            print("Hi, I am " + self.name)
    
    
    class PhysicianRobot(Robot):
        pass
    
    
    x = Robot("Marvin")
    y = PhysicianRobot("James")
    
    print(x, type(x))
    print(y, type(y))
    
    y.say_hi()
    

**Polymorphism**

This principle describes the notion that objects can access other objects using the same interface. 
So, an object can have its methods and the child classes can calculate or implement its own verison of the parent method. 

    class Bear(object):
        def sound(self):
            print("Groarrr")
    
    
    class Dog(object):
        def sound(self):
            print("Woof woof!")
    
        def makeSound(animalType):
            animalType.sound()
    
    
    bearObj = Bear()
    dogObj = Dog()
    
    makeSound(bearObj)
    makeSound(dogObj)