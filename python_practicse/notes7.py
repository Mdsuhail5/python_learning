# lambda :Small and Anonymous functions
# Any number of arguments, but only one expression
# lambda arugment:expression

def a(x): return x+5


print(a(10))


def power(n):
    return lambda x: x**n


square = power(2)  # so this line becomes lambdax:x**2
cube = power(3)

print(square(4))
print(cube(3))

# Decorators: used to modify behaviour of another function by adding some lines to it
# a function takes another function as argument and have a function inside it and defines some lines
# print the argument function and print the rest of the line and can use @decorator_name to define the arg funciton


def my_decorator(func):
    def wrapper():
        print('Something is happening BEFORE the function is called')
        func()
        print('Something is happening AFTER the function is called')
    return wrapper


@my_decorator
def say_hello():
    print('Hello')


say_hello()

# Generators: function that pauses the excecution of the function
# it basically loads the values when called return one after the other instead of return whole values at once
# it produces iterators on the fly
# the generator is identified by yield keyword
# Use Cases:
# Generators are perfect for:
# Creating infinite sequences (like an endless stream of numbers).
# Handling large datasets without loading everything into memory.
# Building data pipelines and processing streams of data efficiently.


def gen():
    yield 1
    yield 2
    yield 3
    yield 4


for x in gen():
    print(x)
    print(x, 'is a number')
    print(x, 'runs from a generator')
    print(x, 'will move to next yield')
    print('============================')


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4


y = numbers()
print(next(y))
print(next(y))
print(next(y))
print(next(y))


def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b


for x in fib(8):
    print(x)

# OR
x = fib(8)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# converting integer list to float list

c = [2, 3, 6, 8]
c2 = []
for x in c:
    c2.append(float(x))

print(c)
print(c2)

# Map function: it uses map(func, variable)

coll = [10, 20, 30, 40]
coll2 = []

y = list(map(lambda x: x**2, coll))
print(y)


# Filter function:

ages = [16, 28, 20, 50, 48, 10, 39, 48, 58, 76, 97, 90, 9, 3, 11, 14]
print(ages)


def adult(ages):
    return ages >= 18


adults = list(filter(adult, ages))
print(adults)
# OR
adults2 = list(filter(lambda x: x >= 18, ages))
print(adults2)
