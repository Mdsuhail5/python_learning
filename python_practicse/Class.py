# 1.Classes
# 2.Constructors
# 3.Attributes (Class attributes vs Instance attributes)
# 4.Methods (Class methods vs Instance methods)


# Class: blueprint for creating new objects
# Objects: instance of a class

# Class: Human
# Objects: John,Mary,Jack

# Custom class

class Point:
    def draw(self):
        print("draw")


point = Point()
point.draw()

print(type(point))
print(isinstance(point, Point))

# Constructors: special method called when we instanciate a new object
# __init__ ->magic method
# self is a reference to current pointer object


class Dot:
    default_color = "red"  # class level attribute

    def __init__(self, x, y):  # __init__ is a constructor
        self.x = x  # it is a attribute (like field)
        self.y = y

    def radius(self):
        print(f"radius ({self.x},{self.y})")


dot = Dot(3, 4)  # Dot constructor pass the value to __init__
dot.radius()
dot.z = 40  # it is dynamic and need not be defined to be created

# Class vs instance attributes

# attributes that are defined for an instance of a class or object and can have different value
another = Dot(4, 5)
another.radius()

# class arttributes ae defined at class level and are same across all instances of class
print(dot.default_color)  # class level attribute using the object
print(Dot.default_color)  # class level attribute using the class
# if we change class level attribute by
Dot.default_color = "yellow"
print(dot.default_color)
print(another.default_color)
# the change is visible in all the objects

# the method decleared in the class should have atleast one parameter(self)


# Class methods
# methods used by class to intialzing a object values
@classmethod
def zero(cls):
    return cls(0, 0)


doint = Point.zero()
# same as
doint = Point(0, 0)

# Magic methods
# __init__
# __str__
# __cmp__
# __eq__
