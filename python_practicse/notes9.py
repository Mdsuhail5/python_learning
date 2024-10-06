import copy
# String Methods
a = 'qwerty123'
print(dir(a))

# Testing methods: all the methods which have is in method
print(a.isalpha())
print(a.isalnum())
print(a. isascii())
print(a. isdecimal())
print(a. isdigit())
print(a. isidentifier())
print(a. islower())
print(a. isnumeric())
print(a. isprintable())
print(a. isspace())
print(a. istitle())
print(a. isupper())

print(a.startswith('hello'))
print(a.startswith('q'))
print(a.endswith('3'))

b = '      go go go go     '
print(b.replace(" ", "*"))
print(b.lstrip('*'))
print(b.rstrip())

# String Methods: every method in string class

z = 'heLLo WorLd'
print(z.capitalize())  # capitalize first word of the sentence
print(z.casefold())  # agressive lowercase
print(z.lower())  # lowercase
print(z.upper())  # converts all to upper case
print(z.swapcase())  # swaps lower to upper and upper to lower
print(z.title())  # first letter of every word is capital


h = 'A B C D E'
print(h.split())
print(h.split(' ', 2))
print(h.rsplit(' ', 2))
i = ['A B C', 'D', 'E']
print(' '.join(i))
print('---'.join(i))
j = "joker is releasing"
print(j.find('i'))
print(j.rfind('i'))
print(j.rindex('i'))
print(j.index('i'))


# Lists: Square brackets []
# Ordered,Changeable and allows duplicate

l1 = ['a', 'b', 'c']
l2 = [1, 3.0, 6j, 8, 9]
l3 = [True, False, True, False]
l4 = ['a', 'b', 'c', 30, 2, 4, 'd']

print(l1, l2, l3, l4, sep='\n')

l5 = list(range(5))
print(l5)

l6 = list(range(2, 8, 2))
print(l6)

# String Format: 3 ways to format
age = 31
school = 'ABC University'
text = ' I am {} age years old and study in {}'
print(text.format(age, school))

text2 = ' I am {} age years old and study in {}'.format(age, school)
print(text2)

text3 = f' I am {age} age years old and study in {school}'
print(text3)

# List methods
# To add
lu1 = [10, 20, 30]
lu1.append(40)
print(lu1)
lu2 = ['Mango', 'Apple', 'Bannana']
lu2.insert(1, "strawberry")
print(lu2)


lu1.extend(lu2)
print(lu1)

# To remove
lu1.remove('Apple')
print(lu1)

lu1.pop()
print(lu1)

lu1.pop(3)
print(lu1)

del lu1[2:5]
print(lu1)
lu1.clear()
print(lu1)

# list index
fruits = ['Banana', 'Papaya', 'Cherries', 'Apples', 'Papaya']
print(fruits.index('Apples'))

# to count the number of items repeated
print(fruits.count('Papaya'))

# to reverse a list
print(fruits[::-1])

fruits.reverse()  # it reverses the original list
print(fruits)

# sort method: used to sort list in aplhanumerically
fruits.sort()
print(fruits)

# to sort in descending order
fruits.sort(reverse=True)
print(fruits)

fruits1 = ['Banana', 'apple', 'Papaya', 'Cherries', 'Apples', 'Papaya']
fruits1.sort()
print(fruits1)

print(ord('A'))
print(ord('a'))

fruits1.sort(key=str.lower)

# copy
l3 = ['Samsung', 'Vivo', 'Apple']
l4 = l3
print(l3)
print(l4)

l3.append("gogo")
print(l4)

l3.clear()
print(l4)

# max() and min()
los = [4, 8, 10, 9, 8, 34, 56, 87]
print(max(los))
print(min(los))
# membership
print(87 in los)
print(10 not in los)

# Nested lists
l1 = [[1, 2, 3], [4, 5, 6]]
l2 = [7, 8, 9]
l1.append(l2)
print(l1)
print(l1[1][0])
print(l1[2][2])
print("-----------------")
l3 = l1.copy()
print(l3)
l3.pop(1)
print(l3)
print(l1)


# list comprehension
# [item (expression) for item in collection if condition=True]
names = ['anna', 'akii', 'naman', 'hitesh', 'gola']
names_with_a = [x for x in names if 'a' in x]
print(names_with_a)

double_from_0_to_10 = [x*1.5 for x in range(11) if (x*1.5) % 2 == 0]
print(double_from_0_to_10)

matrix = [[x for x in range(4)] for y in range(4)]
print(matrix)

matrix1 = []
for i in range(4):
    matrix1.append([])
    for j in range(4):
        matrix1[i].append(j)


print(matrix1)

for row in matrix1:
    print(row)
