nums = [1, 2, 3]
numz = nums + [4, 5, 6]
print(numz*3)
print(5 in numz)

words = ['abstract1', 'abstract3', 'abstract3', 'abstract3']
index = 1
words.insert(index, 'abstract2')
print(words.count('abstract3'))
print(words)

i = 1
while i <= 5:
    print(i)
    i += 1
print('Finished!')

nums = list(range(20, 5, -2))
print(nums)

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])


def function(variable):
    variable += 1
    print(variable)

function(7)


def add(x, y):
    return x + y

def do_twice(func,x, y):
    return func(x, y), func(x, y)

a = 5
b = 10
print(do_twice(add, a, b))

import random

for i in range(5):
    print(i)

try:
    num1 = 8
    num2 = 0
    print(num1 / num2)
    print("Calculation complete")
except ZeroDivisionError:
    print("Cannot divide by Zero!")
    print("FATAL ERROR")

# write / open file
# open("Documents/sololearnpractice1.py, "r")


#file = open("newfile.txt", "w")
#file.write("Some new text")
#file.close()

#file = open("newfile.txt", "r")
#print("Reading new contents")
#print(file.read())
#print("Finished")
#file.close()

#file = open("newfile.txt", "w")
#file.write("Additional text")
#file.close()

# msg = "This text was added for a reason."
# file = open("newfile.txt", "w")
# amount_written = file.write(msg)
# print(amount_written)
# file.close()

#try:
#    f = open("filename.txt")
#    print(f.read())
#finally:
#    f.close()

# with open("newfile.txt") as f:
#     for bookname in f.readlines():
#         if "\n" in bookname:
#             print(bookname[0]+str(len(bookname)-1))
#         else:
#             print(bookname[0]+str(len(bookname)))

# None is used to represent absence of value

def some_func():
    print("Hi!")

foo = print()
if foo == None:
    print(1)
else:
    print(2)

# Dictionaries
ages = {"Dave": [24, 33, 48], "Ali": 29, "Terminus": 99}
print(ages["Dave"])

# test = {}
# print(test[0])

squares = {1:1, 2:4, 3:"error", 4:16,}
squares[8] = 64
squares[3] = 9
print(squares)
print(8 in squares)
print(squares.get(8))

fib = {1: 1, 2: 1, 3: 2, 4: 3}

print(fib.get(3, 8), fib.get(5, 9))

mytuple = ("spam", "eggs", "sausages",)
print(mytuple[0])

mylisty = [0, 1, 4, 9, 16, 25, 36]
print(mylisty[3:1:-1])

# LIST COMPREHENSION
cubes = [i**3 for i in range(5)]
print(cubes)

# string formatting FORMAT METHOD

a = "{x},{y}".format(x=5, y=12)
print(a)
print(", ".join(["we", "live", "in"]))