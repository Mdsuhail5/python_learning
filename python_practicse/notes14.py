class Student:
    school = 'ABC school'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'Name: {self.name}, Age: {self.age}')

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def is_adult(age):
        return age >= 18


s1 = Student('Rohan', 12)
s1.display()
print(s1.get_school())
print(s1.is_adult(18))

# object composition: passing an object one class to another class


class Engine:
    def __init__(self):
        self.power = 100

    def start(self):
        print('Engine starts')


class Car:
    def __init__(self):
        self.Engine = Engine()

    def move(self):
        self.Engine.start()
        print('Car is moving')


c = Car()
c.move()
