from timeit import timeit  # used to time the code that runs
code1 = '''def xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age


try:
    xfactor(0)
except ValueError as error:
    print(error)'''

print("time taken code1= ", timeit(code1, number=1000))


code2 = '''
def xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor(0)
if xfactor ==None:
    pass
'''
print("time taken code2= ", timeit(code2, number=1000))
# use none and pass for more efficient and optimized code and raise exception only when needed
