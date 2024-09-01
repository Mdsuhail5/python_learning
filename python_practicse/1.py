a = 4
print(a)
b = 2+5
print(b)


def multiply(*tuple):
    total = 1
    for number in tuple:
        total *= number
    print(total)
    print(type(tuple))


multiply(1, 2, 3, 4)
