# Ecapsulation
class Car:
    __price = 5000  # private variable by using __
    _petrol = 3  # protected variable by using _

    def display_price(self):
        print(
            f'the price of the car is {self.__price} and petrol in car is {self._petrol}L')


c1 = Car()
c1.display_price()


# Inheritance
# Single level inheritance: methods and attributes and variables of parent class is passed to child class
# Multiple inheritance: two parent class with a child class
# Multilevel inheritance: base class -->intermediatory class --> child class
# Hierarchical inheritance --> one parent have many child class
# Hybrid inheritance --> many inheritance in combined #

# Single level inheritance
class A:
    def A(self) -> None:
        print('I am A')


class B(A):
    def B(self) -> None:
        print('I am B')


obj = B()
obj.A()
obj.B()

# Multiple inheritance


class D:
    def D(self) -> None:
        print('I am D')


class E:
    def E(self) -> None:
        print('I am E')


class F(D, E):
    def F(self) -> None:
        print('I am F')


obj = F()
obj.D()
obj.E()
obj.F()

# Multilevel inheritance


class G:
    def G(self) -> None:
        print('I am G')


class H(G):
    def H(self) -> None:
        print('I am H')


class I(H):
    def I(self) -> None:
        print('I am I')


obj = I()
obj.G()
obj.H()
obj.I()

# hirarchical inheritance


class J:
    def J(self) -> None:
        print('I am J')


class K(J):
    def K(self) -> None:
        print('I am K')


class L(J):
    def L(self) -> None:
        print('I am L')


obj = K()
obj.J()
obj.K()
obj1 = L()
obj1.J()
obj1.L()


class parent:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class child(parent):
    def __init__(self, name, age, school) -> None:
        # need to write super or parent name with .__ini__ to use(inherit) the parents variables defined
        super().__init__(name, age)
        self.school = school


obj = child('Rohan', 15, 'ABCD')
print(obj.name)
print(obj.age)
print(obj.school)
