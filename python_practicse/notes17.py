# Polymorphism: Overloading and Overriding
# a funciton acting in different way based on the value sent to that function
# Method Resolution Order:The order in which the pyton interpreter searchs for a method in inheritance heirarchy
# Duck Typing: if it quacks like a duck, behave like a duck, walks like a duck then it is a duck
# meaning when a function is created for specific purpose and other variables can use and benifit same as the function created for.
# the principle that objects are judge by their behaviour,rather than their class
# Overloading
def f1(x, y=None, z=None):
    if y and z:
        print(x*y*z)
    elif y:
        print(x*y)
    else:
        print(x)


f1(10)
f1(10, 20)
f1(10, 20, 30)


class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length*self.width
        return area

    def perimeter(self):
        perimeter = 2*(self.length + self.width)
        return perimeter


rec = rectangle(5, 3)
print(rec.area())
print(rec.perimeter())


def divide(x, y):
    try:
        z = float(x/y)
        print(z)
    except ZeroDivisionError:
        return "Cannot divide by zero"


divide(10, 2)
