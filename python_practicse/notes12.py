# OOPS: Obejct Oriented Programming System
# Class and objects
# the concept of object is considered which consits the data

# Encapsulation: The ability to hide the details of the object from the program so that the object can be used without knowing the internal working
# Inheritance: it is ability to give the properties of one class to another class. i.e parent and child class
# Polymorphism: it is ability of different object to respond in different ways depending upon the way they are implemented
# Abstraction: it is ability to define and work with object with their general characterstics rather than how they are defined

# Create a Class
class customer:
    bank_name = 'ABC Bank'

    def greet(self):  # self is parameter which is the variables reference
        print(f'Hi and Welcome to {self.bank_name}')


c1 = customer()
c1.bank_name  # it gives the __main__.class name
c1.greet()  # here it is basically customer.greet(c1) when we use self parameter in the function
print(type(c1))

c2 = customer()
print(c2.bank_name)
c2.greet()
# Class-->Obects(instances)|--->Identity (name of the variable storing the object)
#                          |--->Attributes(variables in a class)
#                          |--->Methods(function on the objects)

# Class Attributes: Variables shared with every object in the class
# Method is the functions created inside the class
