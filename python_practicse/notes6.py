# Recursion: a function call itself again and again


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(4))  # 4*3*2*1

# NOTE: a factorial has a maximum depth of 1000 i.e it can run only 1000 times and exceeding it can give error
