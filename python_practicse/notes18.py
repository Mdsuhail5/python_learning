# File Handling
# open(filename,mode)
# mode;
# r: read
# w: write
# a: append
# x" Create

f = open('trail.txt', 'w')
f.write("hey this is my text file")
f.close()

# a file must be closed after the work has done
# or with can be used which closes file automatically
with open('T2.txt', 'a') as f:
    f.write('tiy tiy tiy')

f = open('T2.txt', 'r')
text = f.read()
print(text)
