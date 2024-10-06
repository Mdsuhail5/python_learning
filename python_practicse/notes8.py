# Strings
a = "hello world!"
c = '''hello
world
is 
here'''
print(c)
print(len(c))
print(dir(c))  # here the methods in double underscore (i.e __add__ ) is called dunder method and without underscore is the method that can be used on the string
print(c.split())
print(len(c.split()))  # determines the number of words in a sentence

# Strings are immutable i.e no changes are made to orginial string instead it creates a new object if any operation is performed on a string
a = "hello "
print(a)
print(a * 2)
print()

# Indexing
d = "Python is a programming language"
print('a' in d)
print('java' not in d)
print(d[1])
print(d[-len(d)+1])

# Slicing
# variable[start:End-1:step]
print(d[:5])
print(d[0:18:2])

g = 'it is good to see you today'
reverse_g = g[::-1]
print(reverse_g)

t = 'malayalam'
r_t = t[::-1]
print(r_t)
if t == r_t:
    print('its a palindrome')
else:
    print("its not a palindrome")
