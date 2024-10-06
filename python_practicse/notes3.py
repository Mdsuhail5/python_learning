# Operators
x = 10
y = 5

# Artihmetic Operators
# Addition
print(x+y)
# Subraction
print(x-y)
# Mulltiplication
print(x*y)
# Division
print(x/y)
# Modulus
print(x % y)  # gives remainders
# Power
print(x**y)  # gives power to
# floor division
print(10//3)  # gives only integer value and ignores decimal points

# Assignment Operators
# =,+=,-=,/=

# Comparison Operators
# ==,<=,>=,!=

# Logical Operators
# AND, OR, NOT

# Identity Operators
# is, is not
x = ['apple', 'banana']
y = ['apple', 'banana']
z = x
print(x is y)
print(x is z)
print(y is not x)
# Membership Operators
# in, not in
x = 'apple'
print('a' in x)
print('p' in x)
# Bitwise Operators
# AND(&)
x = 5  # binary: 101
y = 3  # binary: 011
result = x & y
# so here the result is 1 buz it does addtion of the two numbers in binary with AND logic
print(result)
# OR(|)
result = x | y
print(result)  # binary sum is 111 i.e 7
# XOR(^)
result = x ^ y  # xor is both conditions same means false otherwise true
print(result)  # 6
# NOT(~)
result = ~x  # x:101 and NOT of x: 010 and it takes 2's complement
print(result)  # 6
# Zero Fill Left shift(<<)
result = x << 1  # shifts the bits to one position left and 0
print(result)  # 1010
# Zero fill Right Shift(>>)
result = x >> 1  # shifts the bits to one position right and removes the right most bit
print(result)  # 10
