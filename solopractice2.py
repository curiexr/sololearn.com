
print(", ".join(["we", "live", "in"]))

a = "{x},{y}".format(x=5, y=12)
print(a)

# JOIN == turns list into a string print(", ".join(["we", "live", "in"]))
# SPLIT == turns a string into a list print("spam, eggs, ham".split(", "))

# max, min, abs, round, sum

print(abs(-30),2)
#if all 
#if any

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

# enumerate is used to iterate through values and indices of a list simultaneously
for v in enumerate(nums):
        print(v)

# Text Analyzer
# def countcharacter(text, char):
#     count = 0
#     for i in text:
#         if i == char:
#             count += 1
#     return count

# filename = input("Enter a filename: ")
# with open(filename) as f:
#     text = f.read()

# print(countcharacter(text, "r"))

a = (2, 3, 5)
print(a)
print(a[1:2])
print(min(55, 44, 42))
a = ["abra", "ca", "dabra"]
print(a[0])

# high order functions -- take other functions as arguments

def apply_twice(func, arg):
    return func(func(func(arg)))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

# LAMBDA FUNCTIONS
def my_func(f, arg):
    return f(arg)
print(my_func(lambda x: 2*x*x, 5))

print((lambda x: x**2 + 5*x + 4) (-4))

double = lambda x: x * x
print(double(7))


