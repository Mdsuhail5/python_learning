# Pickle : used to store the results of the program and use it wherever u want to use
# Seralization: dump()
# DeSeralization: load()
# by using pickle module
import pickle

result = {'a': 1, 'b': 2, 'c': 3}

with open('Pickle.bin', 'wb') as f:
    pickle.dump(result, f)

with open('Pickle.bin', 'rb') as f:
    text = pickle.load(f)
    print(text)


# seek(): used to start the postion in a file
# tell(): used to tell postion from where the file is starting and ending
with open('text.txt', 'a') as f:
    f.write('I am appending to this file')

with open('text.txt', 'r') as f:
    print(f.seek(4))
    print(f.tell())
    print(f.read())
