# fibonacci counter while loop
nums = 10
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
for i in range(nums), fibonacci():
    print(fibonacci(i))