## Pythonicness and Packaging
# Zen of python == set of principles that serves as a guide to programming the Pythoneer way. To access Zeon of Python, use this: "import this"
import this

## PEP => Python Enhancement Proposals, are suggestions for improvements to the language, made by experienced Python developers
# PEP 8 is a style guide on the subject of writing readable code. It contains a number of guidelines in reference to variable names, which are summarized below:
# 1. Modules should have short, all-lowercase names;
# 2. class names should be in the CapWords style;
# 3. most variables and function names should be lowercase_with_underscores;
# 4. constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
# 5. names that would clash with Python keywords (such as 'class' or 'if') should have a trailing underscore

# PEP 8 also recommends using spaces around operators and after commas to increase readability
# Whitespace should not be overused, e.g. avoid having any space directly inside any type of brackets.
# Lines shoudn't be longer than 80 characters;
# 'from module import*' should be avoided;
# there should only be one statement per line.

# PEP 20: The Zen of Python
# PEP 257: Style Conventions fo Docstrings

## Function Arguments
# in python, functions can have a varying number of arguments. 
# using *args as a function parameter enables you to pass a number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function.
# The parameter *args must come after the named parameters to a function. The name args is just a convention; you can choose to use another
#  For example:

def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

# the parameter *args must come after the named parameters to a function. The name args is just a convention; you can choose to use another.

# Default Values:
# named parameters to a function can be made optional by giving them a default value. These must come after named parameters without a default value:

def function(x, y, food="spam"):
    print(food)

function(1, 2)
function(3, 4, "egg")

# In case the argument is passed in, the default value is ignored. If the argument is not passed in, the default value is used.

# **kwargs (keyword arguments) allow you to handle named arguments that you have not defined in advance.
# The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.

def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

# a and b are the names of the arguments that we passed to the function call

## Tuple Unpacking
# Tuple unpacking allows you to assign each item an iterable (often a tuple) to a variable.

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

# this can also be used to swap variables by doing a,b = b,a because b,a on the right side form the tuple(b,a) which is then unpacked.

x,y = [1,2]
x,y = y,x
print(x)

# a variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables:

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

a = range(0,20)
for a in range(0,20):
    print(a)

## Ternary Operator
# Conditional expressions provide the functionality of if statements while using less code. They shouldn't be oversued, as they can reduce readability
# they are often used when assigning variables
# Conditional expressions are applications of the Ternary Operator
# Ternary operator is called like that because it takes 3 arguments

a = 7
b = 1 if a >=5 else 42
print(b)

status = 1
msg = "Logout" if status == 1 else "Login"
print(msg)

## Else
# The else statement is most commonly used along with the if statement, but it can also follow a for or while loop, which gives it a different meaning. 
# With the for or while loop, the code within it is called if the loop finishes normally (when a break statement does not cause an exit from the loop). 

for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

# essentially, "else" is used only when the for loop doesn't break and fully finishes
# else can also be used with try/except statements. In this case, the code is executed only if no error occurs in the try statement

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

## __main__
# Most Python code is either a module to be imported, or a script that does something. 
# However, sometimes it is useful to make a file that can be both imported as a module and run as a script. 
# To do this, place script code inside if __name__ == "__main__". This ensures that it won't be run if the file is imported. 

def function():
    print("This is a module function")

if __name__=="__main__":
    print("This is a script")

# quiz: Print "Welcome" if the script is imported, and "Hi" if it is not imported:
if __name__=="__main__":
    print("Hi")
else:
    print("Welcome")

# web frameworks: Django, CherryPy, Flask
# data scraping: BeautifulSoup (better than building my own scraper with regular expressions)
# mathematical computing: matplotlib (allows to create graphs based on data in Python), numpy (use of multi-dimensional arrays that are much faster than python's nested lists, also allows matrix transformations on arrays. SciPy has extentions to the functionality of NumPy).
# game development: pygame (2D), Panda3D (3D)

## Packaging
# packaging refers to putting modules you have written in a standard format, so that other programmers can install and use them with ease. This involves the use of modules 'setuptools' and 'distutils'.
# first step in packaging is to organize existing files correctly. Place all of the files you want to put in a library in the same parent directory. This directory should also contain a file called __init__.py, which can be blank but must be present in the directory. This directory should also contain a file called __init__.py, which can be blank but must be present in the directory. 

# example directory structure:
# Sololearn/
#   LICENSE.txt
#   README.txt
#   setup.py
#   sololearn/
#       __init__.py
#       sololearn.py
#       sololearn2.py

# next step in packaging is to write the setup.py file. This file contains information necessary to assemble the package so it can be uploaded to PyPI and installed with pip(name, version, etc.)
# Example of a setup.py file:

# from distutils.core import setup

# setup(
#     name='Sololearn',
#     version='0.1dev',
#     packages=['sololearn',],
#     license='MIT',
#     long_description=open('README.txt').read(),
# )

# After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution (an executable installer)
# To build a source distribution, use the command line to navigate to the directory containing setup.py, and run the command 'python setup.py sdist'.
# Run 'python setup.py bdist' to build a binary distribution.
# Use python setup.py register, followed by 'python setup.py sdist upload' to upload a package.
# finally, install a package with python setup.py install

# to convert python scripts to executables, for windows use py2exe, for mac use py2app, PyInstaller, cx_Freeze.

## Test "Adding Words"
# You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
# The function should be able to take a varying number of words as the argument.

# Sample Input
# this
# is
# great

# Sample Output
# this-is-great 


def concatenate(*args):
    oneliner=''
    for word in args:
        if oneliner == '':
            oneliner = oneliner + word
        else:
            oneliner = oneliner + '-' + word
    return oneliner
print(concatenate("I", "love", "Python", "!"))
