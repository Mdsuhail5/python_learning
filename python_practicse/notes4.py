# Iterations: for loops

# range(end)
# range(start,end)
# range(start,end,sep)

for x in range(2, 10, 2):
    print(x)

# Nested loops

colors = ['red', 'white', 'black']
transport = ['car', 'bike', 'scooter']
for x in colors:
    for y in transport:
        print(x, y)

# assert keyword: test if a condition is True and if it is false it raises Assertion error
# debugging code
x = 'hello'

assert x == 'hello'
# assert x == 'bye', 'X is not bye but hello'

# Function: A block of code which only runs when it is called
# Defining a function


def greeting():
    print("Hello World")


greeting()
# Method: a function performed on objects where the function belongs to certain class.

# return: it is used to get a value from a function


def morning():
    return 'Good Morning everyone'


print(morning())


def multiply(x, y):
    return x*y


def apply(func, x, y):
    return func(x, y)


result = apply(multiply, 5, 10)
print(result)


# Formal Arguments(Parameters) and Actual Arguments(Arguments)

def f1(x, y):  # here the defined parameters are called formal arguments
    return x*y


print(f1(2, 5))  # here the values passed is known as Actual arguments
# Postional arguments are the arguments that are passed in certain order to formal agruments


# Arbitrary Arguments, *args
# it is used when we dont know how many number of actual arguments are being passed
def my_function(*name):
    for x in name:
        print('Hello', x)


my_function('A', 'b', 'c', 'd', 'e')
my_function('A', 'B', 'C', 'D', 'E', 'F', 'G')

# Arbitrary Keyword Arguments, **kwargs
# used when we dont know the number of parameters to pass so we take all the actual arguments as a dictionary


def my_de(**details):
    for key, value in details.items():
        print(key, value)


my_de(name='A', surname='B', age='27')

# Default parameter: used when a function is called but without any arguments


def mylf(name='User'):
    print(name)


mylf('Java')
mylf('python')
mylf()
