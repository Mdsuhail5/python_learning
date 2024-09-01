# lists are mutable as we can change the list or add new element and it is stored in the same memory
# variables are immutable as any change in the variable it is stored in different location

# lists
numbers = [1, 2, 3, 4, 5]
print(numbers)

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)

zeros = [0]*100
print(zeros)

x = list(range(20))
print(x)

h = matrix + x
print(h)

input1 = list("hello world")
print(input1)

# accessing items
letters = ["a", "b", 1, 3, 5, "C"]
print(letters)
print(letters[0])
print(type(letters))
print(letters[-1])
print(letters[0:4])
print(letters[0:6:2])
print(letters[::-1])

# list unpacking
listno = [1, 2, 3, 4, 4, 4, 4, 4, 9]
first = listno[0]
second = listno[1]
print(first, second)
fst, scnd, *others = listno
print(fst)
print(scnd)
print(*others)

f1, *other, s2 = listno
print(f1)
print(*other)
print(s2)


# enumerators: it is used to create enumerate object which is iterable
# we get tuple (0,"a") index and the item
lttr = ["a", "b", "c"]
for x in enumerate(lttr):
    print(x)
# O/P
# (0, 'a')
# (1, 'b')
# (2, 'c')

lttr = ["a", "b", "c"]
for x in enumerate(lttr):
    print(x[0], x[1])
    # 0 a
    # 1 b
    # 2 c

lttr = ["a", "b", "c"]
for x, y in enumerate(lttr):
    print(x, y)
    # 0 a
    # 1 b
    # 2 c

# Add in a list
letters1 = ["a", "b", "c"]
letters1.append("d")  # used to insert element at the last of the list
print(letters1)
letters1.insert(0, "-")  # used to insert element in a specific postions
print(letters1)
# Remove
letters1.pop()  # used to element from last
print(letters1)

letters1.remove("b")  # remove specific element
print(letters1)

del letters[0:3]  # used to delete a range of elements
print(letters1)

print(letters1.clear())  # used to clear all the elements in the list
# o/p None

let = ["a", "b", "c"]
print(let.index("b"))  # o/p 1, used to find the index of the object
# if the element is not present in the list it will give error
# to overcome this we use
if "d" in let:
    print(let.index("d"))  # gives nothing if not present
# or
# check the count of the d in list
print(let.count("d"))  # gives 0 if not present


# sorting a list
number = [3, 30, 45, 67, 14]
number.sort()  # method used to sort the list and is stored in the list no new list is created
print(number)
# to sort in descending order use the argument reverse=True
number.sort(reverse=True)
print(number)

# another method
print(sorted(number))  # sort and gives new list
print(sorted(number, reverse=True))  # gives descending sorted list


# to sort a list of tuples
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(items):
    return items[1]


items.sort(key=sort_item)
print(items)


# this can be done by lambda function easily
items.sort(key=lambda items: items[1])
print(items)

# Map function
prices = list(map(lambda item: item[1], items))
print(prices)
# it maps the lambda function to each item in the list

# to filter the list by only getting the product with greater value than 9
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# list comprehension
# syntax: [expression for item in items]
# we can use list comprehension in place of map and filter as they are
# more functional oriented programming
# for filter we use it
pr = [item[1] for item in items]
print(pr)

# for map
mapped = [item for item in items if item[1] >= 10]
#    the return expression          expression

# zip function; used to zip the elements of lists into a list of tuple
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))
print(list(zip("abc", list1, list2)))
# o/p
# [(1, 10), (2, 20), (3, 30)]
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
