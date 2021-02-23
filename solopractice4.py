# Object Lifecycle: creation, manipulation, destruction
# The first stage of the life-cycle of an object is the definition of the class to which it belongs
# Next stage is the instantiation of an instance, when __init__ is called.
# Then the __new__ method of the class is called, and memory is allocated to store the instance. Now the object is ready to be used.
# Other code can now interact with the object, by calling functions on it and accessing its attributes. Eventually, it will finish being used, and can be destroyed.
# Destruction of an object occurs when its reference count reaches zero. Reference count is the number of variables and other elements that refer to an object.
# If nothing is referring to it (has reference count = 0) nothing can interact with it, so it can be safely deleted
# del statement reduces the reference count of an object by one, which often leads to its deletion. Magic method for del statement is __del__
# Garbage collection = deleting objects when they are no longer needed
# Object's reference count increases when it is assigned a new name or placed in a container (list, tuple, dict).
# When an object's reference count = 0, Python automatically deletes it.

a = 42 # create object <42>
b = a # increase ref. count of <42>
c = [a] # increase ref. count of <42>

del a # Decrease ref. count of <42>
b = 100 # Decrease ref. count of <42>
c[0] = -1 # Decrease ref. count of <42>

# A key part of object-oriented programming is encapsulation, which involves packaging of related variables and functions into a single easy-to-use object- an instance of a class
# Data hiding = implementation details of a class should be hidden (private method= a method that external code is discouraged from using), and clean standard interface should be presented for those who want to use the class
# In python - we shoudn't put arbitrary restrictions on accessing parts of a class. So in python its not possible for a method or an attribute to be strictly private
# In python - weakly private methods and attributes have a single underscore at the beginning - this means that they are private and shouldnt be used by external code. But its just a convention and does not stop external code from accessing them
# The only effect this has is that "from module_name import *" won't import variable starting with a single underscore
# In python - strongly private attributes have a double underscore at the beginning of their names. This causes their names to be mangled, so they can't be accessed from outside of the class. 
# The purpose of strongly private attributes isn't so that they are kept private, but to avoid bugs if there are subclasses that have methods or attributes with the same names.
# Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod of a class Spam could be accessed externally with _Spam__privatemethod
#for example:

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg) # <===
# print(s.__egg)

# Methods of objects are normally called by an instance of a class, which is then passed to the self parameter of the method. 
# Class methods on the other hand, are called by a class, which is passed to the cls parameter of the method
# A common use of Class methods are as factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor
# Class methods are marked with a classmethod decorator

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

# new_square is a class method and is called on the class, rather than on an instance of the class. It return a new object of the class cls

# Static methods - similar to Class methods, except they dont receive any additional arguments; they are identical to normal functions that belong to a class.
# Static methods are marked with a staticmethod decorator

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

# Static methods behave like plain functions, except for the fact that you can call them from an instance of the class

## Properties
# Properties provide a way of customizing access to instance attributes. They are created by putting the @property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead
# Common use of a property is to make an attribute read-only

# class Pizzza:
#     def __init__(self, toppings):
#         self.toppings = toppings
    
#     @property
#     def pineapple_allowed(self):
#         return False

# pizzza = Pizzza(["cheese", "tomato"])
# print(pizzza.pineapple_allowed)
# pizzza.pineapple_allowed = True

# Properties can also be set by defining setter/getter functions.
# Setter function set the corresponding property's value
# Getter function gets the value.
# To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.

# class Piza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#         self._pineapple_allowed = False

#     @property
#     def pineapple_allowed(self):
#         return self._pineapple_allowed
#     @pineapple_allowed.setter
#     def pineapple_allowed(self, value):
#         if value:
#             password = input("Enter the password: ")
#             if password == "Sw0rdf1sh!":
#                 self._pineapple_allowed = value
#             else:
#                 raise ValueError("Alert! Intruder!")

# piza = Piza(["cheese", "tomato"])
# print(piza.pineapple_allowed)
# piza.pineapple_allowed = True
# print(piza.pineapple_allowed)

##SIMPLE GAME

# def get_input():
#     command = input(": ").split()
#     verb_word = command[0]
#     if verb_word in verb_dict:
#         verb = verb_dit[verb_word]
#     else:
#         print("Unknown verb {}".format(verb_word))
#         return
    
#     if len(command) >= 2:
#         noun_word = commnd[1]
#         print (verb(noun_word))
#     else:
#         print(verb("nothing"))

# def say(noun):
#     return 'You said "{}"'.format(noun)

# verb_dict = {
#     "say": say,
# }

# while True:
#     get_input()

# The code above takes input from the user, and tries to match the first word with a command in verb_dict. If a match is found, the corresponding function is called.


## QUIZ
# How is a property created? Using the property decorator.
# What is the difference between a class method and a static method? Class methods are passed the calling class, static methods aren't.
# What are the usual parameter names for the calling instance and the calling class? self and cls.
# What method is called just before an object is instantiated? __init__
# What is the automatic process by which unnecessary objects are deleted to free memory? Garbage collection

## Juice maker

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self, second):
        return Juice(self.name + "&" + second.name, self.capacity + second.capacity)


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)


