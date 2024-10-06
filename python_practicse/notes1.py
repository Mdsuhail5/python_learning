'''
Python:
      High-Level: human level lang 
      Object oriented: contains class and objects
      Interpreted: line by line
      Dynamic Semantics: not need to declare the data type
      General purpose : can be used for anything
      Glue Language: can be used to integrate different technologies
      simple syntax: indentations
      Libraries and modules: supports

'''

# Data types
# 1.Numbers

# int: whole number without decimal
a = 10
print(a)
print(type(a))

# float: floating point number has decimal point, and can contain 'e' which is 10 to the power.
b = 10.8
print(b)
print(type(b))

# complex: contains real part(a number) and imaginary part(j).
c = 10+3j
print(c)
print(type(c))

d = 2e3j
print(d)
print(type(d))

# General Functions:
# type(): determines the data type

# 2. Strings
e = "Hello World"
print(type(e))
print(type('Hello World'))

# 3.Boolean: True or False
print(True)
print(False)
print(type(True))
print(type(False))

# 4.None: Absence of a value
print(None)
print(type(None))

# 5.Sequences:
'''they have these properties
Ordered collection
Slicing
Concatination
Repetitaion
Membership testing
'''

# Strings
s1 = 'Hello World'
print(s1)

# Lists: Square Brackets, mutable(can be changed)
l1 = [10, 20, 30, 40]
print(l1)
print(type(l1))

# Tuples: Round Brackets, immutable(cannnot be changed)
t1 = (10, 20, 30, 40)
print(t1)
print(type(t1))

# 6.Sets: flower bracket, unordered, unique
set1 = {10, 20, 30, 40, 40}
print(set1)
print(type(set1))

# 7.Dictionaries: Key:Value pair,mutable
d1 = {
    'Name': 'John',
    'age': '31'
}
print(d1)
print(type(d1))
