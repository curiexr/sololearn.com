
## Map(function, iterable)
# def add_five(x):
#     return x + 5

# nums = [11, 22, 33, 44, 55]
# result = list(map(add_five, nums))
# print(result)

## Map + lambda
# nums = [11, 22, 33, 44, 55]

# result = list(map(lambda x: x + 5, nums))
# print(result)

# Filter
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x : x%2==0, nums))
print(res)

## Generators --> like lists or tuples, but no indexing, can only be
## iterated through with for/while loops. Yield statement.
## Generators allow to declare a function that behaves like an iterator,
## i.e. it can be used in a for loop

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)

## generators can be converted to lists:

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word
        
print(list(make_word()))

## Decorators --> 
# used to modify functions using other functions
# used to extend functionality of functions that I don't want to modify

# Recursion, factorial ==> 5! = 5 * 4 * 3 * 2 * 1
# n! = n * (n-1)!
# 1! = 1

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))

## this results in Runtime error:
# def sum_to(x):

#    return x + sum_to(x-1)

# print (sum_to(5))

## recursion between two functions:

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)
print(is_odd(17))
print(is_even(23))

def fib(x):

  if x == 0 or x == 1:

    return 1

  else: 

    return fib(x-1) + fib(x-2)

print(fib(4))

## Sets
# key:value pair; does not allow multiple values; unordered; mutable; use 'len'; same with lists; .append in lists, .add in sets; 
# | is union operator that joins two sets together; & gets items only in both sets; 
# - is a difference operator that gets items in first set but not in second;
# ^ is a symmetric difference operator that gets items in either set, but not both

## Itertools
# count() counts up infinitely from a value;
# cycle() infinitely iterates through an iterable e.g. list or string
# repeat() repeats an object

from itertools import count

for i in count(3):
    print(i)
    if i>=11:
        break

# takewhile() takes items from an iterable while a predicate function remains true;
# chain() combines several iterables into one long one;
# accumulate() returns series of accumulated sums;

from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<=6, nums)))

# product() => is a Cartesian product of input iterables;
# permutations() => different combinations of input iterables;
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

nums = [1, 2, 8, 3, 7]
print(list(filter(lambda x: x%2==0, nums)))


# imperative programming - using statements, loops and functions as subroutines
# functional programming - using pure functions, high-order functions and recursion

# OOP - Objects are created using classes. Classes are the focal point of OOP. 
# The class describes what the objec will be, but is separate from the object itself. So basically class is just the object's description or definition.
# Classes are created using the keyword 'class' and an indented block, which contains class methods (which are functions).

# Example of a class below: class named Cat has two attributes: color and legs. Then the class is used to create 3 separate objects of that class
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# What type of object is a method? A function
# __init__ method is the most important method(function) in a class.
# 'self' refers to the object calling the method
# Objects of a class have attributes, which are pieces of data associated with them

print(felix.color)

# the __init__ method is called the class constructor
# Classes can have other methods(definitions) defined to add functionality to them
# all methods must have self as their first parameter.

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")
ellie = Dog("Ellie", "beige")
print(ellie.name)
ellie.bark()

# classes can also have class attributes, by assigning variables within the class body
# class attributes can be accessed either from instances of the class, or the class itself


class Crippledoggo:
    legs = 3
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
fido = Crippledoggo("Fido", "black")
print(fido.legs)
print(Crippledoggo.legs)

# class attributes are shared by all instances of the class

class Student:
    def __init__(self, name):
        self.name = name
    
    def sayHi(self):
        print("Hi from " + self.name + "!")
    
s1 = Student("Amy")
s1.sayHi()

# AttributeError happens when trying to access an instance that isn't defined, e,g,:
# class Rectangle:
#     def __init__(self, weight, height):
#         self.weight = weight
#         self.height = height
# rect = Rectangle(7,9)
# print(rect.color)

# class inheritance - put the superclass name in parentheses after the class name

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
class Catty(Animal):
    def purr(self):
        print("Purr...")
class Doggy(Animal):
    def bark(self):
        print("Woof!")

fido = Doggy("Fido", "yellow")
garmin = Catty("Garmin", "orange")

print(fido.color)
fido.bark()

print(garmin.color)
garmin.purr()

# if a class inherits from another with the same attributes or methods, it overrides them
# circular inheritance is not possible

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dogg(Wolf):
    def bark(self):
        print("Woof")
husky = Dogg("Max", "grey")
husky.bark()

# name, color is a parameter; Max, grey is the argument

# example of indirect inheritance, where one class can inherit from another, and that class can inherit from a third class

class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()
c.another_method()
c.third_method()

# the function "super" is an inheritance-related function that refers to the superclass. Its used to find the method(definition) with a certain name in the superclass.

class A1:
    def spam(self):
        print(1)
    
class B2(A1):
    def spam(self):
        print(3)
        super().spam()

B2().spam()

# Magic Methods (also known as dunders) - have double underscores at the beginning and end of their names.
# Magic Methods are used to create functionality that can't be represented as a normal method(definition)
# one common use of magic methods is operator overloading - this means defining operators for custom classes that allow operators such as +and * to be used on them
# for example, using a magic method __add__ for +

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

# magic methods for common operators:
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for | 

# The expression x + y is translated into x.__add__(y).
# However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called. 

# specialstring division
class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world")
print(spam / hello)

# magic methods for comparisons.
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >= 

# If __ne__ is not implemented, it returns the opposite of __eq__. 

class SpecialeString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialeString("spam")
eggs = SpecialeString("eggs")
spam > eggs

# There are several magic methods for making classes act like containers.
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in 
# __call__ for calling objects as functions
# __int__ , __str__ for converting objects to built-in types

import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont
    
    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]
    
    def __len__(self):
        return random.randint(0, len(self.cont)*2)
vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])



