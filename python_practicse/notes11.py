# tuples: rounded brackets
# ordere,immutable,allows duplicate
import ast
t1 = (10, 20, 30, 40, 50, 50, 50)
print(t1)
print(type(t1))
print(len(t1))

t2 = (1,)
print(t2)
print(type(t2))
print(len(t2))
# for tuple we can convert it into list and can do changes and convert back to tuple

# packing and unpacking of tuple
tup1 = ('A', 'B', 'C')  # packing of tuple
a, b, c = tup1  # unpacking of tuple
print(a, b, c, sep="\n")

# Note the no of elements in tuple should be equal to no of variables it is unpacking or else in would raise an error
# or else can use *variable name to unpack all the remining elements
tup2 = ('A', 'B', 'C', 'D', 'E', 'F', 'F', 'G')
a, b, *c = tup2
print(a, b, c, sep="\n")

# tuple methods: it had two methods that is count and index
print(tup2.count('F'))
print(tup2.index('F'))

t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)
t3 = t1+t2
print(t3)
print(t3*3)

# Dictionaries:dict()
# Ordered,Changeable,allow duplicate values but not key
# {Key:Value}
d = {
    'Name': 'Rohan',
    'Age': 23,
    'Car': 'Huyndai'
}
print(d)
print(d['Age'])
print(d.get("Car"))
print(d.keys())
print(d.values())
print(d.items())  # .items() gives all the key value pairs in a tuple in a list

d['Age'] = 20
print(d)
# use update and remove,pop method to add or delete a dictionary item
# to convet a list into dict
d1 = [('a', 1), ('b', 2), ('c', 3)]
d2 = dict(d1)
print(d2)

# to convert a string into dict
key = [2, 4, 6]
value = ['hi', 'hello', 'bye']
d3 = dict(zip(key, value))
print(d3)

# string into dict by using ast module
# import ast
str = "{'name': 'John', 'age': 30}"
d1 = ast.literal_eval(str)
print(d1)


# looping in dict by items method which gives all the items in a string
for x in d.items():  # x=(k,v) here this is happening
    print(x)

for x, y in d.items():
    print(x, y)


# sorting in dict using the sorted function
d = {'a': 2, 'b': 3, 'c': 1, 'd': 4}
x = sorted(d.items())
print(x)

# to sort by values
d = {'a': 2, 'b': 3, 'c': 1, 'd': 4}
x = sorted(d.items(), key=lambda item: item[1])
print(x)
#
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)


def merge(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(merge(dict1, dict2))
'''

# Sets:
# Unordered, Unchangeable, cannot have duplicates
sets = {1, 2, 3, 'yo', 'ko'}
print(sets)

# we cannot change directly but we can remove and add by method
sets.add(7)
print(sets)
sets2 = {67}
sets.update(sets2)
print(sets)

sets.remove(67)
print(sets)

sets.discard('ko')  # will not raise an error if the item is not present
print(sets)

sets.pop()  # removes the frist item but we dont know what is the first item
print(sets)

sets.clear()
print(sets)

s1 = {'a', 'b', 'c', 'd'}
s2 = {'c', 'd', 'e', 'f'}
s3 = s1.union(s2)
print(s3)
s3 = s1.intersection(s2)  # all elements present in both sets
print(s3)
s3 = s1.symmetric_difference(s2)  # elements present on all sets exactly once
print(s3)
s3 = s1-s2
print(s3)
s3 = s2-s1
print(s3)
'''
