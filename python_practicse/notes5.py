# Global and local variables
# all variables are limited to scope or certain boundary beyond which they are not visible/defined
# global variables:defined before the main and executes as default
# local varibales: defined inside a function and does not affect global variable
# local variable can be set as global variable by using global keyword
x = 10  # global variable
print(x)


def var():
    x = 5  # local variable
    print(x)


var()


def newvar():
    global x
    x = 7
    print(x)


newvar()
print(x)
