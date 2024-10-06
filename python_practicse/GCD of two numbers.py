# to find gcd of two numbers

def gcd(x, y):
    result = min(x, y)
    while (result):
        if x % result == 0 and y % result == 0:
            break
        else:
            result -= 1

    return result


x = int(input('x '))
y = int(input('y '))
print(gcd(x, y))
