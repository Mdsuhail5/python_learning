# list()
# tuple()
# set()
# dict()
# stack -> using list
# queue ->deque
# array=array("i",listofnumber)


# stack: it is datatype that use LIFO principle
# the item which goes last comes out first
from sys import getsizeof
from array import array
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:  # not borwsing_session is ![] gives true
    browsing_session[-1]


string = "hello, how are your?"
print(string.split())

# tuples: read only list ,cannot add,modify or remove an object, used for only when we dont need to change the data
point = ()
print(type(point))

point = (1, 2)+(3, 4)
print(point)
point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point[0:2])

point = (1, 2, 3)
x, y, z = point
print(x, y, z)

x = 10
y = 11
z = x
x = y
y = z
print(x, y)


a = 1
b = 2
a, b = b, a
print("a: ", a, "b: ", b)


# array:store same type of multiple objects
# use array for large sequence of problem and for optimiziation problems
# otherwise use lists and tuples by default
numm = array("i", [1, 2, 3])
numm.append(4)
numm.insert(0, 5)
print(numm)

numm.pop()
numm.remove(5)
print(numm)


# sets: a collection of objects with no duplicates #mutable
# set is unordered collection of unique items
set1 = {1, 2}
print(set1)

numb = [1, 2, 1, 3, 4]
numbset = set(numb)
print(numbset)

set1.add(3)
set1.remove(1)
print(len(set1))
print(set1)

first = {1, 1, 2, 3, 4}
second = {1, 5}
print(first | second)  # union
print(first & second)  # intersection
print(first - second)  # difference
print(first ^ second)  # sematic difference

if 1 in first:
    print("yes")

# dictionary: collection of key value pairs
# name->contact

dict1 = {"x": 1, "y": 2}
print(dict1)
p = dict(x=5, y=8)
print(p)
print(p["x"])
p["x"] = 10
p["z"] = 20
print(p)
if "a" in p:
    print(p["a"])
print(p.get("a", 0))

for key in p:
    print(key, p[key])

for key in p.items():
    print(key)

for key, val in p.items():
    print(key, val)

# dictionary comprehension
values = [x*2 for x in range(5)]  # list comprehension
print(values)
value = {x*2 for x in range(5)}  # set comprehension
print(value)
val = {x: x*2 for x in range(5)}  # dictionary comprehension
print(val)


# generators: used with working with large amount of data
# using list comprehension expression in a tuple brackets
# generator objects dont store all the objects in the memory and a new object is generated every iteration

va = (x*2 for x in range(10))
print(va)
for x in va:
    print(x)
print("gen: ", getsizeof(va))

# (*)unpacking operator: used to take out individual values in any iterable
numbe = [1, 2, 3]
print(*numbe)  # 1 2 3

v = list(range(5))
v = [*range(5), *"Hello"]
print(v)

# dictionary unpacking
Ist = {"x": 1}
IInd = {"x": 10, "y": 20}
combined = {**Ist, **IInd, "z": 1}
print(combined)
