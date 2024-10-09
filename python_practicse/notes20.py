# ZipFile
import zipfile

with zipfile.ZipFile('python_course.zip', 'w') as archive:
    archive.write('Pickle.bin')
    archive.write('T2.txt')
    archive.write('text.txt')
    archive.write('trail.txt')

with zipfile.ZipFile('python_course.zip', 'r') as archive:
    archive.extractall()

# working with directories and deleting files
import os

os.mkdir('Course')
if os.path.exists('Course'):
    os.rmdir('Course')
print(os.getcwd())
os.chdir('Course')
os.listdir()
os.remove('sr.txt')
